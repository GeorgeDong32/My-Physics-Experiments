#生成有误差的高斯分布数据并进行拟合处理的代码
#Copyright(c) 2022 GeorgeDong32. All Rights Reserved.
from cProfile import label
from cmath import pi
import scipy.constants as cst 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
# plt防止中文乱码
plt.rcParams['font.family'] = ['Arial Unicode MS','Microsoft YaHei','SimHei','sans-serif']
plt.rcParams['axes.unicode_minus'] = False
#函数定义
def specExp(x,a,b): #采用另一种形式的高斯分布函数。
    return a*np.exp(-(a*x-b)**2)/np.sqrt(cst.pi)

def fit_gaussian(x,m,s):#用于拟合的高斯分布标准函数
    mid1 = 1 / (np.sqrt(2 * pi) * s)
    mid2 = -1 / (2 * s * s)
    return mid1 * np.exp(mid2 * (x - m)**2)
   
mu,sigma=1,0.3 #高斯分布参数 mu 和 sigma
a,b=1/(np.sqrt(2*sigma**2)),mu/np.sqrt(2)/sigma #将 mu， sigma 折算为 a,b
x=np.arange(0,2,0.05)
y_test=specExp(x,a,b)+0.2*np.random.rand(len(x))-0.1 #利用随机数产生-0.1~0.1 之间的误差
#进行拟合
popt,pcov=curve_fit(fit_gaussian,x,y_test)
y_fit=fit_gaussian(x,popt[0],popt[1])

#绘制图像
plt.scatter(x,y_test,marker='o',label="原数据")
plt.plot(x, y_fit,color='red',label="拟合结果")
plt.xlabel("$x$",fontsize=16)
plt.ylabel("$p( x )$",fontsize=16)
plt.title("高斯分布数据拟合",fontsize=20)
plt.annotate("$p(x)= \\frac{1}{\sqrt{2\pi \sigma}} exp(-\\frac{(x-\mu)^2}{2\sigma^2})$\n"
             "$\sigma = %5.2f$\n"
             "$\mu = %5.2f$\n" %(popt[0],popt[1]), xy=(0,1.1))
plt.legend()
#在show前导出图像
plt.savefig(".\Gaussian_fitting.png")
plt.show()