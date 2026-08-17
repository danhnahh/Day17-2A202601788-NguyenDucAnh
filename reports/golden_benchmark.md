# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1022.8 ms**
- Average token reduction vs full source context: **14.5%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1457.1 | 712 | 0.0% |  |
| G09 | semantic | PASS | 227.9 | 148 | 67.8% |  |
| G10 | semantic | PASS | 286.2 | 95 | 79.3% |  |
| G14 | mixed | PASS | 1526.6 | 431 | 0.0% |  |
| G03 | long_term | PASS | 1621.4 | 1509 | 0.0% |  |
| G04 | long_term | PASS | 1395.3 | 1505 | 0.0% |  |
| G07 | episodic | PASS | 237.8 | 272 | 0.0% |  |
| G08 | episodic | PASS | 209.3 | 339 | 0.0% |  |
| G11 | mixed | PASS | 1836.4 | 439 | 22.3% |  |
| G13 | mixed | PASS | 396.6 | 406 | 28.1% |  |
| G15 | mixed | PASS | 1795.6 | 736 | 0.0% |  |
| G16 | mixed | PASS | 1320.8 | 484 | 14.3% |  |
| G17 | mixed | PASS | 1826.4 | 484 | 14.3% |  |
| G18 | mixed | PASS | 480.0 | 403 | 28.7% |  |
| G19 | mixed | PASS | 1463.4 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1195.5 | 1503 | 0.0% |  |
| G12 | mixed | PASS | 1530.7 | 431 | 31.8% |  |
| G20 | mixed | PASS | 1649.2 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88, prioritizing Java and Spring Boot for backend development, and not using Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPISODES>  <FACTS`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88, prioritizing Java and Spring Boot for backend development, and not using Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPISO`

### G03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he prefers short ex`

### G04 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he prefers short ex`

### G07 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi dang hoc as`

### G08 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cuoi tu`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G13 - mixed

`<EPISODIC> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chi`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G18 - mixed

`<EPISODIC> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G05 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he prefers short ex`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which he prefers to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is studying async/await in programming and sometimes confuses coroutines with Tasks. He has a task to complete a benchmark report by Friday at 16:00, related to LAB-REPORT-1600. Currently, Minh is debugging async HTTP issues, including connection churn, and has explored solutions like reusing aiohttp ClientSession and setting concurrency to 20. This is linked to the ASYNC-FIX-20 incident.  Minh likes Python and dislikes Java. When explaining code, he pref`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
