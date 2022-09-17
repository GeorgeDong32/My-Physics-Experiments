# 练习 19
import matplotlib.pyplot as plt #导入 matplotlib 作图库，并命名为 plt
import numpy as np #导入 numpy 库用于处理列表和阵列行数据，简称为 np
#矩阵运算
t=np.linspace(0, 1, 1001)
f1=np.random.random(len(t))
f1=f1-np.mean(f1)
f1=f1/np.sqrt(np.mean(f1**2))
corr=0.9
noise=np.random.random(len(t))
noise=noise-np.mean(noise)
noise_norm=noise/np.sqrt(np.mean(noise**2))
f2=corr*f1+np.sqrt(1-corr**2)*noise_norm
f2=f2-np.mean(f2)
f2=f2/np.sqrt(np.mean(f2**2))
plt.figure()
plt.plot(t, f1, '.-')
plt.plot(t, f2, 'r.-')
plt.xlabel('Time (second)')
plt.legend([r'$f_1(t)$', r'$f_2(t)$'])

#Compute covariance matrix of f1 and g2
R11=np.mean(f1*f1)
R22=np.mean(f2*f2)
R12=np.mean(f1*f2)
R21=R12
Cov=np.zeros((2,2))
Cov[0,0]=R11
Cov[0,1]=R12
Cov[1,0]=R21
Cov[1,1]=R22
print('Cov=', Cov)
plt.show()

#De-correlation: Eigen problems
[Eigenvalues, Eigenvectors]=np.linalg.eig(Cov)
C=Eigenvectors
b1=C[0,0]*f1+C[1,0]*f2
b2=C[0,1]*f1+C[1,1]*f2
Cov_b=np.zeros((2,2))
Cov_b[0,0]=np.mean(b1*b1)
Cov_b[1,1]=np.mean(b2*b2)
Cov_b[0,1]=np.mean(b1*b2)
Cov_b[1,0]=Cov_b[0,1]
print('Covariance Matrix of b =', Cov_b)
print('Theory of Eigenvalues =', Eigenvalues)
print('f to b transform matrix C=', C)




