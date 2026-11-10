# UART 日誌的無狀態診斷

## 目標與前置條件

目標是把文字中的已知錯誤標記轉成可追溯的觀察，不從少量文字宣稱硬體根因。準備 UTF-8 UART 純文字檔，先移除私有或雇主資料。工具僅讀取一個檔案，不連線裝置、不執行日誌內命令。規則基線為 Linux v6.12；其他版本可能不同。

## 操作流程

從 experiments/bsp-kb 目錄執行 `python3 -m bsp_kb diagnose-uart tests/fixtures/uart/rootfs.txt`。回傳 JSON 包含原始輸入 SHA-256、行數、明確 banner 的觀察、錯誤標記行號、來源與後續人工查核方向。範例為合成測試，並非真實開機紀錄。

找到已知標記的 status 是 signatures-found；空白、截斷或未知內容是 insufficient-evidence。成功分析的結束碼為 0，不代表開機成功；讀取、編碼或大小錯誤為 2。輸入上限 1 MiB，拒絕 NUL 或非 UTF-8 資料。

## 解讀觀察與限制

根檔案系統掛載失敗：核對 root=、映像和儲存／檔案系統支援。找不到可執行 init：查核 rootfs 的 init 路徑、架構及直譯器。panic 標記本身不提供唯一根因，應回到第一個錯誤與完整版本證據。

規則只辨認字串，引用或偽造的訊息也會匹配。未匹配不代表健康；最後出現的 banner 不代表最後成功的階段；多次開機未自動分段。root_cause 永遠是 null。工具不將日誌文字當作指令，也不輸出原始整行，避免擴散無關內容；輸入雜湊並非匿名化承諾。

## 人類練習

先自行判讀 rootfs 合成範例，列出觀察、至少兩項待查證條件及尚不能判定的事情，再和工具比較。把診斷意見與已證實事實分開。這個練習不提供真實硬體能力證據，也不自動回寫知識庫。

## 來源與審閱

下列 Linux v6.12 檔案支持訊息的來源；人工查核流程是本教材的建議，不是自動證明的根因。尚待專家獨立審閱。

- [root mount](https://raw.githubusercontent.com/torvalds/linux/v6.12/init/do_mounts.c)
- [init](https://raw.githubusercontent.com/torvalds/linux/v6.12/init/main.c)
- [panic](https://raw.githubusercontent.com/torvalds/linux/v6.12/kernel/panic.c)
