# BSP 組成與平台邊界

## 學習目標與前置知識

前置：能辨認 CPU、RAM、作業系統。目標：區分 BSP 板級支援的啟動、硬體描述與驅動責任。此課程將 BSP 視為平台整合工作集合，不假設所有廠商有相同封裝。

## 元件與責任

Bootloader 準備核心執行環境；Device Tree 描述硬體；Linux 驅動控制裝置；root filesystem 提供使用者空間。診斷時先辨認問題發生在哪一層，再查該層的版本與設定。這是教材的工作分類，不是通用產品規格。

## QEMU 平台限制

QEMU virt 是虛擬平台，並不對應實體開發板。用它練習軟體啟動流程，不能證明真實板子的 DDR 訓練、電源時序或 EMI 正確。車用與醫療認證不在本實驗範圍。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [linux-boot](https://raw.githubusercontent.com/torvalds/linux/v6.12/Documentation/arch/arm64/booting.rst)
- [qemu](https://raw.githubusercontent.com/qemu/qemu/v8.2.2/docs/system/arm/virt.rst)
