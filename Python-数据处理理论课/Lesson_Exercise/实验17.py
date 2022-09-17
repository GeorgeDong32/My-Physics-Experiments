# 练习 17
import matplotlib.pyplot as plt #导入 matplotlib 作图库，并命名为 plt
import numpy as np #导入 numpy 库用于处理列表和阵列行数据，简称为 np

fb=60 #Hz baseline frequency
T=1/fb
N=1001
M=1
t=np.linspace(0, M*T, M*N) #time

A=2
w=0.005*T
delta=1e-2*(t[2]-t[1]) #shift time to avoid singular value
t1=0.35*T+delta
t2=T-t1
ft=A*(np.sinc((t-t1)/w)+np.sinc((t-t2)/w)) #sinc signal
plt.figure()
plt.subplot(121)
plt.plot(t, ft, 'o-')

bt=np.cos(2*np.pi*fb*t) # baseline
plt.plot(t, bt, '.-')

sigma=0.5
nt=sigma*np.random.random(len(t)) #noise
plt.plot(t, nt, 'x')
plt.xlabel('Time (second)')
plt.ylabel('Signal/Baseline/Noise')
plt.title(r'Signal $s(t)$/Baseline $b(t)$/Noise $n(t)$')
plt.legend([r'Signal $s(t)$', r'Baseline $b(t)$', r'Noise $n(t)$'])

f=ft+bt+nt # total signal
plt.subplot(122)
plt.plot(t, f, '.-')
plt.xlabel('Time (second)')
plt.ylabel('Total Signal')
plt.title(r'Total Signal $f(t) = s(t) + b(t) + n(t)$')
plt.show()

#Fourier Spectrum
F=np.fft.ifft(f)
dt=t[1]-t[0]
fmax=1/dt
freq=np.linspace(0, fmax, M*N)
plt.figure()
plt.subplot(231)
plt.plot(t, f, '.-')
plt.xlabel('Time (second)')
plt.legend([r'Original Signal $f(t)$'])
plt.subplot(234)
plt.plot(freq, abs(F), '.-')
plt.xlabel('Frequency (Hz)')
plt.legend([r'Fourier Spectrum $|F[k]|$'])

#filtering signal to remove baseline
F[1]=0
F[-1]=0
F[0]=0
fnew=np.fft.fft(F)
fnew=np.real(fnew)
plt.subplot(232)
plt.plot(t, fnew, '.-')
plt.xlabel('Time (second)')
plt.legend([r'Baseline Removed $f_b(t)$'])
plt.subplot(235)
plt.plot(freq, abs(F), '.-')
plt.xlabel('Frequency (Hz)')
plt.legend([r'Fourier Spectrum $|F_b[k]|$'])

#filtering signal to remove noise
F[100:900]=0
fnew=np.fft.fft(F)
fnew=np.real(fnew)
plt.subplot(233)
plt.plot(t, fnew, '.-')
plt.xlabel('Time (second)')
plt.legend([r'Baseline & Noise Removed $f_{bn}(t)$'])
plt.subplot(236)
plt.plot(freq, abs(F), '.-')
plt.xlabel('Frequency (Hz)')
plt.legend([r'Fourier Spectrum $|F_{bn}[k]|$'])
plt.show()
