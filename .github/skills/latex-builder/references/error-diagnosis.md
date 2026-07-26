# LaTeX 错误诊断与修复

## 步骤 C.1：读取错误日志

1. 读取 `当前赛题/LaTeX正文/` 下的 `.log` 文件
2. 搜索 `! ` 开头的行（LaTeX 错误标记）
3. 搜索 `Error:` 和 `Fatal error`
4. 搜索 `Warning:` 级别的警告

---

## 步骤 C.2：常见错误诊断表（11 种）

| 错误信息特征 | 原因 | 修复方法 |
|-------------|------|---------|
| `Undefined control sequence` | 使用了未定义的命令 | 检查命令名拼写，或添加对应 `\usepackage` |
| `Missing $ inserted` | 数学模式外的数学符号 | 将符号用 `$...$` 包裹 |
| `File 'xxx' not found` | 图片或依赖文件缺失 | 补全缺失文件或修改路径 |
| `Font 'xxx' not found` | 系统缺少字体 | 引导用户安装对应字体 |
| `Runaway argument` | 花括号不匹配 | 检查 `{}` 是否成对 |
| `Extra }` / `Missing }` | 花括号多余/缺失 | 逐层匹配花括号 |
| `Undefined citation` | 参考文献 `\cite` 但无对应 `\bibitem` | 补充 bibitem 或修改引用 |
| `Undefined reference` | `\ref` 引用不存在的 `\label` | 补充 label 或修改引用 |
| `Environment xxx undefined` | 环境名拼写错误 | 检查 `\begin{...}` `\end{...}` |
| `TeX capacity exceeded` | 递归调用 / 循环引用 | 检查是否有无限循环的宏 |
| `! Emergency stop` | 致命错误，编译中止 | 从上一条 error 开始排查 |

---

## 步骤 C.3：修复流程

```
读取 .log → 提取第一个 Error → 定位 .tex 出错行 → 修复 → 重新编译 → 重复直到无 Error
```

1. 从 `.log` 文件中提取所有 `Error`
2. 按行号从早到晚排序
3. **从第一个 Error 开始修复**（后面的 Error 可能是连锁反应）
4. 每次修复后重新编译验证
5. 最多迭代修复 5 次，超过则报告用户手动介入

---

## 步骤 C.4：修复后报告模板

```
🔧 LaTeX 修复报告
═══════════════════════════════════════
🔴 发现错误：N 个
✅ 已修复：M 个
🔴 需手动修复：K 个

修复详情：
✅ Line 45: Missing $ inserted → 已将 "x < 0" 改为 "$x < 0$"
✅ Line 102: Undefined control sequence \bee → 已改为 \begin
🔴 Line 178: Font 'SimKai' not found → 系统缺少楷体字体，请安装 SimKai 或替换为宋体
═══════════════════════════════════════
📄 已更新 .tex 文件，请重新编译验证。
```
