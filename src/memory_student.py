from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4 -- done.
        #
        # Context Block is assembled by Zep from the *user graph*, but it needs a
        # current thread slice to know what "relevant" means right now. That is
        # why the eval query is written into a fresh thread first.
        prime_eval_thread(self.client, user_id, thread_id, query)

        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        # `.context` is the assembled string. Returning the object itself would
        # make the evaluator score a repr() instead of the memory text.
        context_block = getattr(user_context, "context", "") or ""

        # The Context Block is relevance-ranked and can drop a low-salience fact
        # such as an open loop (E03) or the superseded preference that proves
        # recency (E08). An edge search adds the raw facts *with* their
        # valid_at / invalid_at ranges, which is exactly the provenance needed to
        # argue "TypeScript is current, Python is history".
        # limit=20 because a small limit truncates before the deadline facts.
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            # A fact-search failure must not lose the Context Block we already have.
            fact_text = ""

        return join_nonempty([context_block, fact_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4 -- done.
        #
        # Episodic memory is per-user trajectory ("what did we try last time"),
        # so this searches the USER graph. Using graph_id here would return
        # shared domain knowledge and leak the layers into each other.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        # episode_char_cap: raw session messages are verbose and, under the 3%
        # episodic budget, two long transcripts would fill the whole slot and
        # push out the short reflection episode that actually carries the
        # markers (ASYNC-FIX-20, "connection churn"). Capping each episode keeps
        # more distinct episodes inside the same budget.
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4 -- done.
        #
        # Semantic memory is shared domain knowledge, not owned by any user, so
        # it lives on the standalone graph: graph_id, never user_id.
        q = cap_query(query)
        try:
            # scope="episodes" returns the raw ingested document text, which
            # preserves literal markers like PAYMENT-RULE-3 / CONN-POOL-FIRST.
            # scope="auto" would return extracted facts and silently drop those
            # codes, failing E06/E11 even though the retrieval "looks" correct.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Fallback for accounts/SDK builds where the episodes scope differs.
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        # No episode_char_cap here: semantic documents put their markers at the
        # END of the text, so truncating each episode would cut them off.
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4 -- done.
        #
        # ContextBudgetManager already encodes the lab's teaching budget
        # (short-term 10% / long-term 4% / episodic 3% / semantic 3%) and walks
        # the layers in priority order short_term -> long_term -> episodic ->
        # semantic, trimming each from the tail. Returns (merged_text, breakdown).
        return self.budget.assemble(layers)
