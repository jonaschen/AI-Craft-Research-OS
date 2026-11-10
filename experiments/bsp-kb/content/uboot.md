# U-Boot 在 QEMU 的角色

## 學習目標與前置知識

前置：交叉編譯與 AArch64 基本概念。目標：知道 qemu_arm64_defconfig 對應的 U-Boot 平台，以及韌體與 Linux 的不同驗收點。適用 U-Boot v2024.10。

## 建置與啟動韌體

設定 AArch64 CROSS_COMPILE 工具鏈後，以 make qemu_arm64_defconfig 再 make 建置。QEMU 使用 -bios u-boot.bin 載入韌體，使用 -cpu cortex-a57 指定 64 位元 CPU，-nographic 導向終端。看到 U-Boot 提示符只證明韌體啟動，不等於 Linux 已開機。

## 串列主控台

此虛擬平台提供 PL011 UART 與自動產生的 DTB。無輸出時，先確認 -nographic、CPU 型號及映像路徑。Ctrl-A 再按 X 可離開 QEMU；此快捷鍵不是在 Linux shell 中輸入的命令。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [uboot](https://raw.githubusercontent.com/u-boot/u-boot/v2024.10/doc/board/emulation/qemu-arm.rst)
