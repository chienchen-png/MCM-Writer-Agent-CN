# Event-study 风格（事件前后动态效应）

## 图示说明

横轴"相对事件时间"（0 代表政策实施/冲击发生/处理开始），纵轴每期效应估计，每点配置信区间。保留 y=0 水平参考线 + x=0 事件虚线。若事件前估计长期偏离 0 需谨慎解释因果关系。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,9)
eff=np.array([-.02,.01,-.03,0,.02,0,.05,.11,.16,.19,.23,.21,.18,.17])
ci=.06+.01*np.abs(x)/6
plt.axhline(0,color='0.4'); plt.axvline(0,ls='--',color='tomato')
plt.errorbar(x,eff,yerr=ci,fmt='o-',capsize=3)
plt.xlabel('Time relative to event'); plt.ylabel('Estimated effect')
plt.tight_layout(); plt.show()
```

## 适用场景

经济学、公共政策、管理学、社会科学的实证研究（政策评估、因果推断、事件研究）。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A5，作者：雷霆祥脚迷恋者安和昴
