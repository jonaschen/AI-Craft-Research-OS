# AArch64 Linux 啟動契約

## 學習目標與前置知識

前置：BSP 組成、二進位映像概念。目標：理解 AArch64 開機時 Bootloader 與 Linux kernel 的交接條件。適用 Linux v6.12 ARM64 非 EFI 直接進入核心的路徑。

## 核心交接

Bootloader 必須準備 RAM、DTB 與核心映像，再進入核心。x0 放置 DTB 實體位址；x1、x2、x3 保留為零。DTB 要 8-byte 對齊且不超過 2 MiB。這些規則不能直接套用到其他架構。

## Image 與解壓縮

AArch64 的 Image.gz 需要由進入核心前的軟體解壓縮；也可直接載入未壓縮 Image。查核映像格式、載入位置與 CPU 狀態，再推論沒有輸出的原因。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [linux-boot](https://raw.githubusercontent.com/torvalds/linux/v6.12/Documentation/arch/arm64/booting.rst)
