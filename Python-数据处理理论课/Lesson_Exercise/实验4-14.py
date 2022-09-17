# 练习 4
#数据读入，以 data example.txt 为例
import pandas as pd #导入 pandas 库用于整理数据，并将 pandas 简称为 pd
import numpy as np #导入 numpy 库用于处理列表和阵列行数据，简称为 np
data=pd.read_csv("Example_T.txt", sep=' ', encoding='utf-8') #读取 Example_T.txt 中的数据，在标准情况下，#第一行被认为是列名，同时给数据自动添加行号索引
print('This is the original data:')
print(data)

# 练习 5
#数据读切片例子，可根据需要保留某些语句，然后注释其他，以查看输出的结果如何
print("按照列名读取整列数据，注意列名用单引号或双引号包含：")
print(data["温度/℃"])

print('根据行数读取数据:')
print(data.iloc[14])

print('按照标签读取其中的数据，其中列标签筛选数据:')
print(data.loc[0:10:2,"降温电阻/ohm":"升温电阻/ohm"])

print('利用过滤读取温度列小于 50℃ 的数据结果，其中 data["温度/℃"]<50 是用于获得一个列表标记低于 50 的元素有哪些:')
print(data[data["温度/℃"]<50])

print('#列出 data 中 NaN 的项， pd.isna()判断数值是否为NaN:')
print(data[data["降温电阻/ohm"].isna()])

#为了方便处理数据，重新命名列名称
data.columns=["T/℃","Ra/ohm","Rd/ohm"]
print('This is the new data:')
print(data)

# saving the dataframe
data.to_csv(r'Example_T_new.txt',sep=' ')

# 练习 6
#简单的数据处理
#1. 删除 NaN 数据
# data.dropna(inplace=True) #dropna 用于删除 NaN 的数据， inplace 选型规定在源数据中进行删除操作而不是备份
data=data.dropna() #与上面语句等效
print('删除 NaN 后的数据:')
print(data)

#2. 根据已有数据计算
data["Rmean"]=(data["Ra/ohm"]+data["Rd/ohm"])/2 #增加一列 Rmean，计算电阻平均值并储存。
data["err"]=np.random.rand(len(data))*0.1*data["Ra/ohm"]
#增加一列 err， 以 Ra 的 10%为上限产生一组随机数，获得误差值
print('添加均值和偏差后的数据:')
print(data) #检查数据

# 练习 7
#作图展示
import matplotlib.pyplot as plt #导入 matplotlib 作图库，并命名为 plt
data.columns=["T","Ra","Rd","Rmean","err"]
data.plot(x="T",y=["Ra","Rd","Rmean"]) # 以 温 度 为 横 坐 标 画 电 阻 随 温 度 变 化图,pd.plot 引用的是 plt 中的作图函数
#data.plot(x="T",y=["Ra","Rmean"]) #选取其中两条曲线画在同一个图上
#读取可以被 10 整除的温度值进行作图。作图类型为散点，同时在数据中给出误差棒
data[data["T"]%10==0].plot(kind="scatter",x="T",y="Rmean",yerr="err")
plt.show()#展示作图结果

# 练习 8
#对作图进行细节处理
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
#使用 pd.plot 进行作图,赋值到 ax 后，可以进行更多灵活处理
ax=data.plot(x="T",y=["Ra","Rd","Rmean"], #plot 画线图
style=["*-","o-",">-"], #指定每条曲线的点和线的具体形状
label=["升温电阻","降温电阻","平均电阻"], #图例标签
title="升降温电阻曲线", #设置标题
xlim=[-10,150], #x 轴作图范围
ylim=[-10,1000] #y 轴作图范围
)

#设置纵横坐标的
ax.set_xlabel("温度/℃")
ax.set_ylabel("电阻/ohm")
#设置指示箭头突出关注点
ax.annotate(r"$R_{mean}=\frac{R_a+R_d}{2}$",#开头的 r 是必须的，否则不能输入Latex 语言标记的文字内容
xy=tuple(data.loc[5,["T","Rmean"]]),# 箭头所在位置
# xycoords='data', #默认值， xy 坐标是数据的坐标，也可以指定图像位置
textcoords='offset points',#指定文字位置的参考形式，确定 xytest 的坐标是相对坐标
xytext=(+30,-40),#文字框左下角的坐标，此处+， -代表在箭头基础上的偏移
fontsize=16, #字体大小
#arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.5")
#箭头特性，弯箭头
arrowprops=dict(facecolor='black', shrink=0.05),#箭头特性，
)
# pandas 库的 pd.DataFrame.plot 类实质上继承的是 matplotlib 中的作图类，因此参数和设置与 matplotlib 中的作图函数大致相同，
# 而部分在 pd.DataFame.plot 中不能使用的参数设置，可以用 matplotlib 进行设置，如上例中的 set_xlabel 和 annotation 等，
# 因此， pd.plot 能实现的都可以通过 matplotlib 中的相应方法实现。下面给出上图的实现方案。
plt.show()

# 练习 9
#多坐标结果展示，将升温电阻和随机误差画在同一个图，该图左侧 y 坐标表示温度，右侧 y 坐标表示误差波动情况，
# 然后添加一个新的数据来获得新的第 3 个坐标显示

#为了实现更复杂的画图效果， 需要利用 matplotlib 库的方法进行作图
fig=plt.figure() #用默认值初始化一个画布
ax1=plt.subplot(1,1,1) #加第一个子图，该图的坐标轴默认在左侧，参数(1,1,1)表示画布分割区域只有一个，且在第一个空间作图
fig.subplots_adjust(right=0.75)
#在第一个子图中作图
ax1.plot(data["T"],data["Ra"],"b")
ax1.set_xlabel("温度/℃",fontsize=12)
ax1.set_ylabel("升温电阻/ohm",fontsize=12)
ax1.set_title("多坐标轴结果显示")
ax1.yaxis.label.set_color("b") #将坐标字体转设为相应的颜色
ax1.tick_params(axis="y",colors="b") #将刻度转为相应的颜色
#在第二个子图中作图
ax2=ax1.twinx() #此步关键，表示 ax1 和 ax2 是用相同的 x 坐标作图，
ax2.plot(data["T"],data["err"],"r")
ax2.set_ylabel("温度误差值/ohm",fontsize=12)
ax2.yaxis.label.set_color("r") #将坐标字体转设为相应的颜色
ax2.tick_params(axis="y",colors="r") #将刻度转为相应的颜色
#第三个子图数据,Sin(Va)
ax3=ax1.twinx()
ax3.plot(data["T"],np.sin(data["Ra"]),"g*--")
# ax3.spines.right.set_position(("axes", 1.2)) #将在右侧的第三轴偏移，避免与第二轴重合。
ax3.spines["right"].set_position(("axes",1.2)) #将在右侧的第三轴偏移，避免与第二轴重合。
ax3.set_ylabel(r"$sin(R_a)$")
ax3.yaxis.label.set_color("g") #将坐标字体转设为相应的颜色
ax3.tick_params(axis="y",colors="g") #将刻度转为相应的颜色
plt.show()

# 练习 10
#在同一个画布中做出两个并列放置的子图
fig=plt.figure(figsize=(10,5)) #指定画布大小
ax1=plt.subplot(1,2,1) #参数意义是：将画布分割行是 1，列是 2 的空间，按空间次序在第 1 个位置画图
ax1.plot(data["T"],data["Ra"])
ax2=plt.subplot(1,2,2) #用相同的画布分割，在空间次序第 2 个位置画图
ax2.plot(data["T"],data["err"])

# 练习 11
#以下内容请自己尝试,理解 subplot 的参数意义
fig=plt.figure(figsize=(10,10))#指定画布大小
ax1=plt.subplot(2,2,1) #参数意义：画布按 2× 2 分割，按空间次序在第 1 个位置画图
ax1.plot(data["T"],data["Ra"])
ax2=plt.subplot(2,2,(2,4)) #用相同的画布上，在空间次序第 2 和 4 两个位置合并画图
ax2.plot(data["T"],data["err"],"r")
ax3=plt.subplot(2,2,3) #在原来 2*2 的画布上，在空间次序为 3 的位置作画。
ax3.plot(data["T"],np.sin(data["Ra"]),"g*--")

# 练习 12
#课堂作业：请利用已有的数据，用程序画出下图的效果：
fig=plt.figure(figsize=(10,10)) #指定画布大小
ax1=plt.subplot(2,2,(1,2)) #参数意义：画布按 2× 2 分割，在第 1 和 2 位置合并画图
ax1.plot(data["T"],data["Ra"])
ax2=plt.subplot(2,2,3) #用相同的画布上，在空间次序第 3 位置画图
ax2.plot(data["T"],data["err"],"r")
ax3=plt.subplot(2,2,4) #在原来 2*2 的画布上，在空间次序为 4 的位置作画。
ax3.plot(data["T"],np.sin(data["Ra"]),"g*--")

# 练习 13
#数据拟合
from scipy.optimize import curve_fit #仅导入 curve_fit 函数
data_fitting=data[["T","Ra"]].copy() #切片选取其中的温度和升温电阻数据,copy 是获得副本，而不是对源数据进行操作
data_fitting["T"]=data_fitting["T"]+273.15 #将温度数据进行单位转换，由℃ 转为 K

#按照线性函数定义拟合函数的形式和输入参数
def fit_equs(T,k,Rbias): #定义函数
    return k * T + Rbias

#检验函数
# 令 k=0.1,Rbias=10， T 为 273 时,函数应该返回 37.3
# fit_equs(273,0.1,10)==37.3

#利用 scipy.optimize.curve_fit 进行拟合， popt:返回参数， popt[0],popt[1]分别对应 k 和 Rbias， pcov 返回 2 维矩阵是相关系数矩阵，可用 perr=np.sqrt(np.diag(pcov))获得标准差
param_bounds=([-np.inf,-np.inf],[np.inf,np.inf]) #限定 k 和 Rbias 的范围,第一个List 是两个参数的下限，第二个 List 是两个参数的上限
popt,pcov=curve_fit(fit_equs,data_fitting["T"],data_fitting["Ra"],bounds=param_bounds)
result_fitting=[fit_equs(x,popt[0],popt[1]) for x in data_fitting["T"]]
#弹出独立窗口显示结果
#%matplotlib
#%matplotlib inline #使用在线显示作图结果模式
#将拟合后的结果在图中显示，此处用 plt.plot 方法
plt.figure(figsize=(10,7)) #设置画布尺寸
plt.plot(data_fitting["T"],data_fitting["Ra"],"bo",label="测量结果") #测量结果，散点图
plt.plot(data_fitting["T"],result_fitting,"r--",label="拟合结果")#拟合结果，虚线图
#利用 scipy.optimize.curve_fit 进行拟合， popt:返回参数， popt[0],popt[1]分别对应 k 和 Rbias， pcov 返回 2 维矩阵是相关系数矩阵，可用 perr=np.sqrt(np.diag(pcov))获得标准差
param_bounds=([-np.inf,-np.inf],[np.inf,np.inf]) #限定 k 和 Rbias 的范围,第一个List 是两个参数的下限，第二个 List 是两个参数的上限
popt,pcov=curve_fit(fit_equs,data_fitting["T"],data_fitting["Ra"],bounds=param_bounds)
result_fitting=[fit_equs(x,popt[0],popt[1]) for x in data_fitting["T"]]
#弹出独立窗口显示结果
#%matplotlib
#%matplotlib inline #使用在线显示作图结果模式
#将拟合后的结果在图中显示，此处用 plt.plot 方法
plt.figure(figsize=(10,7)) #设置画布尺寸
plt.plot(data_fitting["T"],data_fitting["Ra"],"bo",label="测量结果") #测量结果，散点图
plt.plot(data_fitting["T"],result_fitting,"r--",label="拟合结果")#拟合结果，虚线图

#细化图中的设置
plt.xlabel("温度/℃",fontsize=16)
plt.ylabel("电阻/ohm",fontsize=16)
plt.title("升温电阻随温度变化的实验结果及其拟合",fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16,loc=2)
#plt.savefig("Temperautre_fitting.png") #将结果导出到图形文件中。

#计算拟合的相关系数 R^2
def R2(y_pred,y_test):
    SStot=np.sum((y_test-np.mean(y_test))**2)
    SSres=np.sum((y_test-y_pred)**2)
    return 1-SSres/SStot

r2=R2(result_fitting,data["Ra"]) #将拟合数据和实验数据代入计算获得 R^2

#将确定系数和公式等信息在图中绘出
plt.annotate("$y=kT+R_{bias}$\n "
             "k=%5.2fK/V\n"
             "$R_{bias}=%5.2fV$\n"
             "$R^2=%1.3f$" %(popt[0],popt[1],r2), xy=(280,600), fontsize=16)
plt.show()

# 练习 14
#均匀刻度分布误差
# 利用rand函数产生服从（a-b）均匀分布的随机序列
a=2       # (a-b)均匀分布下限
b=3    # (a-b)均匀分布上限
fs=1e7    # 采样率，单位：Hz
t=1e-3    # 随机序列长度，单位：s
n=int(t*fs)
u=np.random.uniform(0, 1, n)  # 产生（0-1）单位均匀信号
x=(b-a)*u+a  # 广义均匀分布与单位均匀分布之间的关系
plt.figure()
plt.subplot(211)
plt.plot(x) # 输出信号图
plt.title('均匀分布信号')
plt.subplot(212)
plt.hist(x, bins='auto') # 输出信号的直方图
plt.title('均匀分布信号直方图')
plt.show()

#高斯正态分布
x=np.random.normal(0,1,10001)
plt.figure
plt.subplot(211)
plt.plot(x) # 输出信号图
plt.title('高斯正态分布信号')
plt.subplot(212)
plt.hist(x, bins='auto') # 输出信号的直方图
plt.title('高斯正态分布信号直方图')
plt.show()

#数据统计
err=result_fitting-data["Ra"]
plt.figure()
plt.plot(err,'o-')
max_err=np.max(abs(err))
min_err=np.min(abs(err))
std=np.std(err)
var=np.var(err)
title=r'$\sigma$='+str(std)+r'; $\sigma^2$ ='+str(std**2)+'; Var ='+str(var)+r'; max($\epsilon$)='+str(max_err)+r'; min($\epsilon$)='+str(min_err)
print(title)
plt.title(title)
plt.ylabel(r'Error of Ra Fitting: $\epsilon$')
plt.show()