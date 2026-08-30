# 顶刊 style 全局 rcParams

## 图示说明

顶级期刊（Nature/TPAMI/CVPR 等）论文图的统一视觉基调：白背景、少量颜色、细线条、统一字体、统一坐标轴风格，通过留白自然分隔模块。信息可以复杂，但视觉一定要简单。

4 大高级感来源：① 一张图只讲一条完整故事线（a/b/c 分区）；② 同一种颜色贯穿整张图（蓝-白-橙连续配色）；③ "数据图 + 示意图"组合；④ 高级感来自简洁。

公式：**好 Figure = 清晰的故事线 + 统一的视觉编码 + 数据结果 + 机制解释 + 足够的留白**

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
rng = np.random.default_rng(7)
plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 9,
    "axes.linewidth": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
})
```

## 适用场景

作为全套图的全局 rcParams 基调，或配合 `LinearSegmentedColormap` 自定义连续配色 + `inset_axes` 局部放大。

## 来源

公众号「顶刊科研图为什么"一眼就高级"？这张图，代码来了！」—— 来源② B，作者：万能的ccy
