# 读取核磁共振实验数据并进行拟合
# 数据在Data1.csv和Data2.csv中
# Copyright(c) 2022 GeorgeDong32. All Rights Reserved.

from cProfile import label
import scipy.constants as cst
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# plt防止中文乱码
plt.rcParams['font.family'] = ['Arial Unicode MS', 'Microsoft YaHei', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False


# 拟合函数定义
def fit_fun1(B, k1, b1):
    return k1 * B + b1


def fit_fun2(B, k2, b2):
    return k2 * B + b2


# 数据导入
data1 = pd.read_csv("H2O.csv")
v_1 = data1.iloc[:, 0]
B_1 = data1.iloc[:, 1]

data2 = pd.read_csv("C2F4.csv", sep="\t")
v_2 = data2.iloc[:, 0]
B_2 = data2.iloc[0:, 1]

# 数据拟合
popt1, pcov1 = curve_fit(fit_fun1, B_1, v_1)
v_1fit = fit_fun1(B_1, popt1[0], popt1[1])

popt2, pcov2 = curve_fit(fit_fun2, B_2, v_2)
v_2fit = fit_fun2(B_2, popt2[0], popt2[1])

# 数据处理
h = 6.626E-34
nu_0 = 5.051E-27
g_h = (h / nu_0) * popt1[0] * 1E9
g_f = (h / nu_0) * popt2[0] * 1E9
stdg_h = 5.5857
stdg_f = 5.2567
deltag_h = (g_h - stdg_h) / (stdg_h / 100)
deltag_f = (g_f - stdg_f) / (stdg_f / 100)

# 绘制图形
## 1号数据绘图区
plt.figure()
plt.axis([240, 310, 10, 13])
plt.scatter(B_1, v_1, marker='o', label="原数据")
plt.plot(B_1, v_1fit, color='red', label="拟合结果")
plt.xlabel("$B(mT)$", fontsize=12)
plt.ylabel("$\\nu(MHz)$", fontsize=12)
plt.title("$H_2 O Sample$", fontsize=18)
plt.annotate("$\\nu = %5.4fB + %5.4f$\n$g_h = %5.4f$\n$Standard \\ g_h = %5.4f$\n$\\Delta = %5.4f\%%$"% (popt1[0], popt1[1], g_h, stdg_h, deltag_h),
             xy=(260, 12))
plt.legend()
plt.savefig(".\H2OSample.png")

## 2号数据绘图区
plt.figure()
plt.axis([270, 330, 11, 13])
plt.scatter(B_2, v_2, marker='o', label="原数据")
plt.plot(B_2, v_2fit, color='green', label="拟合结果")
plt.xlabel("$B(mT)$", fontsize=12)
plt.ylabel("$\\nu(MHz)$", fontsize=12)
plt.title("$C_2 F_4 Sample$", fontsize=18)
plt.annotate("$\\nu = %5.4fB + %5.4f$\n$g_f = %5.4f$\n$Standard \\ g_f = %5.4f$\n$\\Delta = %5.4f\%%$" % (popt2[0], popt2[1], g_f, stdg_f, deltag_f),
             xy=(305, 12))
plt.legend()
plt.savefig(".\C2F4Sample.png")
plt.show()
