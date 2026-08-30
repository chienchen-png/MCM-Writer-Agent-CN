"""mcmplot.style —— 统一样式基座：中文字体回退探测 + fig_style() 全局设置。

提供两套能力：
1. fig_style()：设置统一的 rcParams（字体、字号、线宽、刻度方向、DPI）。
2. 中文字体逐个回退探测，根治"Noto Sans CJK SC not found"之类的警告。
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

# 中文字体优先级（按顺序探测，取第一个找到的）
# 注意：Windows 常用中文字体优先；"微软雅黑"是 VS Code 中文环境最常见的。
_CJK_CANDIDATES = [
    "Microsoft YaHei",   # 微软雅黑
    "SimHei",            # 黑体
    "SimSun",            # 宋体
    "KaiTi",             # 楷体
]

# 英文/数字字体候选
_SANS_CANDIDATES = [
    "Arial",
    "DejaVu Sans",
    "Helvetica Neue",
]


def _first_available(candidates):
    """返回第一个系统可用的字体族名；若无则返回 None。"""
    from matplotlib import font_manager

    available = set(f.name for f in font_manager.fontManager.ttflist)
    for name in candidates:
        if name in available:
            return name
    return None


def setup_fonts():
    """探测中文字体并设置 rcParams 的字体族，返回实际选用的字体名。"""
    cjk = _first_available(_CJK_CANDIDATES)
    latin = _first_available(_SANS_CANDIDATES)
    if cjk:
        mpl.rcParams["font.family"] = "sans-serif"
        mpl.rcParams["font.sans-serif"] = [cjk] + (["DejaVu Sans"] if latin else [])
    elif latin:
        mpl.rcParams["font.family"] = latin
    # 若无任何匹配，交给 matplotlib 默认（可能中文方块，但不会崩溃）
    mpl.rcParams["axes.unicode_minus"] = False  # 修复负号显示为方块
    return cjk


def fig_style(fontsize=10.5, linewidth=0.9, dpi=300, **kwargs):
    """设置全局绘图风格。

    Parameters
    ----------
    fontsize : float
        基础字号（默认 10.5，接近论文小四）。
    linewidth : float
        坐标轴边框线宽（顶刊默认 0.8-0.9）。
    dpi : int
        保存图片 DPI（默认 300，满足期刊要求）。
    """
    cjk = setup_fonts()

    mpl.rcParams.update({
        # 字体（若探测到中文字体则优先，未探测到则不覆盖英文默认）
        "font.size": fontsize,
        "axes.unicode_minus": False,
        # 坐标轴
        "axes.linewidth": linewidth,
        "axes.edgecolor": "#2b2b2b",
        "axes.labelcolor": "#2b2b2b",
        "axes.titlecolor": "#2b2b2b",
        # 刻度（顶刊 style：刻度朝外）
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.color": "#2b2b2b",
        "ytick.color": "#2b2b2b",
        "xtick.labelsize": fontsize - 1.5,
        "ytick.labelsize": fontsize - 1.5,
        # 图例
        "legend.frameon": False,
        "legend.fontsize": fontsize - 2,
        # 线条
        "lines.linewidth": 1.8,
        "lines.markersize": 4,
        # 网格（默认极淡 / 关闭）
        "axes.grid": False,
        # 保存参数
        "savefig.dpi": dpi,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
    })
    return cjk
