#读取核磁共振实验数据并进行拟合
#数据在Data1.csv和Data2.csv中
#Copyright(c) 2022 GeorgeDong32. All Rights Reserved.

from cProfile import label
import scipy.constants as cst 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
# plt防止中文乱码
plt.rcParams['font.family'] = ['Arial Unicode MS','Microsoft YaHei','SimHei','sans-serif']
plt.rcParams['axes.unicode_minus'] = False

#拟合函数定义
def fit_fun1(B, k1, b1):
    return k1 * B + b1

def fit_fun2(B, k2, b2):
    return k2 * B + b2

#数据导入
data1 = pd.read_csv("H2O.csv")
v_1 = data1.iloc[:,0]
B_1 = data1.iloc[:,1]

data2 = pd.read_csv("C2F4.csv",sep="\t")
v_2 = data2.iloc[:,0]
B_2 = data2.iloc[0:,1]

#数据拟合
popt1,pcov1=curve_fit(fit_fun1,B_1,v_1)
v_1fit = fit_fun1(B_1,popt1[0],popt1[1])

popt2,pcov2=curve_fit(fit_fun2,B_2,v_2)
v_2fit = fit_fun2(B_2,popt2[0],popt2[1])

#绘制图形
## 1号数据绘图区
plt.figure()
plt.axis([240,310,10,13])
plt.scatter(B_1,v_1,marker='o',label="原数据")
plt.plot(B_1,v_1fit,color='red',label="拟合结果")
plt.xlabel("$B(mT)$",fontsize=12)
plt.ylabel("$\\nu(MHz)$",fontsize=12)
plt.title("$H_2 O Sample$",fontsize=18)
plt.annotate("$\\nu = %5.4fB + %5.4f$\n" %(popt1[0],popt1[1]), xy=(260,12))
plt.legend()
plt.savefig(".\H2OSample.png")

## 2号数据绘图区
plt.figure()
plt.axis([270,330,11,13])
plt.scatter(B_2,v_2,marker='o',label="原数据")
plt.plot(B_2,v_2fit,color='green',label="拟合结果")
plt.xlabel("$B(mT)$",fontsize=12)
plt.ylabel("$\\nu(MHz)$",fontsize=12)
plt.title("$C_2 F_4 Sample$",fontsize=18)
plt.annotate("$\\nu = %5.4fB + %5.4f$\n" %(popt2[0],popt2[1]), xy=(305,12))
plt.legend()
plt.savefig(".\C2F4Sample.png")
plt.show()