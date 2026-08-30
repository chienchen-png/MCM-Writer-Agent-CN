# 非线性 Dose-response（阈值 / 平台期 / S型转折）

## 图示说明

用密集 x 轴取值绘制平滑响应曲线 + 95% 置信带，并用浅色区域标出可能的 transition zone。读者一眼看到关系在哪个区间变化最快、何时进入平台期。曲线应来自拟合模型/GAM/LOESS/参数方程，不为好看而随意平滑。

## 官方代码

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,100,18)
mu=.2+1.8/(1+np.exp(-(x-48)/10))
se=.07+.05*np.abs(x-50)/50
plt.plot(x,mu,lw=2.5,marker='o')
plt.fill_between(x,mu-1.96*se,mu+1.96*se,alpha=.15)
plt.axvspan(40,60,alpha=.08)
plt.xlabel('Dose'); plt.ylabel('Normalized response')
plt.tight_layout(); plt.show()
```

## 适用场景

实验剂量、环境暴露、药理学、生态学、生物学响应数据。

## 来源

公众号「为什么别人的折线图像论文，你的像作业？」—— 来源① A3，作者：雷霆祥脚迷恋者安和昴
