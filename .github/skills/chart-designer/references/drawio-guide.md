# draw.io 逻辑流程图绘制规范

## 前置检查
确认 `hediet.vscode-drawio` 扩展已安装：
```powershell
code --list-extensions | Select-String "drawio"
```
若未安装 → 自动安装：`code --install-extension hediet.vscode-drawio`

---

## 绘制流程

1. **读取设计方案**：从 `当前赛题/论文草稿/图表/图X-Y_设计方案.md` 获取流程图描述。
2. **生成 .drawio 文件**：根据方案中的节点和连接关系，生成标准 `.drawio` XML 文件，保存到 `当前赛题/论文草稿/图表/图X-Y.drawio`。
3. **告知用户打开**：文件生成后，提示用户在 VS Code 中点击该文件即自动用 draw.io 编辑器打开，可手动微调布局。

---

## draw.io 文件模板（XML）

```xml
<mxfile host="app.diagrams.net" agent="MCM Agent">
  <diagram name="流程图" id="diagram-1">
    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
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

---

## draw.io 样式速查

| 节点类型 | style 关键属性 | 配色 (fillColor/strokeColor) |
|----------|---------------|------------------------------|
| 开始/结束（圆角矩形） | `rounded=1` | `#DAE8FC` / `#6C8EBF` (浅蓝) |
| 处理步骤（矩形） | `rounded=0` | `#D5E8D4` / `#82B366` (浅绿) |
| 判断条件（菱形） | `rhombus` | `#FFF2CC` / `#D6B656` (浅黄) |
| 数据输入/输出（平行四边形） | `shape=parallelogram` | `#E1D5E7` / `#9673A6` (浅紫) |
| 子流程（双线矩形） | `rounded=0;double=1` | `#F8CECC` / `#B85450` (浅红) |
| 连线（箭头） | `endArrow=classic;html=1` | `#666666` strokeColor |

---

## 节点自动布局规则
- 从上到下（TB）排列，节点间距 60-80px
- 水平居中于画布（以 827px 为页面宽度基准）
- 判断节点分叉：是→向右、否→向下（或反之）
- 同级并行步骤水平排列
