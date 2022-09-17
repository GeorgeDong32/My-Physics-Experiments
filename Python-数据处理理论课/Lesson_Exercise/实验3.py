# 练习 3：
#结构体例子 if 语句。
a=1
b=0
#以上语句可以简化为 a,b=1,0， python 支持 a,b,c=i,j,k 的赋值方式
if a>0: #注意:下面表示控制体的内容，此处是如果 a>0，用 print 输出 a 是正数
    b = a  # 若 b=a 与 print 语句有相同缩进， 则他们在同一控制体内，即 a>0 时会执行 b=a。
print("a is postive and b is",b)
b=-1 #b=-1 是顶格缩进，因此与 if 无关，是完成 if 语句后继续执行的操作
print("after updated,b is ",b)

#for 循环和嵌套
#请尝试改变 print 的缩进，查看对输出结果的影响。
for i in range(4): #range 函数产生的结果是 0,1,2,3,注意不包括 4，而且初始是 0
    for j in range(i):
        print("i=", i, "j=", j)