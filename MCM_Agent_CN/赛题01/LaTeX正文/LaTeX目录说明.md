# LaTeX 模板目录说明

> 📂 本目录包含 CUMCM 官方 LaTeX 模板（`cumcmthesis`）及你的论文源文件。
> 采用**分章节管理**结构（`2026_new_main.tex` 为入口，各章在 `chapter/`），便于独立调试与填写。

---

## 📄 核心文件

| 文件 | 中文名称 | 说明 |
|------|---------|------|
| `2026_new_main.tex` | **LaTeX 主入口** | 论文入口文件，用 `\input{chapter/...}` 引入各章。用 XeLaTeX 编译它即可生成 PDF。 |
| `cumcmthesis.cls` | **模板格式定义** | 定义封面、字号、页边距等全部格式（v2.6）。**一般不需要改动。** |
| `example.tex` | **旧版参考** | 早期单文件版入口（原 example.tex 保留作参考，实际使用 `2026_new_main.tex`）。 |
| `2026_new_main.pdf` | **渲染结果** | 编译后输出的 PDF。 |
| `使用须知.txt` | 模板说明 | 网络模板提供的使用说明（主 tex + chapter 配套）。 |

---

## 📑 章节文件（`chapter/` 目录）

| 文件 | 中文名称 | 对应论文节 |
|------|---------|-----------|
| `1_restatement.tex` | 问题重述 | 一、问题重述 |
| `2_analysis.tex` | 问题分析 | 二、问题分析 |
| `3_assumptions.tex` | 模型假设 | 三、模型假设 |
| `4_notation.tex` | 符号说明 | 四、符号说明 |
| `5_model_q1.tex` | 问题一模型 | 五、问题一模型的建立与求解 |
| `6_model_q2.tex` | 问题二模型 | 六、问题二模型的建立与求解 |
| `7_model_q3.tex` | 问题三模型 | 七、问题三模型的建立与求解 |
| `8_sensitivity.tex` | 灵敏度分析 | 八、灵敏度分析 |
| `9_evaluation.tex` | 模型评价与推广 | 九、模型评价与推广 |
| `10_ai_declaration.tex` | AI 使用声明 | 十、AI 声明（仅选一种） |
| `11_reference.tex` | 参考文献 | 十一、参考文献 |
| `A_appendix.tex` | 附录 | 附录 A |
| `B_code.tex` | 核心代码 | 附录 B（可选） |

> 📌 各章为 `\section{}` 骨架，内容由 `latex-builder` Skill 依据 `分章节/` 下的 Markdown 填充。

---

## 🖼️ 图片文件夹

| 文件夹 | 说明 |
|------|------|
| `figures/` | 存放论文图片（`.pdf` `.png` `.jpg`），通过 `\includegraphics{文件名}` 引用，**图片名禁用中文**。 |

---

## 🗑️ 辅助/临时文件

| 文件类型 | 说明 |
|---------|------|
| `*.aux` | 交叉引用辅助文件，编译时自动生成 |
| `*.log` | 编译日志，**语法报错时看这个文件找原因** |
| `*.synctex.gz` | 正反向搜索辅助文件 |
| `.gitignore` | Git 忽略规则，自动排除上述临时文件 |

---

## 📝 编译方式

```powershell
# 进入 LaTeX 目录
cd "当前赛题/LaTeX正文"
# 推荐 latexmk（自动处理多次编译）
latexmk -xelatex -interaction=nonstopmode 2026_new_main.tex
# 或直接 xelatex
xelatex -interaction=nonstopmode 2026_new_main.tex
```