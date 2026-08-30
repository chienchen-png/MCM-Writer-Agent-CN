"""mcmplot.colors —— 全局配色字典 COLOR_SCHEMES 与常用色板。

支持三套配色（方案A/B/C 沿用既有chart-designer规范），
以及顶刊风格所需的连续色板（供 LinearSegmentedColormap 使用）。
"""

# 方案A：经典学术蓝-橙（默认）
SCHEME_A = {
    "blue": "#2B579A",
    "orange": "#E87722",
    "green": "#6B8E23",
    "purple": "#8B008B",
}

# 方案B：暖色对比
SCHEME_B = {
    "red": "#C0392B",
    "blue": "#2980B9",
    "gold": "#F39C12",
    "green": "#27AE60",
}

# 方案C：冷色专业
SCHEME_C = {
    "deep_blue": "#1A5276",
    "dark_green": "#117864",
    "deep_purple": "#7D3C98",
    "dark_red": "#B03A2E",
}

# 来源③ 博主使用的多 y 轴配色（亦收进库）
SCHEME_D = {
    "red": "#E74C3C",
    "navy": "#3B4A6B",
    "teal": "#1C8C85",
}

# 全局配色字典：用 scheme_id 一键切换
COLOR_SCHEMES = {
    "A": list(SCHEME_A.values()),
    "B": list(SCHEME_B.values()),
    "C": list(SCHEME_C.values()),
    "D": list(SCHEME_D.values()),
}

# 顶刊连续色板（蓝-白-橙），供 LinearSegmentedColormap 使用
TOP_JOURNAL_CMAP = ["#2166AC", "#FFFFFF", "#F4A582"]  # 蓝-白-红棕


def get_palette(scheme="A"):
    """按 scheme 标识返回 4 色列表。

    Parameters
    ----------
    scheme : str
        "A" / "B" / "C" / "D"。
    """
    return COLOR_SCHEMES.get(scheme.upper(), COLOR_SCHEMES["A"])
