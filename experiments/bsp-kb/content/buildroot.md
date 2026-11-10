# Buildroot 映像與 QEMU 診斷

## 學習目標與前置知識

前置：Linux shell、交叉編譯概念。目標：定位 Buildroot 建置產物，區分模擬器啟動與客體開機。來源基線為 Buildroot 2024.02.1 與 QEMU 8.2.2；此版本選擇供重現，不表示安全更新建議。

## 建置輸出

Buildroot 從設定產生嵌入式系統產物；make menuconfig 後執行 make。output/images 放置可供部署的映像。記錄 defconfig、來源版本與映像雜湊，不把 output/target 當成已完成的可部署映像。

## 啟動問題分層

診斷無法開機時，保存完整命令與串列日誌。先檢查映像路徑及架構，再定位核心是否輸出，最後觀察 root filesystem 與 init 是否可用。這是本教材的診斷框架，並非特定錯誤訊息的唯一解法。

## 固定虛擬機條件

QEMU 可用 virt-8.2 固定機器模型；另記錄 QEMU 完整版本與 CPU。virt 不模擬特定實體板。固定機器模型有助於比較，但不能保證所有主機與加速方式的結果完全相同。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [buildroot](https://raw.githubusercontent.com/buildroot/buildroot/2024.02.1/docs/manual/quickstart.adoc)
- [qemu](https://raw.githubusercontent.com/qemu/qemu/v8.2.2/docs/system/arm/virt.rst)
