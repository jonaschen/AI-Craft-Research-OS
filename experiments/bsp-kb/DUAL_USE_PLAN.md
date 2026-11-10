# BSP 人機雙用實作計畫與協作契約

日期：2026-11-10。需求輸入為根目錄 `BSP 人機雙用知識庫建置架構.md`；延伸既有 [MVP](README.md)，不改寫 Research OS 的研究契約。架構文中的產品版本、效能數字、授權說明與案例是待查核研究主張，不作為本專案測量結果或選型證據。

## 架構理解與取捨

核心是 Git 中的單一知識來源，產生人類學習視圖和 Agent 查閱／工具視圖；每項知識有來源與版本，衍生物有雜湊綁定，知識更新要能使舊產物失效。解析與工具先採確定性實作，評測答案和一般知識分離。QEMU、主機測試與實體板認證是不同證據層級。

沿用 `entries.json` + `sources.json` + `content/*.md` 作為唯一事實來源。這是架構所提 Markdown frontmatter 主存格式的過渡實作：暫不把 metadata 複製到兩處手動維護；編譯產物自動附上 YAML frontmatter。`diataxis` 可選值為 `tutorials`、`how-to`、`reference`、`explanation`，未指定預設 explanation。四類導覽都產生，空類別明示待補；不把概念教材重新命名便宣稱已完成實作教學。

這輪不先導入向量庫、付費模型、企業多租戶服務或自動燒錄。先完成可重現的雙用輸出與無狀態診斷，再用實測缺口決定後續複雜度。來源資料範圍維持原創教材和公開來源紀錄。

## 已討論的分工

`BSP_session_B` 與 `session_BSP_A` 已透過工作階段訊息交換設計並確認共享 checkout 的檔案責任。

| 負責者 | 修改範圍 | 交付契約 |
| --- | --- | --- |
| BSP_session_B | `bsp_kb/compiler.py`、`tests/test_compiler.py`、`templates/bsp-knowledge/SKILL.md`、本計畫 | `compile_views(root, output)`、`check_views(root, output)`；唯讀來源、全新輸出目錄、可攜技能與漂移檢查 |
| session_BSP_A | UART 診斷器與測試、合成 fixtures、教材和來源登錄、CLI、README、CI | `analyze_uart(text)`；觀察與候選檢查分開；CLI 整合、回歸驗證、精確 commit/push |

CLI 對接：`compile --output PATH`、`check --output PATH`、`diagnose-uart PATH`。成功退出 0，漂移／評測未過退出 1，輸入錯誤退出 2。共用分支不互相重設檔案，不使用 `git add -A` 收入他人未完成變更。原始需求文保持原樣。

## 分階段交付與完成條件

| 階段 | 工程交付 | 驗收條件與相依 |
| --- | --- | --- |
| P1：本輪 | 四類 Markdown 導覽、llms.txt、Agent JSON/JSONL、獨立知識 SKILL、manifest；UART 無狀態診斷與合成案例 | 相同輸入跨路徑產生相同位元組；改教材／來源／模板／程式可偵測過期；無答案外洩；不覆寫既有目錄；CLI 與現有評測通過 |
| P2：工作區證據 | 平台 profile、來源與映像快照、`.config` 差異、DTB 解碼、固定映像 Linux 開機紀錄 | 配置差異可追溯；實際執行固定版本映像並達 userspace；記錄命令、工具版本、退出碼、雜湊；不把 DTB 成功當完整開機 |
| P3：精準萃取 | compile_commands 範圍清單、編譯條件／標頭依賴、可稽核 AST 關係、SVD／手冊表格試驗 | 有可用源碼與目標配置；以人工標註樣本量測欄位正確率、漏失率、跨版本污染；DTS 若含 C 前處理 include，先使用原建置管線前處理，再做 dtc，不能假定 dtc 會處理所有 include |
| P4：受控回寫 | 事實／假設／問題契約、revision 綁定檢查、待審 RCA、上游變更報告 | 來源改動使舊檢查失效；新知識由證據支持且保留審閱狀態；硬體驗證需要實際目標與相應操作授權 |
| P5：擴張與研究 | 獨立題庫、專家審閱、人類前後測、Agent 回答與成本評測；必要時 hybrid retrieval／MCP | 先有關鍵字檢索不足的實測，再比較替代方案；分開報告檢索命中、答案正確、工具成功與實體板有效性 |

原文十二週只作相依順序參考，未實測任務不承諾固定工期。沒有目標硬體或 NDA 資料時，持續推進公開、主機可驗證工作，將硬體／專家審閱列成明確缺口。

## P1 產物契約

輸出包含 `human/index.md`、四分類入口和教材、`llms.txt`、`agent/index.json`、`agent/context.jsonl`、`skills/bsp-knowledge/` 與 `manifest.json`。所有教材由登錄清單導出；未知檔案、fixtures、evaluation 與研究原文不會被遞迴收進 Agent 包。技能包本身只提供查閱流程，UART 執行器使用倉庫 CLI。

manifest 綁定原始教材、來源清單、條目清單、技能模板及編譯／分段實作的 SHA-256，並列出每個輸出摘要。沒有時間戳或主機絕對路徑干擾可重現性。`check` 重新編譯預期結果，比對 missing、changed、unexpected 與 invalid_paths；不信任待檢 manifest 內的任意路徑。這是漂移偵測，不是簽章或事實正確性認證。

編譯只寫入全新目錄，既有目錄拒絕覆寫。建置前驗證來源；遇到 I/O 中斷可能保留部分輸出，`check` 會判定不完整，請使用另一個新目錄重建。不得把部分產物當成功。編譯期間變動會拒絕完成；這不等同對其他程序提供跨程序鎖。

Markdown 本地內嵌連結只支援已登錄教材之間的連結，編譯時重寫至各視圖內的相對路徑。未登錄的本地附件會明確拒絕；完整 Markdown AST、引用式連結、Obsidian 圖譜及 HTML 網站尚未實作。公開語料清單不是 NDA 存取控制機制，不能直接用於私有多租戶隔離。

## 規範依據與驗證紀錄

2026-11-10 查閱 [Agent Skills 官方格式](https://agentskills.io/specification)：名稱與 description frontmatter、相對 references、按需載入；以及 [Diátaxis 官方說明](https://diataxis.fr/)：tutorials、how-to、reference、explanation 對應不同文件需求。使用 `skill-creator` 檢查技能的適用範圍及可攜資源，不安裝到使用者全域環境。

本輪結果由實際測試與整合報告補錄；自編 fixtures 不算獨立專家評測。後續優先補足跨平台／負樣本與人工根因對照，避免以測試數目替代覆蓋率證據。
