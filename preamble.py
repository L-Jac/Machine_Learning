from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib_inline

matplotlib_inline.backend_inline.set_matplotlib_formats('pdf', 'png')  # 设置matplotlib保存图像的格式为pdf和png。
plt.rcParams['savefig.dpi'] = 300  # 设置保存图像的分辨率为300dpi。
plt.rcParams['image.cmap'] = "viridis"  # 设置默认的颜色映射为’viridis’。
plt.rcParams['image.interpolation'] = "none"  # 设置图像插值方法为’none’。
plt.rcParams['savefig.bbox'] = "tight"  # 设置保存图像时的边界框为’tight’，即紧凑型。
plt.rcParams['lines.linewidth'] = 2  # 设置线宽为2。
plt.rcParams['legend.numpoints'] = 1  # 设置图例中每个条目的标记点数为1。
plt.rc('axes', prop_cycle=(
        cycler('color', ['#0000aa', '#ff5050', '#50ff50', '#9040a0', '#fff000']) +
        cycler('linestyle', ['-', '-', "--", (0, (3, 3)), (0, (1.5, 1.5))])))
# 这个设置是用来改变默认的颜色循环和线型循环
# cycler('color', mglearn.plot_helpers.cm_cycle.colors)改变了颜色循环
# cycler('linestyle', ['-', '-', "--", (0, (3, 3)), (0, (1.5, 1.5))])改变了线型循环。

np.set_printoptions(precision=3, suppress=True)  # 设置numpy打印数组时的精度为3，且抑制科学计数法。

pd.set_option("display.max_columns", 8)  # 设置pandas打印DataFrame时最多显示8列。
pd.set_option('display.precision', 2)  # 设置pandas打印数据时的精度为2。

__all__ = ['np', 'display', 'plt', 'pd']
# 定义当从这个模块中导入所有名字时，应该导入哪些名字
# 当使用from preamble import *时，只有’np’、‘mglearn’、‘display’、'plt’和’pd’这五个名字会被导入。
