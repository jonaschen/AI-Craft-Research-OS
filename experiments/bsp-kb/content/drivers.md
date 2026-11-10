# 核心設定與驅動綁定

## 學習目標與前置知識

前置：Linux 建置與裝置概念。目標：區分核心組態、裝置比對與 probe。適用 Linux v6.12；實際設定名稱需依目標驅動確認。

## 核心設定

使用 make menuconfig 選擇核心功能，保留 .config 與來源版本才能重現設定。跨架構編譯需明確指定 ARCH 與 CROSS_COMPILE。複製其他板子的組態不代表周邊一定相容。

## match 與 probe

裝置與驅動的比對規則由 bus 決定。匹配後呼叫 probe，讓驅動確認並初始化裝置。遇到周邊失效，先檢查裝置是否列舉、驅動是否建入或載入，再查 probe 的錯誤；match 成功不等於 probe 成功。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [linux-config](https://raw.githubusercontent.com/torvalds/linux/v6.12/Documentation/admin-guide/README.rst)
- [linux-driver](https://raw.githubusercontent.com/torvalds/linux/v6.12/Documentation/driver-api/driver-model/binding.rst)
