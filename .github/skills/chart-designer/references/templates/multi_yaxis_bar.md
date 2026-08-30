# 多 Y 轴渐变色嵌套柱状图（工程化多轴架构）

## 图示说明

在同一画布用多个独立的频率 Y 轴清晰展示不同样本量/量纲的数据分布。柱子代表各组频数，其上彩色虚线是基于均值和标准差的正态分布概率密度曲线。核心技巧：模块化 4 分层（环境→颜色库→绘图函数→执行）、`COLOR_SCHEMES` 字典管理配色、`scheme_id` 一键切换、多 Y 轴 + 子图编号。

## 官方代码

### C1 环境设置

```python
import numpy as np
import pandas as pd
# =========================================================================================
# ====================================== 1. 环境设置 =======================================
# =========================================================================================
```

### C2 颜色库

```python
# =========================================================================================
# ======================================2.颜色库==========================================
# =========================================================================================
COLOR_SCHEMES = {
    1: ['#E74C3C', '#3B4A6B', '#1C8C85'],
}
```

### C3 绘图函数

```python
# =========================================================================================
# ======================================3.绘图函数=========================================
# =========================================================================================
def plot_residual_stacked_histogram(df_real, scheme_id):
    selected_hex_colors = COLOR_SCHEMES[scheme_id] # 获取配色方案
    colors_list = selected_hex_colors[:len(sources)] # 分配颜色

    # 创建画布
    fig, ax = plt.subplots(figsize=(8, 6))
    # 绘制子图编号
    ax.text(0.85, 0.9, '(a)', transform=ax.transAxes,
            fontsize=30, fontweight='bold', va='bottom', ha='left')
    ax.tick_params(axis='y', colors=colors_list[0])
    ax.spines['left'].set_color(colors_list[0])

    # 创建多 y 轴
    axes = [ax] # 存放多 Y 轴
    # 设置刻度样式
    ax_new.tick_params(axis='y', colors=colors_list[i])
    ax_new.spines['right'].set_color(colors_list[i]) # 边框组颜色
    for label in ax_new.get_yticklabels():
        label.set_fontsize(11)
    axes.append(ax_new) # 保存

    # 绘制渐变色直方图
    patches = []   # 存放柱子
    max_counts = []  # 各组最大频数
    for i, (res, current_ax) in enumerate(zip(res_list, axes)):
        n, _, p = current_ax.hist(res, bins=bins, stacked=False,
                                  edgecolor='white', linewidth=0,
                                  rwidth=0.95 - i * 0.20)

    # 绘制正态分布曲线
    x_pdf = np.linspace(-res_limit, res_limit, 200) # 生成坐标用于绘制正态曲线
    ax.set_xlim(-res_limit, res_limit)  # X轴范围
    max_pdf = max(y_pdf * scale_factor) if len(y_pdf) > 0 else 0
    line_normals.append(plt.Line2D([0], [0],
                                   color=colors_list[i], linestyle='--',
                                   lw=2.5, label=rf'... $\mu={mean_i:.1f}$, $\sigma = {std_i:.1f}$'))

    # x轴标题
    ax.set_xlabel(r'Residual ($\mu\epsilon$)', fontsize=14, fontweight='bold')
    # 添加图例
    ax.legend(handles=legend_patches + line_normals,
              loc='upper left', prop={'size': 9},
              edgecolor='gray', framealpha=1)
```

### C4 执行部分

```python
# =========================================================================================
# ======================================4.执行部分=========================================
# =========================================================================================
if __name__ == "__main__":
    df_data = pd.read_excel(r'\data.xlsx')  # 读取数据
    scheme_id = 1
    print(f'正在绘制并保存方案：{scheme_id}')
    plot_residual_stacked_histogram(df_data, scheme_id)
```

## 注意

> ⚠️ 此代码为博主"占位示例"，含 `sources`、`res_list`、`bins`、`res_limit`、`scale_factor`、`y_pdf`、`legend_patches` 等需按实际数据定义的占位变量。**保留其模块化架构 + 字典配色 + 多轴/子图编号技巧**，实际应用时补齐数据变量。这是官方代码的忠实转写。

## 适用场景

多分组/多量纲数据的频数分布对比（需在同一画布展示不同样本量或不同量纲的 Y 轴）。

## 来源

公众号「Python绘制多y轴渐变色嵌套柱状图」—— 来源③ C，作者：关注公众号「python+遥感学习日志」
