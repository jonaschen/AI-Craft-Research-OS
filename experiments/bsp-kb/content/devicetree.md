# Device Tree 硬體描述

## 學習目標與前置知識

前置：記憶體映射與裝置概念。目標：理解 DTS 原始描述與 DTB 二進位表示，以及 bindings 對屬性的約束。適用 Linux v6.12 的裝置樹使用模型。

## 節點與 bindings

Device Tree 以節點與屬性描述硬體，讓核心不必寫死所有板級資訊。bindings 定義特定裝置屬性的含義。compatible 用於識別相容硬體；新增節點前應先查對應 binding，而不是任意發明屬性。

## 硬體描述不等於驅動

DTB 的存在不保證周邊已能使用。排查時分別確認描述是否正確、驅動是否提供，以及裝置是否成功初始化。修改裝置樹不能替代缺少的驅動實作。

## 來源與審閱

本教材為原創說明，已對照下列公開來源，尚未經 BSP 專家獨立審閱。

- [linux-dt](https://raw.githubusercontent.com/torvalds/linux/v6.12/Documentation/devicetree/usage-model.rst)
