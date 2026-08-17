# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **945.7 ms**
- Average token reduction vs full source context: **14.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 779.9 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1342.9 | 828 | 0.0% |  |
| E10 | short_term | PASS | 0.4 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1875.5 | 1399 | 0.0% |  |
| E03 | long_term | PASS | 1838.3 | 1413 | 0.0% |  |
| E04 | episodic | PASS | 443.0 | 284 | 0.0% |  |
| E05 | episodic | PASS | 295.9 | 303 | 0.0% |  |
| E07 | mixed | PASS | 2228.2 | 485 | 14.2% |  |
| E11 | semantic | PASS | 252.0 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1346.6 | 1359 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88, and they prioritize using Java and Spring Boot for backend examples. They do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Python is still preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining async/await, coroutines, and Tasks, Minh will prioritize the timeline. In Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks."  When explaining async/await, coroutines, and Tasks, explain using a timeline. The user stated in Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks." </USER_SUMMARY>  <EPISODES> Episodes are source message o`

### E03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Python is still preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining async/await, coroutines, and Tasks, Minh will prioritize the timeline. In Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks."  When explaining async/await, coroutines, and Tasks, explain using a timeline. The user stated in Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks." </USER_SUMMARY>  <EPISODES> Episodes are source message o`

### E04 - episodic

`EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout th`

### E05 - episodic

`EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat conc`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Python is still preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining async/await, coroutines, and Tasks, Minh will prioritize the timeline. In Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks."  When explaining async/await, coroutines, and Tasks, explain using a timeline. The user stated in Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks." </USER_SUMMARY>  <EPISODES> Episodes are sour`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Python is still preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining async/await, coroutines, and Tasks, Minh will prioritize the timeline. In Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks."  When explaining async/await, coroutines, and Tasks, explain using a timeline. The user stated in Vietnamese: "I will prioritize the timeline when explaining coroutines and Tasks." </USER_SUMMARY>  <EPISODES> Episodes are source message o`
