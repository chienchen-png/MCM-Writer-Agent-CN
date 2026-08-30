# 多模型学习曲线（模型 + 样本量）

## 图示说明

横轴放训练样本量，纵轴放交叉验证指标，不同模型用不同 marker/颜色。样本量跨度很大时用 log2 横轴避免"大样本点挤在右侧"。配色控制在 3-5 组、marker 形状保持一致。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.array([100,200,400,800,1600,3200])
y1=.64+.24*(1-np.exp(-x/700))
y2=.60+.28*(1-np.exp(-x/1000))
plt.plot(x,y1,'o-',label='Model A')
plt.plot(x,y2,'s-',label='Model B')
plt.xscale('log',base=2)
plt.ylabel('Cross-validated AUC'); plt.xlabel('Training samples')
plt.legend(frameon=False); plt.tight_layout(); plt.show()
```

## 适用场景

机器学习/模型比较，判断模型是否过拟合、训练数据是否充足。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A4，作者：雷霆祥脚迷恋者安和昴
