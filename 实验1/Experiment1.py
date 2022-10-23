# %% [markdown]
# # 实验1 玻尔振动的物理研究
# > Copyright(c) 2022 GeorgeDong32. All Rights Reserved.

# %%
from cProfile import label
import scipy.constants as cst
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# plt防止中文乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# %% [markdown]
# ### 测量摆轮摆幅$\theta$与固有周期$T_0$的关系
# 数据见theta-T0.csv

# %% [markdown]
# ### 阻尼系数$\beta$的计算

# %% [markdown]
# #### 阻尼挡位1

# %%
T1 = 1.5640
data1 = pd.read_csv("cbeta1.csv")
th11 = data1.iloc[:,0]
th12 = data1.iloc[:,1]
ln1 = np.log(th11 / th12)
avaln1 = np.mean(ln1)
beta1 = avaln1 / (th11.count() * T1)
print(ln1)
print("ln平均值=",avaln1)
print("beta1=", beta1)

# %% [markdown]
# #### 阻尼挡位2

# %%
T2 = 1.5693
data2 = pd.read_csv("cbeta2.csv")
th21 = data2.iloc[:,0]
th22 = data2.iloc[:,1]
ln2 = np.log(th21 / th22)
avaln2 = np.mean(ln2)
beta2 = avaln2 / (th21.count() * T2)
print(ln2)
print("ln平均值=",avaln2)
print("beta2=", beta2)

# %% [markdown]
# #### 阻尼挡位3

# %%
T3 = 1.5615
data3 = pd.read_csv("cbeta3.csv")
th31 = data3.iloc[:,0]
th32 = data3.iloc[:,1]
ln3 = np.log(th31 / th32)
avaln3 = np.mean(ln3)
beta3 = avaln3 / (th31.count() * T3)
print(ln3)
print("ln平均值=",avaln3)
print("beta3=", beta3)

# %% [markdown]
# ### 幅频/相频特性测量

# %%
def wr(w0,beta):
    return np.sqrt(w0*w0 - 2*beta*beta)

def thetar(m,w_r,beta):
    return m / (2*beta*w_r)

def phi_c(beta,T,T0):
    return np.arctan((beta*T0*T0*T)/(np.pi*((T*T) - (T0*T0))))

def thetae(w,w0,beta):
    return beta**2 / ((w-w0)**2 + beta**2)

E3data = pd.read_csv("3data.csv")
m = E3data.iloc[:,0]
TL = E3data.iloc[:,1]
theta = E3data.iloc[:,3]
T0 = E3data.iloc[:,4]
phi = E3data.iloc[:,5]
omega = 2*np.pi / TL
omega0 = 2*np.pi / T0
omegar = wr(omega0,beta3)
theta_r = thetar(m,omegar,beta3) * (180/np.pi)
d1 = omega / omegar
d2 = (theta / theta_r)**2
d3 = phi_c(beta3,TL,T0)
print(d1)
print(d2*10)
plt.figure(dpi=200)
plt.plot(omega,d2*10)
plt.savefig(".\幅频特性曲线.png")
plt.figure(dpi=200)
plt.plot(omega,thetae(omega,omega0,beta3))
plt.savefig(".\理想幅频特性曲线.png")
plt.figure(dpi=200)
plt.plot(d1,thetae(omega,omega0,beta3))
plt.savefig(".\对照理想幅频特性曲线.png")
plt.figure(dpi=200)
plt.plot(d1,d3)
plt.savefig(".\相频特性曲线.png")

# %%
print(d3/np.pi*180)


