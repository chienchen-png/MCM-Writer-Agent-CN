---
name: 04-图表设计与绘制
description: 分析建模文档与运行结果，输出图表文字设计方案；或在用户指令下执行实际绘图（Python matplotlib 绘制数据图，draw.io 绘制逻辑流程图）。
trigger:
  - "配什么图"
  - "设计图表"
  - "图表方案"
  - "需要什么图"
  - "可视化方案"
  - "画图"
  - "绘制图表"
  - "生成图表"
  - "画流程图"
  - "画数据图"
  - "画3D图"
  - "画三维图"
  - "出图"
autonomous_trigger: true  # 当用户讨论图表需求时，Agent 可自动唤起设计模式
---

# 04-图表设计与绘制 SKILL

## 触发条件

### 设计模式（默认，被动触发）
当用户指令包含以下关键词，或 Agent 检测到上下文需要图表设计时，进入**设计模式**：
- "配什么图" / "设计图表"
- "图表方案" / "需要什么图"
- "可视化方案"

### 绘制模式（主动触发）
当用户指令包含以下关键词时，进入**绘制模式**，实际渲染图片：
- "画图" / "绘制图表" / "生成图表"
- "画流程图" / "画数据图"
- "画3D图" / "画三维图"
- "出图"

---

## 模式一：设计模式（DESIGN）

仅输出**文字设计方案**，不执行任何绘图代码。此模式用于大纲规划阶段和写作前的图表预案。

### 步骤 D1：读取输入
1. 读取要配图的建模文档（`当前赛题/建模思路/QX_建模思路文档.md`）。
2. 读取对应的运行结果（`当前赛题/编程计算结果/QX_运行结果.md`）。
3. 读取 `知识库/模板与规范/图标模板/图表模板与撞色配色设计.md`（配色规范）。
4. 读取 `当前赛题/论文草稿/论文大纲_草稿.md`（确认图表清单与章节上下文）。

### 步骤 D2：数据分析
从建模文档和运行结果中提取：
- 适合可视化的数据列（如时间序列、分类对比数据、收敛数据）
- 需要展示的逻辑流程（如算法步骤、决策路径）
- 需要对比的维度（如不同方案的指标对比）
- 适合 3D 展示的多变量关系

### 步骤 D3：输出文字设计方案

对每个建议的图表，输出完整文字方案（**不执行绘图代码**）：

```markdown
### 图X-Y：图表名称

| 属性 | 值 |
|------|-----|
| **图表名称** | 如"算法收敛曲线对比"（不在图中显示） |
| **图表类型** | 折线图 / 柱状图 / 热力图 / 流程图 / 箱线图 / 散点图 / 3D曲面图 / 3D散点图 |
| **维度** | 2D / 3D |
| **配色方案** | 方案A（学术蓝-橙）/ 方案B（暖色对比）/ 方案C（冷色专业） |
| **X轴** | 含义 + 单位 + 数据范围 |
| **Y轴** | 含义 + 单位 + 数据范围 |
| **Z轴**（3D） | 含义 + 单位 + 数据范围 |
| **图例** | 系列名称列表（如"方案一"、"方案二"、"方案三"） |
| **数据来源** | `编程计算结果/QX_运行结果.md` 中第X行到第Y行 |
| **引用语句** | "参见图X-Y所示的XX曲线" |
| **绘制工具** | Python(matplotlib) / draw.io |
| **设计说明** | 简述此图的核心论证目的、读者应关注的要点 |
```

### 步骤 D4：写入设计文件
将设计方案写入 `当前赛题/论文草稿/图表/图X-Y_设计方案.md`。

### 步骤 D5：更新图表清单
更新 `当前赛题/论文草稿/图表/图表设计清单.md`，标记状态为「已设计」。

---

## 模式二：绘制模式（DRAW）

当用户明确要求"画图"时，执行实际渲染。**先判断工具，再执行绘图。**

### 步骤 R1：工具决策树

```
图表类型判断：
├── 是逻辑流程/算法步骤/决策树/模型结构？
│   └── 🎯 draw.io（生成 .drawio 文件，VS Code 编辑器打开）
│
├── 是数据图表（折线/柱状/散点/热力/箱线/饼图/雷达/3D等）？
│   └── 🎯 Python matplotlib（mcp_provides_tool_pylanceRunCodeSnippet 执行）
│
└── 无法判断？
    └── 询问用户："这是逻辑流程图还是数据图？"
```

### 步骤 R2-P：Python matplotlib 数据图绘制规范

#### 基本要求
- 使用 `mcp_provides_tool_pylanceRunCodeSnippet` 执行代码
- 代码必须包含**完整中文注释**，说明每段逻辑
- 图表中**不出现图表名称**（标题在正文中通过"如图X-Y所示"引用）
- 所有文字标注使用**中文**
- 布局**紧凑**，减少留白，`plt.tight_layout(pad=1.0)`
- 保存到 `当前赛题/论文草稿/图表/图X-Y.png`
- DPI ≥ 300，格式 PNG
- 生成后**不调用 `plt.show()` 弹出窗口**（非交互模式下），直接保存文件

#### 2D 图表代码模板

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

#### 3D 图表代码模板

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
x = np.array([...])
y = np.array([...])
z = np.array([...])

# ========== 绘制 3D 曲面/散点 ==========
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85, edgecolor='none')
# 或：ax.scatter(x, y, z, c=z, cmap='viridis', s=30)

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

> **交互预览**：如果用户想先在交互窗口中旋转查看 3D 图，将 `plt.close()` 替换为 `plt.show()` 并用 `run_in_terminal` 执行（非 `mcp_provides_tool_pylanceRunCodeSnippet`）。

#### 图表类型 → matplotlib 函数速查

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

### 步骤 R2-D：draw.io 逻辑流程图绘制规范

#### 前置检查
确认 `hediet.vscode-drawio` 扩展已安装：
```powershell
code --list-extensions | Select-String "drawio"
```
若未安装 → 自动安装：`code --install-extension hediet.vscode-drawio`

#### 绘制流程

1. **读取设计方案**：从 `当前赛题/论文草稿/图表/图X-Y_设计方案.md` 获取流程图描述。
2. **生成 .drawio 文件**：根据方案中的节点和连接关系，生成标准 `.drawio` XML 文件，保存到 `当前赛题/论文草稿/图表/图X-Y.drawio`。
3. **告知用户打开**：文件生成后，提示用户在 VS Code 中点击该文件即自动用 draw.io 编辑器打开，可手动微调布局。

#### draw.io 文件模板（XML）

```xml
<mxfile host="app.diagrams.net" agent="MCM Agent">
  <diagram name="流程图" id="diagram-1">
    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- ========== 样式定义 ========== -->
        <!-- 圆角矩形（开始/结束）: rounded=1;fillColor=#DAE8FC;strokeColor=#6C8EBF; -->
        <!-- 普通矩形（处理步骤）: rounded=0;fillColor=#D5E8D4;strokeColor=#82B366; -->
        <!-- 菱形（判断）: rhombus;fillColor=#FFF2CC;strokeColor=#D6B656; -->
        <!-- 连线箭头: endArrow=classic;html=1;strokeColor=#666666; -->
        <!-- ========== 节点 ========== -->
        <mxCell id="node-1" value="开始" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="350" y="40" width="120" height="50" as="geometry"/>
        </mxCell>
        <!-- ========== 连线 ========== -->
        <mxCell id="edge-1" style="endArrow=classic;html=1;strokeColor=#666666;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="node-1" target="node-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

#### draw.io 样式速查

| 节点类型 | style 关键属性 | 配色 (fillColor/strokeColor) |
|----------|---------------|------------------------------|
| 开始/结束（圆角矩形） | `rounded=1` | `#DAE8FC` / `#6C8EBF` (浅蓝) |
| 处理步骤（矩形） | `rounded=0` | `#D5E8D4` / `#82B366` (浅绿) |
| 判断条件（菱形） | `rhombus` | `#FFF2CC` / `#D6B656` (浅黄) |
| 数据输入/输出（平行四边形） | `shape=parallelogram` | `#E1D5E7` / `#9673A6` (浅紫) |
| 子流程（双线矩形） | `rounded=0;double=1` | `#F8CECC` / `#B85450` (浅红) |
| 连线（箭头） | `endArrow=classic;html=1` | `#666666` strokeColor |

#### 节点自动布局规则
- 从上到下（TB）排列，节点间距 60-80px
- 水平居中于画布（以 827px 为页面宽度基准）
- 判断节点分叉：是→向右、否→向下（或反之）
- 同级并行步骤水平排列

### 步骤 R3：完成后输出

绘制完成后，向用户汇报：

```markdown
✅ 图表已生成：

| 图表 | 文件路径 | 绘制工具 |
|------|---------|---------|
| 图3-1 算法流程图 | `论文草稿/图表/图3-1.drawio` | draw.io → 请双击打开编辑 |
| 图3-2 收敛曲线 | `论文草稿/图表/图3-2.png` | Python(matplotlib) |
| 图3-3 3D参数曲面 | `论文草稿/图表/图3-3_3D.png` | Python(matplotlib 3D) |
```

---

## 图表类型决策树

```
数据类型判断：
├── 是算法流程/决策逻辑/模型结构？
│   └── 🎯 draw.io 流程图（.drawio 文件）
├── 是随时间变化的序列？
│   ├── 系列数 ≤ 3 → 折线图（多系列叠加）
│   └── 系列数 > 3 → 分面折线图
├── 是不同方案/算法的对比？
│   ├── 指标数量 ≤ 3 → 分组柱状图
│   ├── 指标数量 > 3 → 雷达图
│   └── 多次实验结果 → 箱线图
├── 是变量间关系？
│   ├── 2个变量 → 散点图 + 拟合线
│   ├── 3个变量 → 3D 散点图 (projection='3d')
│   └── 多个变量 → 热力图（相关性矩阵）
├── 是双参数对目标的影响？
│   └── 3D 曲面图 (plot_surface)
├── 是比例/构成？
│   ├── 类别 ≤ 5 → 饼图
│   └── 类别 > 5 → 堆叠柱状图
└── 是参数敏感性？
    └── 灵敏度曲线（折线图，多参数叠加）
```

## 图表配色速查

| 配色方案 | 主色1 | 主色2 | 主色3 | 主色4 | 适用场景 |
|----------|-------|-------|-------|-------|---------|
| A：学术蓝-橙 | `#2B579A` | `#E87722` | `#6B8E23` | `#8B008B` | 默认通用 |
| B：暖色对比 | `#C0392B` | `#2980B9` | `#F39C12` | `#27AE60` | 对比突出 |
| C：冷色专业 | `#1A5276` | `#117864` | `#7D3C98` | `#B03A2E` | 正式场合 |

## 输入规范

| 输入 | 路径 | 模式 |
|------|------|------|
| 建模文档 | `当前赛题/建模思路/QX_建模思路文档.md` | 设计 + 绘制 |
| 运行结果 | `当前赛题/编程计算结果/QX_运行结果.md` | 设计 + 绘制 |
| 配色规范 | `知识库/模板与规范/图标模板/图表模板与撞色配色设计.md` | 设计 + 绘制 |
| 论文大纲 | `当前赛题/论文草稿/论文大纲_草稿.md` | 设计 |
| 图表设计方案（已设计） | `当前赛题/论文草稿/图表/图X-Y_设计方案.md` | 绘制 |

## 输出规范

| 输出项 | 路径 | 说明 |
|--------|------|------|
| 设计方案 | `当前赛题/论文草稿/图表/图X-Y_设计方案.md` | 设计模式输出 |
| 数据图表 | `当前赛题/论文草稿/图表/图X-Y.png` | matplotlib 渲染 |
| 3D 图表 | `当前赛题/论文草稿/图表/图X-Y_3D.png` | matplotlib 3D 渲染 |
| 流程图 | `当前赛题/论文草稿/图表/图X-Y.drawio` | draw.io 源文件 |
| 图表清单 | `当前赛题/论文草稿/图表/图表设计清单.md` | 状态追踪 |

## 错误处理

- 若运行结果中无可视化数据 → 输出文字方案，标记为「待数据」。
- 若数据范围异常（如全零列）→ 提示用户确认数据正确性。
- 若无法确定图表类型 → 默认建议"分组柱状图 + 方案A配色"。
- 若 `hediet.vscode-drawio` 扩展未安装 → 自动执行 `code --install-extension hediet.vscode-drawio`。
- 若 Python matplotlib 导入失败 → 自动执行 `python -m pip install matplotlib`。
