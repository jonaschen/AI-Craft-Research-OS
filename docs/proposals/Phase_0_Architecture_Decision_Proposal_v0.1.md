# AI Craft Research OS — Phase 0 架構決策與研究準備建議書 v0.1

**文件性質：**供 Human Research Director 審閱的建議書（Proposal，不是已通過 ADR 或實作授權）  
**日期：**2026-10-21  
**目標專案：**`AI-Craft-Research-OS`  
**建議存放位置：**`docs/proposals/Phase_0_Architecture_Decision_Proposal_v0.1.md`  
**狀態：**Reviewed draft / Pending owner approval  
**涵蓋：**五項架構問題、RQ-001 的研究邊界、文件一致性修正、後續作業與停止條件

## 0. 執行摘要與建議決策

**長期產品／研究願景：**使用者提供研究目標與基本資源政策；獨立 Orchestrator 依任務需要決定協作拓樸、Session、模型及執行時機；再由預先定義的外部證據與 Oracle 判斷決策是否合理。Research Team 既是研究工具，也是研究對象。這是**尚待驗證的目標架構**，不是現有產品能力。

**近期研究範圍：**RQ-001 只研究「任務開始前，依固定特徵決定是否進行跨 Session Reviewer 審查」的靜態選擇政策（Selective Review）。這是自適應協作的一個最小可測子問題，**不代表 Adaptive Orchestration 只允許事前決策**。

**本建議書推薦：**

1. 同意以 **P0 單 Session 自我檢查、P1 Researcher→獨立 Reviewer→Researcher 一次修訂、P2 事前固定規則選擇 P0/P1** 作為 RQ-001 的待核准流程；對三者使用同一份最終產物契約、獨立 Oracle 與 task-level 總資源限制。
2. 同意控制權由**確定性 Control Function／Orchestrator** 掌握；Human 核准任務／政策／預算／發布；Agents 只能提出語義內容及有限請求，不能自授權、調整 Oracle 或擴張資源。
3. 同意先以 **Task、Session、Handoff、Artifact、Verdict** 五個概念契約與簡潔執行紀錄處理證據；不要提前建置通用 Agent Framework。
4. 同意以**全新、公開且授權允許的非 BSP／SoC／AOSP 一般軟體文件**建立兩份紙上 Task/Oracle 範例；第一輪先做可行性與工時計算，試驗規模與數值門檻待確認後再凍結。
5. 維持 `AI-Craft-Research-OS` 作為獨立主線；原 `agent-skill-automation` 維持 Private，不直接移植程式碼、Prompt、Fixture、資料或歷史。

**不在本次授權範圍內：**任何模型試跑或消費、編寫 Runner、啟用 Agent、訓練或模型路由、提交／推送／公開 Repo、修改既有已發表文件；這些動作皆需另外取得核准。

---

## 1. 本建議書的證據基礎與界線

### 1.1 直接依據（已讀取的提供文件）

- `docs/architecture/Research_Team_Architecture_v0.1.md`：原始長期願景、Research Team Charter、概念 Schema、Phase 0–5、白皮書中的 ADR-001～004 編號。
- `docs/reviews/Research_Team_Architecture_Review_v0.1.md`：指出五項架構阻塞問題、效能評估不充分、預算介面未可證實、Git 追蹤及文獻證據限制。
- `docs/research/Research_Question_001_Draft.md`：具體描述 P0/P1/P2、固定事前規則、外部 Oracle、development/holdout 分離、使用量／失敗記錄。
- `docs/decisions/ADR-001_Independent_Orchestrator_Draft.md`：權限邊界、控制層的邏輯獨立性、資料來源限制、資源能力檢查和 ADR 編號衝突。
- 先前的 `Architecture_Discovery_Report.md` 與 `AI_Craft_Reuse_Decision.md`：對 Private 舊系統的 Codex 靜態檢視報告，**僅作內部背景、不得視為已獨立驗證的 Runtime 事實或直接引入公開文件的程式碼來源**。

### 1.2 證據狀態

上述 Codex 文件是**架構審閱與實驗規劃**，不是多代理系統性能的實驗證據。`Research_Question_001_Draft.md` 明言尚未預註冊、核准或執行；本建議書也不把政策效益、安全保證、成本節省當成已成立結論。

> 本文件的「建議」、「提議的約束」、「待凍結」均屬提案；任何尚無來源或實驗支撐的數值不得冒稱實測結果。

---

## 2. 五項最重要架構問題：建議與核准條件

### Q1. Adaptive 的範圍：先限定事前選擇性審查嗎？

**建議：RQ-001 是；平台長期架構不是。**

- RQ-001 的選擇政策輸入只能是**執行前真實可得**的任務特徵、已核准資料來源與明確的任務需求。政策版本、特徵值、分支決策、原因碼須在第一個模型呼叫前保存。
- P2 不得在評分後事後選出當次較佳策略；不得根據 hidden answer key、驗證結果、錯誤發生與否判斷是否審查。
- 執行中的動態擴員、模型切換、自我調整政策、平行 Agent、Peer Messaging 全部列入後續研究，不混入首輪比較。
- 狀態紀錄預留未來可合法重新決策的**概念欄位**，但 Phase 0 不設計可任意擴張的動態拓樸引擎。

**待 Human 核准：**確認本次驗證的是 *selective review workflow*，不是完整 adaptive team 的一般有效性。

### Q2. Reviewer 的發現如何進入修訂，品質怎麼獨立判定？

**建議的待核准 Finalization Contract：**

| 策略 | 草稿與修訂過程 | 交付結果 |
|---|---|---|
| P0 | Researcher 起草，於**同一 Session** 進行一次有界自我檢查／修訂 | Final Note + Claim/Source + Uncertainty |
| P1 | Researcher 起草 → **新 Reviewer Session** 獨立審查核准 corpus 與草稿 → Researcher 接收 findings 並**一次有界修訂** | 與 P0 同一 Final Artifact Contract + Reviewer Findings + Handoff |
| P2 | 已凍結、事前可重現的規則選擇 P0 或 P1 | 實際分支結果 + Policy Decision Record |

- Reviewer 提出的 finding 必須有 claim ID、所引用的 corpus locator、問題類型／嚴重度與建議；**finding 不是 Oracle verdict，也不是強制修改指令**。
- Researcher 可 `accept`、`reject`、`uncertain`；建議記錄判定及簡述理由。Reviewer 不得修改 task、oracle、預算或權限。
- 無 finding：保留「已審核但無變更」記錄；矛盾 finding：用證據判斷，可拒絕並說明；格式錯誤 finding：依事前失敗政策處理，不秘密要求人類代修；Reviewer 或修訂耗盡預算：保留部分產物，未完成必要最終產物即不能通過驗收。
- **外部 Oracle** 依事先固定的 answer key、claim rubric、來源支持與 critical-error 定義評估**最終產物**。結構及 locator 可機械驗證，語義正確性可能需要盲化人工審查；Reviewer 自評不能取代 Oracle。
- 額外記錄草稿→最終稿的 `corrected_errors`、`introduced_errors`、`unchanged_errors` 與人工判讀不確定性；若沒有可信的已知缺陷分母，不報 Reviewer Detection Recall。

**因果主張限制：**P0 與 P1 不只差一個 Agent，也差在獨立 Context、Reviewer 指令與交接開銷；因此第一輪比較的是**工作流程套裝效果**，不能聲稱純粹隔離了「Agent 數量」的因果效應。

**待 Human 核准：**固定最終修訂次數、空／錯誤 findings 的規則、Output Contract、Oracle rubric。

### Q3. 誰掌管權限、預算、重試與停止？限制無法執行時怎麼辦？

**權限分工：**

| 主體 | 掌握的權限 | 明確不允許 |
|---|---|---|
| Human Research Director | 核准特定 task、oracle、policy、模型／網路／輸入傳輸政策、預算與對外發布；最終研究結論 | 以主觀偏好私下更改已凍結評分以偏袒某策略 |
| Deterministic Control Function（將來的 Orchestrator） | 驗證合約、保存批准版本、發出有限 dispatch、控制狀態與 retry、保留 log、拒絕越權 | 自創答案、無紀錄追加花費、讓模型文字當核准令 |
| Researcher / Reviewer | 在已允許資料與工具內完成語義工作、提供輸出及建議 | 自行授權額外 Agent、變更 Oracle、讀取答案金鑰、對外發布 |
| Oracle／人工評分 | 依凍結 rubric 產生獨立判定 | 自動核准額外預算或重跑 |

**資源控制設計：**在 dispatch 前檢查權限、capability、剩餘 task-level token／成本／延遲額度；對要發出的請求預留有根據的資源上界，聚合所有 Session、Retry、Review、Revision 及可計費開銷。須區分 `reserved`、`observed`、`estimated`、`reconciled`、`unknown`。訂閱工具無可靠費用明細時，不應以未知值當 0，或宣稱已證明省錢。

**Fail closed：**如果 Provider／CLI 不能提供足以支持所聲稱的資源限制或取消／用量觀測能力，**不派發該執行**；回報 `UNSUPPORTED_CAPABILITY`／`BUDGET_UNVERIFIABLE`，待 Human 決定縮小契約、改選介面或改為不能宣稱硬性上限的研究模式。**不能僅靠 Prompt 承諾控制花費。**

**停止／恢復：**所有 timeout、取消、crash、重試、預算不足、human hold 應保存獨立 `execution_status`、`stop_reason` 和 lineage；不可默默重播已計費請求。Human Hold 的「暫停待核」與「終止」不可混為同一種狀態。這是待另行完成的狀態轉換規格，不表示 v0.1 已有可靠執行器。

### Q4. 最小契約：Task、Session、Handoff、Artifact 如何定義？

**建議先建立五個概念契約，不以此文件承諾固定程式 API：**

| 概念契約 | 最小可審閱欄位 | 必須守住的邊界 |
|---|---|---|
| Task Contract | `task_id`、`contract_version`、目標、資料來源／hash、輸出與 oracle version、核准特徵、權限、總預算、停止與人工核准政策 | Agent 不能覆寫或查看 hidden key |
| Session Specification | `session_id`、`attempt_id`、`role`、`model_id`、輸入 Context hash、工具 allowlist、局部預留額度、timeout、期望輸出 | Role、Agent Instance、Session、Model 不得混同 |
| Handoff Manifest | `task/contract_version`、來源 `attempt/session`、預期接收角色、artifact ID/hash、可用 corpus/version、預期欄位、大小限制 | 驗證來源、版本及 scope；不得偷偷傳更多歷史 Context |
| Artifact Manifest | `artifact_id`、型別、產出 Session、版本、內容 digest、路徑、來源與敏感性分類 | Hash 是內容識別，不是事實正確性或防竄改保證 |
| Oracle Verdict | `oracle_version`、最終 Artifact ID、結構檢查、Claim 正確／支持／coverage、critical errors、分數／不確定性 | Oracle 與 Runner 分離，固定 rubric 後才計算 |

每次 Trial 的執行紀錄另保留 `experiment_id`、`task_id`、`strategy_id`、`policy_version`、`trial_id`、`attempt_id`、`session_ids`、時間、Prompt/環境版本、全部產物摘要、usage 的來源及缺漏、失敗／人工介入、Oracle verdict。**Trial、Attempt、Session、Retry 是不同層級**。

Phase 0 只要求**兩份完整紙上實例**及其欄位一致性；暫不產生複雜 Schema Generator、資料庫、Message Bus、Provider Adapter Factory。後續需另寫最小狀態轉換表，才能討論執行器。

### Q5. 哪一組任務、模型、評分與資源能在 4–6h／週下公平比較？

**第一個任務家族建議：**凍結的一般軟體公開文件中，對指定技術主張進行證據查核／跨段落合成。暫不執行程式、安裝依賴或即時搜尋。原始文件來源、版本、取得日期、散布許可與 hash 須記錄；公開可讀不等於允許重新散布。只使用新建、已授權、與現職領域無重疊的材料。

**理由：**可預先建立 answer key、claim rubric 與穩定 citation locator；不像開放式「研究品質」那麼難判定，也避免在首輪混合軟體執行環境差異。

**漸進規模：**

1. **紙上設計（當前）：**先寫兩個獨立 Task/Oracle 範例，分別是單段證據核對與跨段落／多來源核對；不呼叫模型。
2. **Protocol feasibility（另經核准）：**選一個固定 Provider／model configuration，先評估是否能可靠取得 Token/Cost/Latency、隔離 Session、限制 Context 與預算；必要時做極少量 dry-run，只檢查程序能否執行，**不作效果宣稱**。
3. **Pilot（另經核准）：**Codex 的 RQ 草稿建議 6–10 任務、P0/P1/P2、各兩次，約 36–60 次 Trial（未計 Retry）。此規模目前只是成本估計情境，不是承諾。先估算人類評分與全部試次工時；無法承擔則先測 P0/P1，**P2 標為未測**。
4. **Held-out protocol：**以來源／主題家族拆分 development 與 held-out，先凍結 Task、權重、Policy、Prompts、Oracle、執行順序與 Retry 規則；P2 必須在實際事前執行決策，而非事後選勝者。極小資料集只報個案／可行性，不主張一般顯著性。

**公平性要點：**每個 Task 的公開輸入資料、基本 Researcher 指令、模型設定、工具權限、最終 Oracle 與總資源 Ceiling 一致；P0 可把限額用於自我檢查，P1 的 Review/Handoff/Revision 所耗全部合併計算；固定而保留無法完全消除的 Role/Context 差異。Trial 順序平衡；重複試驗不當作獨立任務。保存所有 timeout、rate-limit、invalid-output、失敗與缺失資料。

**Primary outcomes 建議：**（a）事前凍結 Oracle 的 task acceptance；（b）每個 attempted task 的總 Token（分 input/output/cache categories，若 Provider 可提供），以及另外報告金額、延遲與人工分鐘。Task Acceptance 不得只用來源 URL 存在或模型自評替代。

**數值門檻尚待核准，不能自行填值：**`quality_floor`、相對 P1 可接受品質損失、相對 P1 所需節省量、相對 P0 可容許資源增加量。若要說 P2 有效，須按凍結門檻共同滿足條件；小型 Pilot 的門檻比對只作描述，不能主張嚴格 noninferiority 或普遍優勢。

---

## 3. 文件一致性與正式決策順序

### 3.1 ADR 編號衝突（實際存在，必須解決）

白皮書 §13 規劃：
- `ADR-001 — Independent Research OS Repository`
- `ADR-002 — Deterministic Independent Orchestrator`
- `ADR-003 — Research Team as Experimental Subject`
- `ADR-004 — Static Policy before Learned Routing`

但 Codex 交付的 `ADR-001_Independent_Orchestrator_Draft.md` 把 Repository 邊界與 Orchestrator 邊界合併為 ADR-001；它自己也說明**尚未取代白皮書編號**。

**我的建議：**保留白皮書的 ADR-001～004 分工；將 Codex 合併草稿視為**內容參考來源**，於下一輪由 Codex 擬成兩份獨立的新草案：
- `ADR-001_Independent_Research_OS_Repository_Draft.md`
- `ADR-002_Deterministic_Independent_Orchestrator_Draft.md`

目前不要覆寫原草稿或聲稱兩份 ADR 已核准。ADR-003/004 可留待研究進一步成熟。

### 3.2 Git 追蹤與白皮書公開狀態

Codex 的 Architecture Review 記載，在它檢查時 `docs/architecture/` 尚未被 Git 追蹤；新產物引用白皮書，但當時遠端可能尚無該檔。**這是 Codex 在當時的觀察，不代表今天 Git 狀態仍相同。** 下一次需執行只讀 `git status`／`git ls-files` 檢查，再由 Human 確定是否納入版本管理。白皮書引用舊 Private 審查報告的部分，公開前應轉為可對外理解的「來源狀態與限制」，避免公開 Private 報告的敏感內容或誤稱已重驗證。

### 3.3 不要混淆核准層級

- **批准方向** ≠ 批准白皮書每個 Schema／Policy 細節。
- **批准 ADR** ≠ 批准 Runner 實作。
- **批准 Task/Oracle** ≠ 批准模型推論、外傳資料、花費或公開發布。
- **Paper Walkthrough 完成** ≠ Agent Team 已驗證可用。

---

## 4. 下一次研究時段：可交給 Codex 的有限任務

**前提：**Human 先核准本文件建議方向與明確的後續授權範圍；此處是工作提案，不構成 Codex 自動執行的指令。

**建議作業（控制在約 3–4 小時，可拆成兩次或更多研究時段）：**

| 工作 | 粗估時間 | 交付物 | 完成判準 |
|---|---:|---|---|
| Human 審定五項建議與待選門檻 | 30–45 分 | 審閱註記與開放問題 | 未核准事項逐項標記 |
| Codex 起草兩份全新紙上 Task/Oracle 範例 | 60–90 分 | 兩份獨立 Markdown 案例 | 含合規 Corpus Manifest、可判定 Claim Key；不啟動模型 Trial |
| 手工 Walkthrough：P0/P1/P2 資訊流與否定／失敗路徑 | 45–60 分 | 問題與修正記錄 | Key 不洩露；每一個 Session 都可指認輸入與產物 |
| 量測與評分時間估算 | 30–45 分 | Protocol Feasibility Estimate | 明確標示未知成本與 Provider 能力 |

下一輪若僅執行文件設計，仍不得修改現有正式架構稿、進行 Model Trial、呼叫額外 API、發布或 Push，除非 Human 在任務中另行核准。

### 4.1 進入實作前 Gate

必須同時滿足：

- [ ] Human 已明確選定 RQ-001 限縮範圍及 P0/P1/P2 Finalization 規則。
- [ ] 已有兩個可審的紙上 Task/Oracle 範例與有權使用的 Corpus Manifest。
- [ ] 最終 Artifact 欄位、Reviewer finding、Handoff 和 Oracle 評分規則互相一致。
- [ ] 資源政策、接口 capability 與未知用量的處理已確認。
- [ ] 狀態／停止／重試與 Human Hold 的生命週期至少有簡單轉換表。
- [ ] Development/Holdout、重複次數、順序、工作量估算和最低效果判定門檻已確認（或明確把相應比較延後）。
- [ ] IP、資料使用與授權、外傳、公開條件已核實。
- [ ] 新的實作工作獲得另一次 Human 授權。

---

## 5. 需要 Human Research Director 決定的事項

**建議先批准「方向」，不要一次批准所有細節。**

1. **範圍：**RQ-001 僅限事前 Selective Review（是／需修改）。
2. **角色與結案：**接受 P0 自我檢查一次、P1 獨立 Reviewer 加 Researcher 修訂一次的流程（是／需修改）。
3. **權限：**接受 Human 最終政策核准、確定性 Control Function 行使執行權限，以及 unsupported interface 時 fail closed（是／需修改）。
4. **契約：**同意優先寫五份輕量概念契約與兩份紙上實例、不先搭建框架（是／需修改）。
5. **測試領域：**同意從全新公開一般軟體文件的 Evidence Checking 開始（是／需修改）。
6. **ADR：**同意將 Repository Independence 與 Orchestrator 分成 ADR-001／002（是／需修改）。
7. **下一輪：**是否授權 Codex *僅* 製作兩份紙上 Task/Oracle 與時間估算文件（需明確另行說明是否允許 Commit/Push）。

**尚未建議拍板：**具體模型、精確 Token／金額上限、成功率門檻、是否執行 P2、正式 Trial 數量、何時做動態 Routing、是否用某 SDK。這些應以 Provider 能力、Source Manifest 及小規模工時計算為依據。

---

## 6. 交付前審閱（作者自審紀錄）

**審閱性質：**文件一致性與研究方法學自審；**不是外部同儕審查，也不是已執行的實驗驗證**。

| 檢查項目 | 結果 | 審閱意見 |
|---|---|---|
| 有遵循使用者最新的 Research Team First／Independent Orchestrator 願景 | 通過 | 目標架構與首輪研究邊界分開敘述 |
| 與 RQ-001 Draft 的 P0/P1/P2 程序一致 | 通過 | 保留 P0 自查、P1 Reviewer→Researcher 修訂、P2 執行前分流 |
| Reviewer 與 Oracle 是否分離 | 通過 | 無效 finding、反對修訂、錯誤引入與盲評均有處理 |
| 是否誤將純 Agent 數量視為唯一變因 | 通過 | 明列 Workflow Package／Context 等混淆因子 |
| 是否宣稱 Orchestrator 已有強制預算能力 | 通過 | 硬限制需 Provider capability；未知非 0；失敗閉鎖 |
| 是否明確標示 ADR 編號衝突 | 通過 | 建議拆成 ADR-001／002，未偷改原文件 |
| 是否避免將 Private 舊 Repo 內容搬入 AI Craft | 通過 | 只概括來源調查結論與風險；不複製程式／Prompt |
| 是否將 36–60 Trial 當作必做承諾 | 通過 | 明定為估算情境，實際試驗待核准 |
| 是否保留缺失值、失敗及人類工作量 | 通過 | 記錄 all attempted trials、用量來源與人為介入 |
| 是否清楚區分建議與執行授權 | 通過 | 本文件不授權模型試跑、程式開發、Commit/Push |

### 6.1 已辨識但仍待後續解決的缺口（Open Items）

- **Provider Capabilities：**現有文件未證實某 CLI／API 可以可靠執行預算保留、取消或逐次用量收集，故未在此指定供應商。
- **Rubric 精確度：**尚未提供可直接測試的兩個 Task/Oracle Fixture，所以 `critical_error`、Accept Rule 與數值門檻仍待實例化。
- **工作量可信度：**12 週計畫只是預估；真正可行性需實測文件準備、人工評分與追蹤開銷。
- **文獻驗證：**本次只以專案白皮書及 Codex 報告為設計基礎，未替白皮書候選文獻做新一輪獨立核查；不得把列出的文獻當作本專案成效證明。

**審閱結論：**本版適合作為 Human 審查五項架構方向、並決定下一輪 Codex 文件任務的 Proposal；**尚不適合作為正式實作規格或預註冊的實驗協定**。
