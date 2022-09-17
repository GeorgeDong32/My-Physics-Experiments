# 练习 18
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
def ball_go(y, t, g, m, k, l):
    theta, omega = y
    d_theta = omega
    d_omega = -k / m * omega + g / l * np.sin(theta)
    return d_theta, d_omega
g = 9.8  # m/s
m = 1
k = 0.5
l = 1
t = np.linspace(0, 20, 1000)
y0 = np.array([np.pi * 1 / 3, 1])
# 使用odient进行求值
result = odeint(ball_go, y0, t, args=(g, m, k, l))
# 画静态图
plt.plot(t, result[:, 0], label='theta')
plt.plot(t, result[:, 1], label='omega')
plt.legend()
plt.show()

fig, ax = plt.subplots()
ax.grid()
ax.axis('scaled')
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
theta_ = np.linspace(0, np.pi * 2, 100)
x_round = np.cos(theta_)
y_round = np.sin(theta_)
ax.plot(x_round, y_round)
# 画动态图
def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    time_text.set_text('')
    return line, time_text
def update(frame):
    theta = result[:, 0][frame]
    x = [0, np.sin(theta) * l]
    y = [0, np.cos(theta) * l]
    time_text.set_text('time = %.1fs' % (0.02 * frame))
    line.set_data(x, y)
    return line, time_text
ani = animation.FuncAnimation(fig, update, range(len(result[:, 0])), init_func=init, interval=50)
ani.save('pendulum.gif')
plt.show()
