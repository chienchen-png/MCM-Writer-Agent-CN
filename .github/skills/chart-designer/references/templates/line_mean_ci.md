# 均值 + 95% CI（趋势 + 不确定性）

## 图示说明

均值曲线 + 95% 置信区间阴影带，用于展示总体趋势的同时交代结果的不确定性。建议 2-3 条主线、低饱和度配色、少量 marker，置信区间设较低透明度让线成为视觉中心。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(13)
mean=1.2+0.15*x+0.12*np.sin(x/1.7)
ci=0.12+0.02*np.sqrt(x+1)
plt.plot(x,mean,lw=2.2,marker='o')
plt.fill_between(x,mean-ci,mean+ci,alpha=.15)
plt.axvline(6,ls='--',color='tomato')
plt.xlabel('Week'); plt.ylabel('Standardized outcome')
plt.tight_layout(); plt.show()
```

## 适用场景

纵向实验、医学随访、教学干预、环境监测、经济时间序列。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A1，作者：雷霆祥脚迷恋者安和昴
