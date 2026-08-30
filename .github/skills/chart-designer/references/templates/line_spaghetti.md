# Spaghetti Plot（总体 + 个体差异）

## 图示说明

把每个样本/受试者的轨迹用浅色细线画出，再在顶层叠加一条粗的组均值线。同时表达"总体趋势"和"个体异质性"。个体轨迹需降低透明度、线宽明显小于均值线，避免图面变一团线。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(1)
x=np.arange(9)
ys=[]
for i in range(28):
    y=.5+.08*x+rng.normal(0,.16)+rng.normal(0,.07,len(x)).cumsum()
    ys.append(y); plt.plot(x,y,alpha=.12,lw=.8)
mean=np.vstack(ys).mean(0)
plt.plot(x,mean,lw=3,marker='o',label='Group mean')
plt.legend(frameon=False); plt.tight_layout(); plt.show()
```

## 适用场景

医学随访、成长曲线、训练效果、重复测量、面板数据的探索性展示。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A2，作者：雷霆祥脚迷恋者安和昴
