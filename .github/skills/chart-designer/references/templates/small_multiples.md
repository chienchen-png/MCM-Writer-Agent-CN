# Small Multiples（多指标清晰比较）

## 图示说明

指标一多别把十几条线塞进一张图。把每个指标放独立小面板，所有面板保持相同坐标尺度、相同字体、相似版式。高级感来自一致性——同一套坐标、同一套视觉语法、不同数据。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(10)
fig,axes=plt.subplots(2,3,sharex=True,sharey=True,figsize=(9,5.5))
for i,ax in enumerate(axes.flat):
    y=.45+.07*x+.10*np.sin((x+i)/2)+i*.05
    ax.plot(x,y,lw=2)
    ax.fill_between(x,y-.06,y+.06,alpha=.12)
    ax.set_title(f'Outcome {chr(65+i)}')
plt.tight_layout(); plt.show()
```

## 适用场景

多终点临床研究、多传感器监测、多个地区时间序列、不同生物指标、模型诊断结果。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A6，作者：雷霆祥脚迷恋者安和昴
