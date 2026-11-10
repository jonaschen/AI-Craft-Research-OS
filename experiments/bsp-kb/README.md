# BSP 知識庫實驗

Python 3.12、標準函式庫、離線可執行。教材以 Linux／QEMU 為主線；此工具不是完整 Research OS，也不生成答案或執行硬體操作。

## 快速開始

從倉庫根目錄執行：

```sh
cd experiments/bsp-kb
python3 -m bsp_kb validate
python3 -m bsp_kb search 'DTB 對齊' --json
python3 -m bsp_kb search 'probe' --topic drivers --limit 3
python3 -m bsp_kb build > /tmp/bsp-index.json
python3 -m bsp_kb export > /tmp/bsp-context.jsonl
python3 -m unittest discover -s tests -v
python3 -m bsp_kb evaluate
```

`--root PATH` 可放在子命令之前指定另一份語料。結束碼：成功 0、評測門檻未過 1、輸入或資料錯誤 2。所有命令先驗證資料；搜尋與匯出永遠從目前教材重建，因此不會讀到過期索引。`build` 的 JSON 包含 `schema_version: 1`；`export` 每行為一個相同格式的段落物件。

段落 ID 由條目 ID 與標題雜湊組成，編輯正文不改 ID，改標題會改 ID。搜尋結果包含 `entry_id`、`heading`、`text`、`topic`、`version`、`status`、`path`、`sources` 與 `score`。排序使用中英文 token 的 TF-IDF 類分數及 ID 決勝；分數不是信心機率。中文使用雙連字、英文使用詞彙；無同義詞或語意理解，常見詞可能造成不相關結果。

## 教材路徑

1. [BSP 組成](content/bsp.md)
2. [ARM64 啟動](content/boot.md)
3. [U-Boot](content/uboot.md)
4. [Device Tree](content/devicetree.md)
5. [核心設定與驅動](content/drivers.md)
6. [Buildroot 與診斷](content/buildroot.md)
7. [UART 無狀態診斷](content/uart-diagnostics.md)

前六課對應 [練習與評分規則](evaluation/exercises.md) 中同序號題目。答案與 `evaluation/cases.json` 不納入 `build` 或 `export`。這是匯出邊界，不是作業系統的保密隔離：使用 Agent 時只提供匯出檔案，不給它完整倉庫存取權。

## 來源與新增內容

`entries.json` 是內容清單，`sources.json` 是來源清單；CLI 實作為 v1 可執行資料契約。新增條目需填 ID、標題、主題、版本、來源 ID、查核日期、審閱狀態、檔名與授權狀態；正文用唯一的二級標題分段。每個段落繼承條目的來源集合，屬於文件級引用，尚未做到每句主張的精確對應。

來源紀錄包含公開 URL、版本標籤、作者、擷取日期、整份 raw 檔案的 SHA-256、範圍、專案授權與存取／模型傳輸／再散布範圍。固定 tag 加摘要用來偵測變動，不宣稱 tag 本身不可更改。專案授權不等於每個檔案的獨立授權審查；本倉庫不散布上游原文。原創教材僅整理已查核的技術事實並提供連結，尚待專家審閱。來源雜湊不是本地教材的雜湊。

網路查核另行執行，不影響離線測試：

```sh
python3 check_sources.py
```

不收錄雇主資料、私有案例或授權未明的全文。尚未選擇倉庫授權，這次實作不改變該狀態。更正流程：以 Issue 回報條目 ID、版本與公開證據，修改教材和評測，再執行檢查並提交；不得把 Agent 自評標為專家審核。

## 驗證範圍

[驗證報告](reports/validation.md) 包含檢索結果與 QEMU 實測邊界。[QEMU 操作指南](qemu-lab.md) 分開記錄已執行的 DTB 實驗與未執行的韌體建置。未執行完整 Linux 開機、學習者前後測、Agent 回答評分或 A/B 實驗。教材版本是重現基線，不是最新版本或生產環境建議。

## 一源雙用編譯與漂移檢查

同一份 entries.json、sources.json 與 content 編譯成人類 Markdown 視圖、llms.txt、Agent context 與可攜技能包。這是檔案產物，不啟動網站或 MCP 服務。輸出目錄必須不存在；工具拒絕覆寫既有資料。

```sh
python3 -m bsp_kb compile --output /tmp/bsp-views
python3 -m bsp_kb check --output /tmp/bsp-views
python3 -m bsp_kb diagnose-uart tests/fixtures/uart/rootfs.txt
```

`check` 重新計算預期產物，回報 missing／changed／unexpected；漂移時結束碼為 1。manifest 將內容、編譯器與產物雜湊綁定；它不是數位簽章或來源真實性的證明。四個 Diátaxis 入口標示內容缺口，不將原有概念教材冒稱完整教學課程。技能包是建置產物，不自動安裝或啟用。

UART 分析是純文字規則工具：不連接硬體、不執行日誌命令、不判定唯一根因。樣本全為合成測試，輸出只含匹配標記而不附原始整行。詳見新增教材與 `tests/fixtures/uart/README.md`。
