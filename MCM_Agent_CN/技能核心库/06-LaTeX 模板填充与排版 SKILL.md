---
name: 06-LaTeX 模板填充与排版
description: 将分章节 Markdown 论文草稿填入 LaTeX 模板并编译为 PDF；检查模板格式是否符合 CUMCM 官方要求；诊断和修复 LaTeX 语法错误。
trigger:
  - "填充LaTeX"
  - "填入模板"
  - "检查LaTeX格式"
  - "修复LaTeX语法"
  - "编译LaTeX"
  - "编译论文"
  - "生成PDF"
  - "LaTeX报错"
  - "LaTeX错误"
  - "LaTeX检查"
---

# 06-LaTeX 模板填充与排版 SKILL

## 触发条件

当用户指令包含以下关键词时激活：
- "填充LaTeX" / "填入模板" / "填充模板"
- "检查LaTeX" / "检查模板格式" / "LaTeX格式"
- "修复LaTeX" / "LaTeX报错" / "LaTeX语法" / "编译报错"
- "编译LaTeX" / "编译论文" / "生成PDF"
- "LaTeX检查"

## 前置条件检查

执行前必须确认：
1. `当前赛题/赛题原文/格式要求.md` 已存在
2. `当前赛题/LaTeX正文/` 目录已存在（含 `.tex` 主文件和 `.cls` 类文件）
3. `当前赛题/论文草稿/分章节/` 中已有至少一个章节文件
4. Python 环境 + `diagram_utils.py` 可用（用于后续 `mermaid_to_png` 等图表转换）

若条件不满足，向用户报告缺失项并暂停。

---

## 核心指令

本 Skill 提供 **三种子模式**，根据用户具体指令自动选择：

| 用户指令 | 激活模式 | 说明 |
|----------|:----:|------|
| "填充LaTeX" / "填入模板" / "生成PDF" | 🅰 填充模式 | 将 Markdown 章节内容写入 .tex 并编译 |
| "检查LaTeX格式" / "LaTeX检查" | 🅱 检查模式 | 核对模板格式是否合规 |
| "修复LaTeX" / "LaTeX报错" / "编译报错" | 🅲 修复模式 | 读取 .log 文件 → 诊断 → 修复 |

---

### 模式 🅰：填充模式（Markdown → LaTeX → PDF）

#### 步骤 A.0：理解模板结构

在填充前，必须充分理解 LaTeX 模板的架构：

1. 读取 `当前赛题/LaTeX正文/LaTeX目录说明.md`，了解各文件的作用。
2. 读取 `当前赛题/LaTeX正文/` 下的 `.cls` 文件，理解：
   - 文档类选项（`\documentclass[...]{cumcmthesis}`）
   - 封面变量（`\tihao{}` `\baominghao{}` `\schoolname{}` `\membera{}` 等）
   - 编译方式（**强制 XeLaTeX**）
3. 读取 `当前赛题/LaTeX正文/` 下的 `.tex` 主文件，理解：
   - `\begin{document}` 前后的结构
   - `abstract` 环境的写法
   - `section` / `subsection` 的组织方式
   - `thebibliography` 环境的写法
   - `appendices` 环境的写法

#### 步骤 A.1：格式合规检查（填充前必做）

> ⚠️ **原则**：先检查，再填充。确保模板格式符合官方要求后再写入内容。

1. 读取 `当前赛题/赛题原文/格式要求.md` 获取官方基准。
2. 逐项比对 `.cls` 文件和 `.tex` 主文件中的格式设置：

```
格式自检清单                        .cls 中对应位置
═══════════════════════════════════════════════════════
☐ 纸张 A4                         \LoadClass[a4paper,12pt]{article}
☐ 上下左右边距 25mm                \geometry{top=25mm,bottom=25mm,left=25mm,right=25mm}
☐ 行距约 1.38 倍                   \renewcommand*{\baselinestretch}{1.38}
☐ 正文宋体小四（12pt）              \setCJKfamilyfont{song}[...]{SimSun} + 12pt
☐ 一级标题黑体三号（16pt）          \ctexset section/format (如未设则需补)
☐ 二级标题黑体四号（14pt）          \ctexset subsection/format (如未设则需补)
☐ 三级标题黑体小四（12pt）          \ctexset subsubsection/format (如未设则需补)
☐ 图标题宋体小四加粗                 \captionsetup[figure]{font={song,minusfour,bf}}
☐ 表标题宋体小四加粗                 \captionsetup[table]{font={song,minusfour,bf}}
☐ 无页眉                         默认无页眉即符合
☐ 页码居中                       默认符合
☐ 首行缩进 2 字符                  \setlength\parindent{2em}
☐ 编译器要求 XeLaTeX              \RequireXeTeX
☐ 封面承诺书 + 编号页              \maketitle 中生成
☐ 参考文献三线表/顺序编码          thebibliography 环境
☐ 图片搜索路径含 figures/          \graphicspath{{figures/}...}
```

3. 输出格式检查报告：

```
🔍 LaTeX 格式合规检查报告
═══════════════════════════════════════
✅ 纸张 A4
✅ 边距 25mm 四周
✅ 行距 1.38 倍
⚠️  一级标题：未显式设置 \ctexset section/format（.cls 中缺失），需补充
✅ 图表标题宋体小四加粗
✅ 编译器 XeLaTeX
...
═══════════════════════════════════════
总结：10/12 项通过，2 项需修正（已自动修复/已标注）
```

4. 若发现格式问题，优先自动修复 `.cls` 或 `.tex`，修复不了则报告用户并标注为 ⚠️。

#### 步骤 A.2：填充内容

按以下映射关系，将 `当前赛题/论文草稿/分章节/` 中的 Markdown 内容写入 `.tex` 主文件：

| Markdown 章节文件 | LaTeX 写入位置 |
|------------------|---------------|
| `01_题目及关键词.md` | ① `\title{...}` 标题；② `\keywords{...}` 关键词 |
| `02_摘要.md` | `\begin{abstract} ... \end{abstract}` 内部 |
| `03_问题重述.md` | `\section{问题重述}` |
| `04_模型假设与符号说明.md` | `\section{模型假设}` + `\section{符号说明}` |
| `05_Q1_模型建立与求解.md` | `\section{Q1 模型建立与求解}` |
| `06_Q2_模型建立与求解.md` | `\section{Q2 模型建立与求解}` |
| `07_Q3_模型建立与求解.md` | `\section{Q3 模型建立与求解}` |
| `08_灵敏度分析.md` | `\section{灵敏度分析}` |
| `09_模型评价与推广.md` | `\section{模型评价与推广}` |
| `10_参考文献.md` | `\begin{thebibliography}{99} ... \end{thebibliography}` |

> 若仅写了部分章节，只填充已完成的章节。已填充的章节保持不变。

#### 步骤 A.3：Markdown → LaTeX 转换规则

将 Markdown 内容转换为 LaTeX 语法时，严格遵守以下规则：

| 元素 | Markdown 写法 | LaTeX 转换结果 |
|------|--------------|---------------|
| 一级标题 | `# 标题` | `\section{标题}` |
| 二级标题 | `## 标题` | `\subsection{标题}` |
| 三级标题 | `### 标题` | `\subsubsection{标题}` |
| 行内公式 | `$...$` | `$...$`（保持不变） |
| 行间公式（无编号） | `$$...$$` | `\[ ... \]` |
| 行间公式（有编号） | `$$...\tag{1}$$` | `\begin{equation} ... \label{eq:...} \end{equation}` |
| 加粗 | `**文本**` | `\textbf{文本}` |
| 斜体 | `*文本*` | `\textit{文本}` |
| 无序列表 | `- 项目` | `\begin{itemize} \item ... \end{itemize}` |
| 有序列表 | `1. 项目` | `\begin{enumerate} \item ... \end{enumerate}` |
| 图片 | `![标题](path)` | `\begin{figure}[!htbp] \centering \includegraphics[width=...]{...} \caption{标题} \label{fig:...} \end{figure}` |
| 表格 | Markdown 表格 | 三线表（`\toprule` / `\midrule` / `\bottomrule`） |
| 引用 `[N]` | `[3]` | `\cite{bib:xxx}` 或 `\cite{...}` |
| 占位符 | `【占位_描述】` | `\textbf{\color{red}【待补充：描述】}` |

**关键转换规则：**

- 🔢 **公式编号**：将 `\tag{N}` 转为 `\label{eq:xxx}`，编号由 LaTeX 自动管理
- 🖼️ **图片引用**：Markdown 中的 `![...]` 图片需确保对应 PNG/PDF 文件已拷贝到 `figures/` 目录
- 📊 **表格转换**：从 Markdown 管道表格转为 LaTeX `tabular` 三线表，表头加粗
- 📚 **参考文献**：将 `[N] 作者. 标题[J]...` 格式转换为 `\bibitem{bib:N} 作者. 标题[J]...`
- ⚡ **特殊字符**：`&` → `\&`，`%` → `\%`，`_` 在数学模式外 → `\_`，`~` → `\~{}`
- 🎨 **图表 PNG 文件**：确保 `论文草稿/图表/` 中的 PNG 已同步到 `LaTeX正文/figures/` 目录

#### 步骤 A.4：编译 PDF

填充完成后，自动尝试编译：

```powershell
# 进入 LaTeX 目录
Push-Location "当前赛题/LaTeX正文/"
# 使用 latexmk（推荐，自动处理编译次数）
latexmk -xelatex -interaction=nonstopmode example.tex
# 若 latexmk 不可用，降级为：
xelatex -interaction=nonstopmode example.tex
```

编译完成后：
1. 检查是否生成了 `.pdf` 文件
2. 扫描 `.log` 文件中的 `Error` 和 `Warning`
3. 若有错误，自动切换到 **模式 🅲（修复模式）**

#### 步骤 A.5：完成报告

```
✅ LaTeX 填充完成
═══════════════════════════════════════
📄 源文件：当前赛题/LaTeX正文/example.tex
📕 PDF 文件：当前赛题/LaTeX正文/example.pdf
📊 填充章节：6/10 个章节
⚠️  编译警告：2 条（详见下方）
🔴 编译错误：0 条
═══════════════════════════════════════

警告详情（若有）：
- Line 145: Overfull \hbox (12.3pt too wide)
- Line 302: Citation 'bib:ref5' undefined (需检查参考文献 bibitem 是否存在)
```

---

### 模式 🅱：检查模式（格式合规审查）

用户说"检查LaTeX格式"时，跳过填充，只做格式检查。

#### 步骤 B.1：格式合规检查

与 A.1 节完全相同的检查流程，输出检查报告。

#### 步骤 B.2：内容完整性检查

额外检查 `.tex` 文件中的内容完整度：

```
📋 内容完整性检查
═══════════════════════════════════════
✅ 标题已设置
✅ 题号已设置（\tihao{A}）
⚠️  报名号为空（\baominghao{}）
✅ 成员信息已填写
✅ 摘要已填写
❌ 问题重述：为空（需填充）
✅ Q1 模型建立与求解：已填写（152 行）
❌ Q2 模型建立与求解：为空（需填充）
⚠️  参考文献：仅有 2 条，范文预期 5-8 条
═══════════════════════════════════════
```

---

### 模式 🅲：修复模式（语法诊断与修复）

用户说"LaTeX报错"或编译失败时激活。

#### 步骤 C.1：读取错误日志

1. 读取 `当前赛题/LaTeX正文/` 下的 `.log` 文件
2. 搜索 `! ` 开头的行（LaTeX 错误标记）
3. 搜索 `Error:` 和 `Fatal error`
4. 搜索 `Warning:` 级别的警告

#### 步骤 C.2：常见错误诊断表

| 错误信息特征 | 原因 | 修复方法 |
|-------------|------|---------|
| `Undefined control sequence` | 使用了未定义的命令 | 检查命令名拼写，或添加对应 `\usepackage` |
| `Missing $ inserted` | 数学模式外的数学符号 | 将符号用 `$...$` 包裹 |
| `File 'xxx' not found` | 图片或依赖文件缺失 | 补全缺失文件或修改路径 |
| `Font 'xxx' not found` | 系统缺少字体 | 引导用户安装对应字体 |
| `Runaway argument` | 花括号不匹配 | 检查 `{}` 是否成对 |
| `Extra }` / `Missing }` | 花括号多余/缺失 | 逐层匹配花括号 |
| `Undefined citation` | 参考文献 \cite 但无对应 \bibitem | 补充 bibitem 或修改引用 |
| `Undefined reference` | \ref 引用不存在的 \label | 补充 label 或修改引用 |
| `Environment xxx undefined` | 环境名拼写错误 | 检查 `\begin{...}` `\end{...}` |
| `TeX capacity exceeded` | 递归调用 / 循环引用 | 检查是否有无限循环的宏 |
| `! Emergency stop` | 致命错误，编译中止 | 从上一条 error 开始排查 |

#### 步骤 C.3：修复流程

```
读取 .log → 提取第一个 Error → 定位 .tex 出错行 → 修复 → 重新编译 → 重复直到无 Error
```

1. 从 `.log` 文件中提取所有 `Error`
2. 按行号从早到晚排序
3. **从第一个 Error 开始修复**（后面的 Error 可能是连锁反应）
4. 每次修复后重新编译验证
5. 最多迭代修复 5 次，超过则报告用户手动介入

#### 步骤 C.4：修复后报告

```
🔧 LaTeX 修复报告
═══════════════════════════════════════
🔴 发现错误：3 个
✅ 已修复：2 个
🔴 需手动修复：1 个

修复详情：
✅ Line 45: Missing $ inserted → 已将 "x < 0" 改为 "$x < 0$"
✅ Line 102: Undefined control sequence \bee → 已改为 \begin
🔴 Line 178: Font 'SimKai' not found → 你的系统缺少楷体字体，请安装 SimKai 或替换为宋体
═══════════════════════════════════════
📄 已更新 .tex 文件，请重新编译验证。
```

---

## 输出文件规范

| 模式 | 输出文件 | 位置 |
|------|---------|------|
| 🅰 填充 | `example.tex`（更新） | `当前赛题/LaTeX正文/` |
| 🅰 填充 | `example.pdf`（生成） | `当前赛题/LaTeX正文/` |
| 🅱 检查 | 格式检查报告（聊天框输出） | — |
| 🅲 修复 | `example.tex`（修复后） | `当前赛题/LaTeX正文/` |

---

## 关键原则

1. **先检查后填充**：永远在格式合规后再写入内容，避免格式问题被内容覆盖。
2. **保留原模板**：填充时只修改 `.tex` 主文件，不动 `.cls` 类文件（除非格式检查发现缺陷）。
3. **增量填充**：只填充已完成的章节，不清空已有内容。
4. **图片同步**：填充前检查 `论文草稿/图表/` 中的 PNG 是否已在 `LaTeX正文/figures/` 中。
5. **公式保持 LaTeX**：Markdown 中的公式已经是 LaTeX 语法，转换时保持不动。
6. **编译验证**：每次填充后必须编译验证，编译失败自动进入修复模式。
7. **日志更新**：完成后在 `当前赛题/进度日志.md` 追加记录。

---

## 禁止行为

- 不得修改 `.cls` 类文件的核心结构（除非格式检查发现与官方要求不一致）
- 不得使用 pdfLaTeX 编译（必须 XeLaTeX）
- 不得编造数据填充（所有数字必须来自编程计算结果）
- 不得删除 `.tex` 中已有的封面变量设置（`\tihao{}` 等）
- 不得在未检查格式合规的情况下直接填充内容
