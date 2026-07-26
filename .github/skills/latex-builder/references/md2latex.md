# Markdown → LaTeX 转换规则表

## 元素转换

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

---

## 关键转换规则

- 🔢 **公式编号**：将 `\tag{N}` 转为 `\label{eq:xxx}`，编号由 LaTeX 自动管理
- 🖼️ **图片引用**：Markdown 中的 `![...]` 图片需确保对应 PNG/PDF 文件已拷贝到 `figures/` 目录
- 📊 **表格转换**：从 Markdown 管道表格转为 LaTeX `tabular` 三线表，表头加粗
- 📚 **参考文献**：将 `[N] 作者. 标题[J]...` 格式转换为 `\bibitem{bib:N} 作者. 标题[J]...`
- ⚡ **特殊字符**：`&` → `\&`，`%` → `\%`，`_` 在数学模式外 → `\_`，`~` → `\~{}`
- 🎨 **图表 PNG 文件**：确保 `论文草稿/图表/` 中的 PNG 已同步到 `LaTeX正文/figures/` 目录

---

## 格式自检清单（16 项）

```
格式自检清单                        .cls 中对应位置
═══════════════════════════════════════════════════════
☐ 纸张 A4                         \LoadClass[a4paper,12pt]{article}
☐ 上下左右边距 25mm                \geometry{top=25mm,bottom=25mm,left=25mm,right=25mm}
☐ 行距约 1.38 倍                   \renewcommand*{\baselinestretch}{1.38}
☐ 正文宋体小四（12pt）              \setCJKfamilyfont{song}[...]{SimSun} + 12pt
☐ 一级标题黑体三号（16pt）          \ctexset section/format
☐ 二级标题黑体四号（14pt）          \ctexset subsection/format
☐ 三级标题黑体小四（12pt）          \ctexset subsubsection/format
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
