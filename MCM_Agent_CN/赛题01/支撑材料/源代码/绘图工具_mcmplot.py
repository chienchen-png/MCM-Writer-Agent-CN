# -*- coding: utf-8 -*-
"""
图表绘制工具：统一调用 mcmplot 包出图
对应论文中的 6 张图（图4-1、4-2、4-4、4-5、4-6、4-7）
"""
import matplotlib.pyplot as plt
import numpy as np


def fig_style():
    """统一绘图风格（mcmplot 提供）"""
    try:
        import mcmplot
        mcmplot.fig_style()
    except Exception:
        print("mcmplot 未安装，使用 matplotlib 默认风格")


def boxplot_matrix(data, labels, title, outfile):
    """图4-1 箱线图矩阵"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(data)
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()


def group_bar(data, labels, title, outfile):
    """图4-2 分组柱状图"""
    plt.figure(figsize=(10, 6))
    x = np.arange(len(labels))
    plt.bar(x, data)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()


# 其余图（散点、折线、热力图、网络图）同理，按需补充
if __name__ == "__main__":
    pass
