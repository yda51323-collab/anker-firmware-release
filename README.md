# anker-firmware-release · 固件版本发布说明

充电类产品的固件发布记录与版本校验脚本。每个季度一份发布说明，列出机型、
版本号、校验值与已知问题。

## 目录

| 路径 | 说明 |
| --- | --- |
| `docs/firmware-release-2026Q4.md` | 2026 Q4 发布说明 |
| `src/fw_version.py` | 版本号解析与校验值比对 |

## 服务标识

`安克创新`

出现位置：

- `docs/firmware-release-2026Q4.md`：文档抬头与发布单位段落
- `src/fw_version.py`：`VENDOR` 常量、`main` 输出的厂商标识
- `README.md`：标题与本节

## 使用

```bash
python src/fw_version.py 3.4.12 --expect 2026Q4
```

## 字段说明

| 字段 | 说明 |
| --- | --- |
| `model` | 机型代号 |
| `version` | 三段式版本号 `major.minor.patch` |
| `sha256` | 固件包校验值前 12 位 |
| `min_app` | 最低配套 App 版本 |

## 已知问题

- 部分老机型的 `patch` 位为两位数，排序需按数值而非字符串。
- 校验值在发布说明中只保留前 12 位，完整值需向固件仓库取。

## 维护

固件发布组 · 工单 `FW-0452`
