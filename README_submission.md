# Lab 17 — Bài nộp

**Kết quả:** practice 11/11 (100%); baseline no-memory 2/11 (18.2%).

## 1. Ba câu thực hành

**Layer quan trọng nhất: long-term.** Quyết định E02 (preference), E03 (open loop), E08 (recency), E09 (isolation) = 20/56đ, và một nửa E07. Baseline fail sạch 4 case này; short-term vẫn pass vì bằng chứng còn trong thread.

**Trade-off Zep vs Redis+Qdrant.** Zep tự trích entity/fact kèm `valid_at`/`invalid_at`; một call `thread.get_user_context` trả context đã xếp hạng relevance. Cái phải trả: ingest bất đồng bộ nên phải poll, latency 1.2–1.7s mỗi case long-term so với ~0ms của store local, và không kiểm soát được ranking. Redis+Qdrant cho toàn quyền và độ trễ gần 0, nhưng phải tự viết extraction, conflict resolution, recency, provenance — đúng bốn thứ tốn thời gian nhất.

**Guardrail chống memory poisoning.** (a) `consent.json` + `minimize_pii` chặn ingest khi chưa opt-in và redact PII. (b) Heartbeat chỉ được de-dup note, đánh dấu task stale, tạo recap — không tự ghi instruction mới vào durable memory. (c) `MEMORY_SCHEMA` bắt mọi record mang `source`/`timestamp`/`confidence`/`validity`, nên fact bịa không có provenance sẽ lộ.

## 2. Phân tích benchmark

1. **Layer yếu nhất:** student run không có, cả 4 layer 100%. Ở baseline, long_term/episodic/semantic đều 0%, chỉ short_term 2/2.
2. **Nhiều token nhất:** bốn case long-term chiếm trọn top (828–1413 token), dẫn đầu E03, do Context Block nối thêm `graph.search(scope="edges", limit=20)`.
3. **E07** cần long-term + semantic; evidence bắt buộc `Python` (user graph) và `Idempotency-Key` (KB chung).
4. **Token reduction:** memory 14.2% vs baseline 81.8%, nhưng hit rate 100% vs 18.2%. Baseline "tiết kiệm" vì không retrieve gì. Reduction chỉ có nghĩa khi đọc kèm hit rate.

## 3. E08 recency, E10 compaction

**E08:** BLUEBIRD-42 buộc TypeScript/NestJS dù Minh thích Python. `scope="edges"` trả fact kèm `valid_at`/`invalid_at` nên phân biệt được preference hiện hành với preference đã bị thay.

**E10:** hạ `max_recent_messages` 6→4, sliding giữ 4 message qua 12 lần compaction nhưng `REVIEW-DEADLINE-1600` vẫn sống trong `<DURABLE_NOTES>` nhờ `extract_durable_notes` bắt keyword `deadline` và regex marker. Buffer cũng giữ được nhưng vì không quên gì (16/16 message) nên không scale.
