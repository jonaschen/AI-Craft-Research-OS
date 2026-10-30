# AI Craft Research State & Discipline

- **建議目標路徑：** `docs/RESEARCH_STATE.md`
- **版本：** v0.1（提案／待 Human Research Director 審閱）
- **整理日期：** 2026-10-31
- **用途：** 研究狀態入口與團隊工作記憶；不是實驗證據，也不取代正式 ADR、研究報告或原始來源。

## 1. 核心研究目標

從真實問題出發，透過可追溯證據建立 AI 系統的能力邊界、最小必要架構與成本評估；隨模型進步持續重新驗證，而不預設 Multi-Agent、KB 或複雜 Harness 必然更好。

**研究循環：** Problem → Evidence → Capability → Architecture → Evaluation → Evolution。

## 2. 研究紀律（Working Principles）

1. **Human-directed：** 人類負責研究問題、風險邊界、資源政策及最終核准；AI 的分析與建議不是授權。
2. **Evidence-driven：** 區分原始來源、可重現觀察、合理推論、研究假說與未知。負面結果與失敗紀錄必須保留。
3. **Constructive Challenge：** 每次重要架構或研究決策，主動找出 **1–3 個有實質意義的修正／反證點**；不為挑錯而挑錯。每點說明原始假設、失效條件、修正方案與最小驗證方法。
4. **Minimal Sufficient Architecture：** 增加 Agent、KB、索引或控制層之前，先證明現有較簡單方案不能達到品質／成本門檻；同時評估 Scale Out 與 Scale In。
5. **Independent Oracle：** 不讓 Agent 自評取代正式驗收；區分檢索成功、工作完成和引用正確。
6. **Honest Boundaries：** 能力標為 Demonstrated、Assisted、Target、Out of Scope/Blocked 或 Unknown；必須附適用條件與證據，不能把未測等同於不能。
7. **Cost Includes Human Effort：** 評估總 Token／金額、延遲、重試、維護與人類審閱，而非只計模型呼叫費用。
8. **Sustainable Pace：** 研究與理解計入工時；疲憊時可降載。避免文件生產速度超越人類審閱能力。
9. **Source and Employer Boundary：** 研究可分析合法公開的 Linux Kernel／BSP／半導體一般技術問題，但不得使用、複製或揭露雇主非公開資訊或工作成果；正式修改現有 ADR-001 範圍前，相關研究輸入仍依已核准的政策處理。

## 3. 研究主線與狀態

| 研究 | 研究問題 | 目前狀態 | 下一步 |
|---|---|---|---|
| Research 01 — KB Problem Landscape | AI 在哪些情境下真正需要外部知識？ | 有兩份初步報告；案例、數據及「KB 必要」判斷尚須來源查核 | 完善案例分類與證據品質標記 |
| Research 02 — Model Capability Evolution | 2023–2026 模型演進，尤其 2026 H1/H2，如何改變外部知識需求？ | 已定義研究委託與比較方向；尚未在本文件確認獨立研究結論 | 取得可查證研究結果，拆分 Model-only、當次 Context、工具檢索、持久 KB |
| Research 03 — AI Kernel Team | 在約一名工程師的總預算內，AI 能可靠承擔哪些公開 Linux Kernel 工作？ | 研究願景及能力分類方向已建立；未有完整能力實測 | 先做 Kernel Work Taxonomy／Capability Boundary Specification，並承接 Research 02 |
| Research OS — RQ-001 | 選擇性 Reviewer 是否改善研究品質與資源效益？ | Phase 0；核心 ADR 方向經 Human Review 接受；尚未批准 Runtime 或實驗 | 驗證 Task A/B Source Hash、Oracle Isolation、Scoring Boundary |

## 4. 已確認的方向（Direction Accepted ≠ Implemented）

- AI Craft Research OS 為獨立研究專案；舊 `agent-skill-automation` 不作為程式碼／Prompt／資料來源。
- **ADR-001 核心方向：** 獨立性、來源追溯與非公開雇主資料隔離。
- **ADR-002 核心方向：** 確定性 Orchestrator 掌管權限、派工、狀態、預算及停止；Researcher／Reviewer 做語意工作；獨立 Oracle 判定結果。
- Research Team 既是研究工具，也是研究對象。Role、Agent Instance、Session、Model 不混同。
- RQ-001 的 Adaptive 暫限「執行前固定政策選擇是否加入 Reviewer」；不代表長期架構的限制。

## 5. 未決事項與證據缺口

- Task A/B：固定 CPython 來源及切片的 SHA-256、行號與證據支持程度尚待獨立重驗。
- Oracle：Agent-visible Input Bundle 與 Oracle-only 答案需實際隔離；評分邊界案例尚待紙上驗證。
- Runtime：Retry／Resume／Cancellation、Provider 能力、預算上限可執行性尚未驗證。
- Research 02：H1/H2 模型比較必須先查核發布日期、版本、相同任務與可比性；不得比較異質 Benchmark 後宣稱模型進步幅度。
- Research 03：未有完整 Kernel 任務覆蓋率、人工負擔及總成本實測；不得宣稱能取代整支 Kernel Team。
- ADR-001：公開 Linux Kernel 與一般 BSP 技術研究的範圍修訂仍需正式審閱，不因討論自動生效。

## 6. 下一次研究工作（最多一項主題）

**預設優先：** 若 Research OS Phase 0 持續推進，完成 Task A/B 的 Source Integrity → Oracle Isolation → Scoring Boundary 人工檢查，產出一份簡短 Review Record，不啟動實作。

**可切換優先：** 若當前以 KB 系列為主，先審閱 Research 02 的模型比較證據與知識需求分類，不同時展開第三題實驗。

## 7. 維護方法

- 每次重要 Human Review 後，更新「已確認方向」「未決事項」「下一步」，附上正式來源文件路徑或連結。
- 每週或每個研究時段結束時，最多更新 5–10 分鐘；沒有變化就不更新。
- 正式結論放 ADR 或研究報告；這份文件只記決策狀態與索引。用 Git diff 保留變更歷史。
- 如果文件互相衝突，以明確核准且較新的正式決策文件為準；不要由 Agent 默默改寫歷史。

## 8. Source Index（請在 Repo 內核對實際路徑）

- `docs/architecture/Research_Team_Architecture_v0.1.md`
- `docs/decisions/ADR-001_Repository_Independence_Draft.md`
- `docs/decisions/ADR-002_Independent_Orchestrator_Draft.md`
- `docs/research/Research_Question_001_Draft.md`
- `docs/research/Task_Oracle_Examples_v0.1.md`
- `docs/reviews/Phase_0_Consolidation_Review.md`
- `docs/decisions/Human_Review_Decision_2026-10-25.md`（請確認已存入 Repository）
- Research 01 兩份報告（請補 Git/Library 實際位置）
- Research 02 正式研究成果（待取得後補入）

> **狀態說明：** 本文件為 2026-10-31 的研究脈絡草案，尚未自動同步至 GitHub，也不代表最新遠端 Git 狀態已獲檢查。
