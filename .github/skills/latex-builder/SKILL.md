---
name: latex-builder
description: '三模式：A-填充（MD章节→LaTeX模板→XeLaTeX编译→PDF）+ B-检查（格式合规16项审查+内容完整性检查）+ C-修复（读取.log诊断11种错误自动修复）。Use when: 填充LaTeX, 生成PDF, 检查LaTeX格式, 修复LaTeX语法, 编译论文, LaTeX报错.'
argument-hint: '填充LaTeX / 生成PDF / 修复LaTeX语法'
---

# LaTeX 模板填充与排版

## When to Use
- 填充LaTeX / 填入模板 / 填充模板
- 生成PDF / 编译LaTeX / 编译论文
- 检查LaTeX格式 / LaTeX检查
- 修复LaTeX语法 / LaTeX报错 / LaTeX错误 / 编译报错

## 前置条件检查

执行前必须确认：
1. `当前赛题/赛题原文/格式要求.md` 已存在
2. `当前赛题/LaTeX正文/` 目录已存在（含 `.tex` 主文件和 `.cls` 类文件）
3. `当前赛题/论文草稿/分章节/` 中已有至少一个章节文件

若条件不满足，向用户报告缺失项并暂停。

---

## 核心指令

本 Skill 提供 **三种子模式**：

| 用户指令 | 激活模式 | 说明 |
|----------|:----:|------|
| "填充LaTeX" / "填入模板" / "生成PDF" | 🅰 填充模式 | 将 MD 章节内容写入 .tex 并编译 |
| "检查LaTeX格式" / "LaTeX检查" | 🅱 检查模式 | 核对模板格式是否合规 |
| "修复LaTeX" / "LaTeX报错" / "编译报错" | 🅲 修复模式 | 读取 .log → 诊断 → 修复 |

---

### 模式 🅰：填充模式（Markdown → LaTeX → PDF）

#### 步骤 A.0：理解模板结构

1. 读取 `当前赛题/LaTeX正文/LaTeX目录说明.md`，了解各文件的作用。
2. 读取 `.cls` 文件，理解文档类选项、封面变量、编译方式（**强制 XeLaTeX**）。
3. 读取 `.tex` 主文件，理解 `\begin{document}` 前后结构、abstract/section/bibliography/appendices 环境写法。

#### 步骤 A.1：格式合规检查（填充前必做）

> ⚠️ **原则**：先检查，再填充。

格式自检清单（16 项）：纸张 A4、边距 25mm、行距 1.38 倍、正文宋体 12pt、一级标题黑体 16pt、二级标题黑体 14pt、三级标题黑体 12pt、图标题宋体小四加粗、表标题宋体小四加粗、无页眉、页码居中、首行缩进 2 字符、XeLaTeX 编译器、封面承诺书+编号页、参考文献顺序编码、图片搜索路径含 figures/。

逐项比对 `.cls` 和 `.tex` 中的设置，发现问题优先自动修复，修复不了则报告用户并标注 ⚠️。

#### 步骤 A.2：填充内容

按以下映射将 Markdown 章节写入 `.tex`：

| Markdown 章节文件 | LaTeX 写入位置 |
|------------------|---------------|
| `00_摘要.md` | `\begin{abstract} ... \end{abstract}` + `\keywords{...}` |
| `01_问题重述.md` | `\section{问题重述}` |
| `02_模型假设与符号说明.md` | `\section{模型假设}` + `\section{符号说明}` |
| `03_Q1_模型建立与求解.md` ～ `05_Q3_模型建立与求解.md` | 对应 `\section{QX ...}` |
| `06_灵敏度分析.md` | `\section{灵敏度分析}` |
| `07_模型评价与推广.md` | `\section{模型评价与推广}` |
| `08_参考文献.md` | `\begin{thebibliography}{99} ... \end{thebibliography}` |

#### 步骤 A.3：Markdown → LaTeX 转换规则

详见 [md2latex.md](./references/md2latex.md)。

关键转换：`#` → `\section{}`，`$$` → `\[ \]`，`$$...\tag{1}$$` → `\begin{equation}...\end{equation}`，Markdown 表格 → 三线表（`\toprule/\midrule/\bottomrule`），`[N]` 引用 → `\cite{}`，图片 → `\begin{figure}...\includegraphics...\end{figure}`。

#### 步骤 A.4：编译 PDF

```powershell
Push-Location "当前赛题/LaTeX正文/"
latexmk -xelatex -interaction=nonstopmode example.tex
# 若 latexmk 不可用：
xelatex -interaction=nonstopmode example.tex
```

编译后检查 `.pdf` 是否生成，扫描 `.log` 中的 Error/Warning。若有错误 → 自动切换 🅲 修复模式。

#### 步骤 A.5：完成报告

```
✅ LaTeX 填充完成
📄 源文件：当前赛题/LaTeX正文/example.tex
📕 PDF 文件：当前赛题/LaTeX正文/example.pdf
📊 填充章节：X/10 个章节
⚠️  编译警告：N 条  |  🔴 编译错误：0 条
```

---

### 模式 🅱：检查模式（格式合规审查）

与 A.1 相同的检查流程 + 内容完整性检查（标题/题号/报名号/成员/摘要/各章节/参考文献填写状态）。

---

### 模式 🅲：修复模式（语法诊断与修复）

详见 [error-diagnosis.md](./references/error-diagnosis.md)，含 11 种常见 LaTeX 错误诊断表。

修复流程：
```
读取 .log → 提取第一个 Error → 定位 .tex 出错行 → 修复 → 重新编译 → 重复直到无 Error
```
最多迭代修复 5 次，超过则报告用户手动介入。

---

## 关键原则

1. **先检查后填充**：永远在格式合规后再写入内容。
2. **保留原模板**：填充时只修改 `.tex` 主文件，不动 `.cls` 类文件（除非格式检查发现缺陷）。
3. **增量填充**：只填充已完成的章节，不清空已有内容。
4. **图片同步**：填充前检查 `论文草稿/图表/` 中的 PNG 是否已在 `LaTeX正文/figures/` 中。
5. **编译验证**：每次填充后必须编译验证，编译失败自动进入修复模式。

## 禁止行为

- 不得修改 `.cls` 类文件的核心结构（除非格式检查发现与官方要求不一致）
- 不得使用 pdfLaTeX 编译（必须 XeLaTeX）
- 不得编造数据填充（所有数字必须来自编程计算结果）
- 不得删除 `.tex` 中已有的封面变量设置
- 不得在未检查格式合规的情况下直接填充内容
