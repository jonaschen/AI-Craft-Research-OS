# QEMU 實驗操作指南

## 已驗證：不需客體映像的 DTB 檢查

環境：Ubuntu 提供的 QEMU 8.2.2、machine virt-8.2、cortex-a57、512 MiB RAM，並安裝 dtc。這個實驗只驗證虛擬硬體描述產生，不執行 Linux。

```sh
qemu-system-aarch64 -machine virt-8.2,dumpdtb=/tmp/bsp-virt.dtb -cpu cortex-a57 -m 512 -nographic
dtc -I dtb -O dts /tmp/bsp-virt.dtb > /tmp/bsp-virt.dts
```

驗收：QEMU 正常退出，DTB 開頭為十六進位 `d00dfeed`，dtc 能解碼，輸出包含 `arm,pl011`。dtc 可能提出 bindings／節點格式警告；解碼成功並不代表所有 binding 都已驗證。[本次證據](reports/qemu-dtb.json)。

## 未執行：U-Boot 韌體開機

固定 U-Boot v2024.10 與 QEMU 8.2.2。在獨立工作目錄準備該版 U-Boot 原始碼及其建置相依工具（包含 AArch64 GCC、make、bison、flex、OpenSSL 開發檔案），執行：

```sh
make CROSS_COMPILE=aarch64-linux-gnu- qemu_arm64_defconfig
make CROSS_COMPILE=aarch64-linux-gnu-
qemu-system-aarch64 -machine virt-8.2 -cpu cortex-a57 -nographic -bios u-boot.bin
```

驗收需保存編譯器版本、來源提交、設定與映像雜湊，以及顯示 U-Boot 版本及提示符的串列日誌。本機缺少 `aarch64-linux-gnu-gcc`，本次未建置或執行此段。它也不是完整 Linux 開機驗證。

完整 Buildroot／Linux 開機留待下一次實驗：須另固定板級 defconfig、核心與 rootfs 產物，記錄從核心到 init 的日誌，才可提升能力狀態。
