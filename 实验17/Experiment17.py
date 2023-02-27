# 实验十七 迈克尔逊干涉实验
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

data = pd.read_csv("ndata.csv")
p1 = data.iloc[:,0]
N1 = data.iloc[:,1]
p2 = data.iloc[:,2]
N2 = data.iloc[:,3]

# 折射率计算
def calculate(l , N):
    return 1 + N * l * 760 / (2 * 8.2 * 20 / 100)

n1 = calculate(614E-9, N1)
n2 = calculate(614E-9, N2)
print(n1)
print(n2)
