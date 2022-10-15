# 实验六 传感器设计实验I
# Copyright(c) 2022 GeorgeDong32. All Rights Reserved.

from cProfile import label
import scipy.constants as cst
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# plt防止中文乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#拟合函数
def fit_fun1(u, k1, b1):
    return k1 * u + b1

def fit_fun2(u, k2, b2):
    return k2 * u + b2

def fit_fun3(u, k3, b3):
    return k3 * u + b3

# 导入数据
data1 = pd.read_csv("data1.csv")
x1 = data1.iloc[:,0]
u1 = data1.iloc[:,1]

data2 = pd.read_csv("data2.csv")
x2 = data2.iloc[:,0]
u2 = data2.iloc[:,1]

data3 = pd.read_csv("data3.csv")
x3 = data3.iloc[:,0]
u3 = data3.iloc[:,1]

# 数据拟合
popt1,pcov1=curve_fit(fit_fun1,u1,x1)
xf1 = fit_fun1(u1,popt1[0],popt1[1])

popt2,pcov2=curve_fit(fit_fun2,u2,x2)
xf2 = fit_fun1(u2,popt2[0],popt2[1])

popt3,pcov3=curve_fit(fit_fun1,u3,x3)
xf3 = fit_fun1(u3,popt3[0],popt3[1])

## 数据绘图区
plt.figure(dpi=250)
plt.scatter(u1,x1,marker='o',label="单臂原数据")
plt.plot(u1,xf1,color='red',label="单臂拟合结果")
plt.scatter(u2,x2,marker='*',label="半桥原数据")
plt.plot(u2,xf2,color='blue',label="半桥拟合结果")
plt.scatter(u3,x3,marker='s',label="全桥原数据")
plt.plot(u3,xf3,color='green',label="全桥拟合结果")
plt.xlabel("$U(mV)$",fontsize=12)
plt.ylabel("$x(mm)$",fontsize=12)
plt.title("金属箔式应变片X-U",fontsize=18)
plt.annotate("$x1 = %.2fu + %.2f$\n$x2 = %.2fu + %.2f$\n$x3 = %.2fu + %.2f$\nS1 = %.3f\nS2 = %.3f\nS3 = %.3f" %(popt1[0],popt1[1],popt2[0],popt2[1],popt3[0],popt3[1],1/popt1[0], 1/popt2[0], 1/popt3[0]), xy=(0,6.8))
plt.legend()
plt.savefig(".\金属箔式应变片X-U曲线.png")
plt.show()