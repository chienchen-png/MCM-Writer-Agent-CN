# Python matplotlib 数据图绘制规范

> ⚠️ **统一样式基座（阶段二已建立）**：所有绘图脚本**必须**使用 `mcmplot` 包统一设置字体/配色/DPI，**不再手写 rcParams**。
> 脚本顶部统一写法：
> ```python
> from mcmplot.style import fig_style
> fig_style()   # 自动设好全局字体/字号/配色/DPI（含中文字体回退）
> ```

## 基本要求
- 使用 `mcp_provides_tool_pylanceRunCodeSnippet` 执行代码
- 脚本开头必须 `from mcmplot.style import fig_style` + `fig_style()`
- 代码必须包含**完整中文注释**，说明每段逻辑
- 图表中**不出现图表名称**（标题在正文中通过"如图X-Y所示"引用）
- 所有文字标注使用**中文**（mcmplot 已自动回退到中文字体，如微软雅黑）
- 布局**紧凑**，减少留白，`plt.tight_layout(pad=1.0)`
- 保存到 `当前赛题/论文草稿/图表/图X-Y.png`
- DPI ≥ 300，格式 PNG
- 生成后**不调用 `plt.show()` 弹出窗口**（非交互模式下），直接保存文件

---

## 学术配色方案

> ⚠️ **配色唯一来源是 `color-schemes.md`（全局统一色板）**，不再使用旧的"多套方案"。全文共用一个主色调色板，仅靠图型/线型/标记区分。

取色统一用 `mcmplot.colors`：

```python
from mcmplot.colors import get_palette  # 或 SCHEME_A / SCHEME_B / SCHEME_C
BLUE   = '\#2B579A'   # 主蓝（主序列/方案一）
ORANGE = '\#E87722'   # 警示橙（对比序列/方案二）
```

> 完整色板 + 语义约定 + 章节色板见 `references/color-schemes.md`。

---

## 2D 图表代码模板

> 脚本开头统一：`from mcmplot.style import fig_style`，颜色用 `mcmplot.colors` 取全局色板（勿手写新色值）。

```python
from mcmplot.style import fig_style
from mcmplot.colors import SCHEME_A
fig_style()   # 统一字体/字号/配色/DPI（含中文字体回退）
import matplotlib.pyplot as plt
import numpy as np

# ========== 取全局色板（方案A） ==========
BLUE   = SCHEME_A['blue']
ORANGE = SCHEME_A['orange']

# ========== 数据（从运行结果提取） ==========
x = np.array([...])       # X轴数据
y1 = np.array([...])      # 系列一
y2 = np.array([...])      # 系列二

# ========== 创建画布 ==========
fig, ax = plt.subplots(figsize=(7, 4.5))

# ========== 绘制 ==========
ax.plot(x, y1, color=BLUE, linewidth=1.8, marker='o', markersize=4, label='方案一')
ax.plot(x, y2, color=ORANGE, linewidth=1.8, marker='s', markersize=4, label='方案二')

# ========== 标注 ==========
ax.set_xlabel('迭代次数', fontsize=10)
ax.set_ylabel('目标函数值', fontsize=10)
ax.legend(fontsize=9, framealpha=0.8)
ax.grid(True, alpha=0.3, linestyle='--')

# ========== 紧凑保存 ==========
plt.tight_layout(pad=1.0)
plt.savefig(r'当前赛题/论文草稿/图表/图X-Y.png', dpi=300, bbox_inches='tight')
plt.close()
```

---

## 3D 图表代码模板

> 脚本开头统一：`from mcmplot.style import fig_style`。

```python
from mcmplot.style import fig_style
from mcmplot.colors import SCHEME_C
fig_style()
import matplotlib.pyplot as plt
import numpy as np

# ========== 取全局色板（方案C） ==========
BLUE   = SCHEME_C['deep_blue']
ORANGE = SCHEME_C['dark_red']

# ========== 创建 3D 画布 ==========
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# ========== 数据 ==========
X, Y = np.meshgrid(np.linspace(...), np.linspace(...))
Z = ...  # 计算 Z 值

# ========== 绘制 3D 曲面 ==========
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85, edgecolor='none')
# 或 3D 散点：ax.scatter(x, y, z, c=z, cmap='viridis', s=30)

# ========== 视角设定 ==========
ax.view_init(elev=25, azim=45)  # 仰角25°, 方位角45°

# ========== 标注（中文） ==========
ax.set_xlabel('参数 α', fontsize=10, labelpad=8)
ax.set_ylabel('参数 β', fontsize=10, labelpad=8)
ax.set_zlabel('目标函数值', fontsize=10, labelpad=8)

# ========== 颜色条 ==========
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='函数值')

# ========== 紧凑保存 ==========
plt.tight_layout(pad=1.0)
plt.savefig(r'当前赛题/论文草稿/图表/图X-Y_3D.png', dpi=300, bbox_inches='tight')
plt.close()
```

> **交互预览**：如果用户想先在交互窗口中旋转查看 3D 图，将 `plt.close()` 替换为 `plt.show()` 并用 `run_in_terminal` 执行。

---

## 图表类型 → matplotlib 函数速查

| 图表类型 | matplotlib 函数 | 关键参数 |
|----------|----------------|---------|
| 折线图 | `ax.plot()` | `linewidth, marker, markersize` |
| 柱状图 | `ax.bar()` / `ax.barh()` | `width, color, edgecolor` |
| 分组柱状图 | `ax.bar()` + 偏移 | 手动计算 x 偏移量 |
| 散点图 | `ax.scatter()` | `s, c, cmap, alpha` |
| 箱线图 | `ax.boxplot()` | `positions, widths` |
| 热力图 | `ax.imshow()` 或 `sns.heatmap()` | `cmap, annot` |
| 雷达图 | 极坐标 `subplot(projection='polar')` | 需手动闭合多边形 |
| 饼图 | `ax.pie()` | `colors, autopct, startangle` |
| 3D 曲面 | `ax.plot_surface()` | `cmap, alpha, edgecolor` |
| 3D 散点 | `ax.scatter()` (3D axes) | `c, cmap, s` |
| 3D 曲线 | `ax.plot()` (3D axes) | `linewidth` |
| 等高线 | `ax.contour()` / `ax.contourf()` | `levels, cmap` |
