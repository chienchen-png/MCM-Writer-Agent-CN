# Python matplotlib 数据图绘制规范

## 基本要求
- 使用 `mcp_provides_tool_pylanceRunCodeSnippet` 执行代码
- 代码必须包含**完整中文注释**，说明每段逻辑
- 图表中**不出现图表名称**（标题在正文中通过"如图X-Y所示"引用）
- 所有文字标注使用**中文**
- 布局**紧凑**，减少留白，`plt.tight_layout(pad=1.0)`
- 保存到 `当前赛题/论文草稿/图表/图X-Y.png`
- DPI ≥ 300，格式 PNG
- 生成后**不调用 `plt.show()` 弹出窗口**（非交互模式下），直接保存文件

---

## 学术配色方案

| 配色方案 | 主色1 | 主色2 | 主色3 | 主色4 | 适用场景 |
|----------|-------|-------|-------|-------|---------|
| A：学术蓝-橙 | `#2B579A` | `#E87722` | `#6B8E23` | `#8B008B` | 默认通用 |
| B：暖色对比 | `#C0392B` | `#2980B9` | `#F39C12` | `#27AE60` | 对比突出 |
| C：冷色专业 | `#1A5276` | `#117864` | `#7D3C98` | `#B03A2E` | 正式场合 |

---

## 2D 图表代码模板

```python
import matplotlib.pyplot as plt
import numpy as np

# ========== 配色：学术蓝-橙（方案A） ==========
BLUE   = '#2B579A'
ORANGE = '#E87722'
GREEN  = '#6B8E23'
PURPLE = '#8B008B'

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

```python
import matplotlib.pyplot as plt
import numpy as np

# ========== 配色 ==========
BLUE   = '#2B579A'
ORANGE = '#E87722'

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
