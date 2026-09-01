# MinerU PDF 转 Markdown 完整操作指南

## 前置条件

- MinerU 已安装：`mineru` 命令可用（需先激活其 venv，如 `F:\MinerU\venv\Scripts\activate`）
- 模型已下载
- 若不可用，引导用户完成总控 Agent 1.6/1.7 节配置

---

## 步骤 A：确认输入与目标赛题类型

1. 确认用户要转换的 PDF 文件路径。
2. 向用户确认该论文的赛题类型（A / B / C），用于确定输出目录。
   - 若用户未指定，根据论文内容或文件名推断（如包含"A题"、"优化"等关键词 → A题）。
   - 若无法判断赛题类型（可能是非数模论文），提醒用户本模块仅用于往届数模竞赛论文，并终止。

---

## 步骤 B：执行 MinerU 识别

### B.1 确定识别模式

```powershell
nvidia-smi 2>&1
```

- **若 GPU 可用（8GB+ 显存）**：使用 `hybrid-engine` 后端，最高精度 + 图片分析。
- **若仅 CPU**：使用 `pipeline` 后端，公式 + 表格识别（不含图片内容分析）。

### B.2 构建并执行命令

**模式一：CPU / 低显存（默认）**

```powershell
mineru `
  -p "<PDF绝对路径>" `
  -o "<临时输出目录>" `
  -b pipeline `
  -l ch `
  -m auto
```

**模式二：NVIDIA GPU 8GB+ 显存（高精度）**

```powershell
mineru `
  -p "<PDF绝对路径>" `
  -o "<临时输出目录>" `
  -b hybrid-engine `
  -l ch `
  --effort high
```

**参数说明**：

| 参数 | 含义 | 取值 |
|------|------|------|
| `-p` | 输入 PDF 路径 | 绝对路径 |
| `-o` | 输出目录 | 临时目录，后续会整理 |
| `-b` | 识别后端 | `pipeline`（CPU）/ `hybrid-engine`（GPU） |
| `-l` | 文档语言 | `ch`（中文）/ `en`（英文） |
| `-m` | 模型模式 | `auto`（自动选择最佳模型） |
| `--effort` | 精度等级 | `high`（仅 hybrid-engine 支持） |

### B.3 执行自检

首次调用 MinerU 时，先在终端执行一次轻量测试：

```powershell
if (Get-Command mineru -ErrorAction SilentlyContinue) {
    Write-Host "✅ MinerU 已安装"
    mineru --version 2>&1
} elseif (Test-Path "F:\MinerU\venv\Scripts\mineru.exe") {
    Write-Host "✅ MinerU 已安装（绝对路径）"
    & "F:\MinerU\venv\Scripts\mineru.exe" --version 2>&1
} else {
    Write-Host "⚠️ MinerU 未找到，请参考总控 Agent 1.7 节配置"
}
```

---

## 步骤 C：整理输出文件

MinerU 输出目录中会包含多个中间文件，**仅保留最终 Markdown 文件**。

1. 识别 MinerU 输出目录中生成的最终 `.md` 文件（通常位于 `<输出目录>/<PDF文件名>/<PDF文件名>.md` 或类似结构）。
2. 将该 `.md` 文件复制到目标路径：`MCM_Agent_CN/知识库/文献库/范文存档/{A,B,C}题/<论文名称>.md`
3. 删除 MinerU 输出的临时目录（包括 images、tables 等中间文件）。
4. 若 Markdown 中引用了本地图片，将必要的图片复制到范文存档对应目录下。

**文件命名规范**：
```
<年份>_<赛事>_<赛题类型>_<获奖等级>.md

示例：
2023_国赛_A题_国一.md
2024_美赛_B题_F奖.md
2025_校赛_C题_一等奖.md
```

---

## 步骤 D：输出确认报告

```
📄 PDF 识别完成
═══════════════════════════════════════
输入文件：  xxx.pdf
识别模式：  pipeline / hybrid-engine
输出路径：  MCM_Agent_CN/知识库/文献库/范文存档/X题/xxx.md
识别功能：  ✅ 公式(LaTeX)  ✅ 表格(HTML)  ✅ 图片分析(GPU时)
处理耗时：  XX 秒
═══════════════════════════════════════
💡 提示：可执行"学习范文"将新文件纳入索引。
```

---

## 步骤 E：错误处理

| 错误场景 | 处理方式 |
|----------|----------|
| MinerU 未安装 | 输出 1.6 节配置引导 |
| PDF 文件不存在 | 提示用户确认文件路径 |
| 识别超时/失败 | 先尝试降级为 `pipeline` 模式重试（若原为 hybrid-engine） |
| 输出目录无 .md 文件 | 报告 MinerU 输出结构异常，引导用户检查 |
| 中文 OCR 乱码 | 确认 `-l ch` 参数，检查 PDF 是否为扫描件 |
