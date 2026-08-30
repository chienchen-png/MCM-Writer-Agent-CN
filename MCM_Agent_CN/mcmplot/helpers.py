"""mcmplot.helpers —— 绘图辅助函数：子图编号、置信带、多 Y 轴工具。"""

import matplotlib.pyplot as plt


def subpanel_label(ax, label="(a)", loc="upper right", fontsize=16, **kwargs):
    """在子图一角绘制面板编号（如 (a)、(b)）。

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        目标子图。
    label : str
        面板标签文本。
    loc : str
        位置（'upper right' / 'upper left' / ...）。
    fontsize : int
        字号（默认 16，比正文略大）。
    """
    x = 0.96 if "right" in loc else 0.04
    y = 0.96 if "upper" in loc else 0.06
    ha = "right" if "right" in loc else "left"
    va = "top" if "upper" in loc else "bottom"
    ax.text(
        x, y, label,
        transform=ax.transAxes,
        fontsize=fontsize,
        fontweight="bold",
        va=va, ha=ha,
        **kwargs,
    )
    return ax


def add_shaded_ci(ax, x, mean, ci, color="0.4", alpha=0.15, **kwargs):
    """绘制均值 ± 置信区间阴影带（科研折线图核心）。

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x : array-like
    mean : array-like
        均值曲线。
    ci : array-like
        半置信区间宽度（即 mean±ci）。
    """
    ax.fill_between(x, mean - ci, mean + ci, color=color, alpha=alpha, **kwargs)
    return ax


def add_key_line(ax, x=None, y=None, color="tomato", ls="--", lw=1.2, label=None, **kwargs):
    """添加关键事件参考线（水平或垂直）。

    Parameters
    ----------
    x : float, optional
        若提供，画垂直参考线（axvline）。
    y : float, optional
        若提供，画水平参考线（axhline）。
    """
    if x is not None:
        ax.axvline(x, color=color, linestyle=ls, linewidth=lw, label=label, **kwargs)
    if y is not None:
        ax.axhline(y, color=color, linestyle=ls, linewidth=lw, label=label, **kwargs)
    return ax


def twin_y_axes(fig, ax, colors_list, n_extra, spine_x=1.0, **kwargs):
    """创建多 Y 轴并绑定颜色（来源③ 多 y 轴架构的精简实现）。

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
        主坐标轴。
    colors_list : list
        颜色列表，长度 >= n_extra + 1。
    n_extra : int
        额外 Y 轴个数。
    spine_x : float, optional
        额外轴右边框的相对位置（>1 表示向右偏移）。
    """
    axes = [ax]
    for i in range(n_extra):
        new_ax = ax.twinx()
        # 右移边框避免重叠
        pos = new_ax.get_position()
        new_ax.set_position([pos.x0 + i * 0.0, pos.y0, pos.width * (spine_x - 1.0), pos.height])
        if i + 1 < len(colors_list):
            ax2 = new_ax
            ax2.spines["right"].set_color(colors_list[i + 1])
            ax2.tick_params(axis="y", colors=colors_list[i + 1])
            for lbl in ax2.get_yticklabels():
                lbl.set_fontsize(11)
        axes.append(new_ax)
    return axes
