# Memory vs No-Memory Comparison

| Metric | Memory-enabled | No-memory | Delta |
| --- | ---: | ---: | ---: |
| Evidence hit rate | 100.0% | 18.2% | +81.8% |
| Passed cases | 11/11 | 2/11 | +9 |
| Avg retrieval latency (ms) | 1625.1 | 0.0 | +1625.1 |
| Avg token reduction | 19.1% | 81.8% | -62.7% |

## Interpretation

Short-term cases can pass without durable memory because their evidence is still in the current thread. Cross-session, episodic and semantic cases should fail in the no-memory baseline and recover when memory retrieval is enabled.

A no-memory baseline may show near-100 percent token reduction simply because it retrieves nothing. Treat token reduction as useful only together with evidence hit rate; dropping all context is cheap but incorrect.