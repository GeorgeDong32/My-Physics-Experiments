#练习15
import numpy as np #导入 numpy 库用于处理列表和阵列行数据，简称为 np
import matplotlib.pyplot as plt
# Piechart

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#Polar chart plot
r = np.linspace(0, 2, 100)
theta = 2 * np.pi * r
fig = plt.figure(figsize=(13, 4))
ax1 = plt.subplot(121, projection='polar')
ax1.scatter(theta, r, label = 'Polar Projection', s = 10)
ax1.legend(bbox_to_anchor = (.85, 1.35))
ax2 = plt.subplot(122)
ax2.scatter(theta, r, label = 'Planar Projection', s = 10)
ax2.legend(bbox_to_anchor = (0.85, 1.35))
ax2.set_xlabel('R')
ax2.set_ylabel(r'$\theta$')
plt.show()

#Polar bar chart
np.random.seed(10130)
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.random.rand(N) * .8 - .1
colors = plt.cm.Spectral(radii / 10)

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0,
       color=colors, alpha=0.5)
plt.show()

#Geographic projection
N = 100
np.random.seed(157)
long = np.random.random(N) * 360 - 180
lat = np.random.random(N) * 180 - 90
plt.figure(figsize=(12, 7))
plt.subplot(111, projection="aitoff")
plt.scatter(long, lat, marker = '*', color = 'red', s = 40)
plt.title("Aitoff")
plt.grid(True)
plt.show()

#3D scatter plot
projection = '3d'
N = 250
np.random.seed(124)
x = 15 * np.random.random(N)
y = np.sin(x) + 0.25 * np.random.random(N)
z = np.cos(x) + 0.25 * np.random.random(N)

plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')
ax.scatter3D(x, y, z, color = 'r')
ax.set_xlabel('x', fontsize = 20, labelpad = 20)
ax.set_ylabel('y', fontsize = 20, labelpad = 20)
ax.set_zlabel('z', fontsize = 20, labelpad = 20)
plt.show()

#3D line plot
N = 100
np.random.seed(124)
xline = np.linspace(0, 15, N)
yline = np.sin(xline)
zline = np.cos(xline)
fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')
ax.plot3D(xline, yline, zline)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((2, 1.5, 1.2))
ax.view_init(10, 180)
plt.show()

#Triangular 3D surfaces
N = 2000
np.random.seed(124)
r = 2 * np.pi * np.random.random(N)
theta = 20 * np.pi * np.random.random(N)
xdata = np.ravel(r * np.sin(theta))
ydata = np.ravel(r * np.cos(theta))
zdata = np.sin(xdata) + np.cos(ydata)
fig = plt.figure(figsize=(15, 6))
plt.subplots_adjust(wspace=0)
ax1 = plt.subplot(121, projection = '3d')
ax1.plot_trisurf(xdata, ydata, zdata, cmap = 'inferno')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.view_init(40, 100)
ax1.set_box_aspect((4.5, 4.5, 1.5))
ax1.set_title('Elevation = 40$^\circ$, Azimuth = 100$^\circ$')
ax2 = plt.subplot(122, projection = '3d')
ax2.plot_trisurf(xdata, ydata, zdata, cmap = 'inferno')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.view_init(20, 100)
ax2.set_box_aspect((4.5, 4.5, 1.5))
ax2.set_title('Elevation = 20$^\circ$, Azimuth = 100$^\circ$')
plt.show()

#2D Contour plot
N = 100
np.random.seed(100)
x = np.linspace(-2, 2, N) + np.random.random(N)
y = np.linspace(-2, 2, N) + np.random.random(N)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)**3
plt.figure(figsize=(15, 5))
plt.subplot(121)
plt.contourf(X, Y, Z, 50, cmap = 'inferno')
plt.colorbar()
plt.title('Contourf 2D counts = 50', pad = 10)
plt.subplot(122)
plt.contourf(X, Y, Z, 200, cmap = 'inferno')
plt.colorbar()
plt.title('Contourf 2D counts = 200', pad = 10)
plt.show()

#3D contour plot
N = 100
np.random.seed(3124)
x = np.linspace(-2, 2, N) + np.random.random(N)
y = np.linspace(-2, 2, N) + np.random.random(N)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')
ax.contour3D(X, Y, Z, cmap = 'Spectral')
plt.show()

#Surface plot
N = 200
np.random.seed(3124)
x = np.linspace(-2, 2, N) + np.random.random(N)
y = np.linspace(-2, 2, N) + np.random.random(N)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)
fig = plt.figure(figsize=(14, 6))
ax1 = plt.subplot(121, projection = '3d')# 3d contour plot
ax1.plot_surface(X, Y, Z,  cmap = 'Spectral')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_box_aspect((2, 2, 1))
ax1.view_init(60, 100)
ax1.set_title('Plot surface rstride = cstride = default, \n elevation = 60, azimuth = 100')
ax2 = plt.subplot(122, projection = '3d')# 3d contour plot
ax2.plot_surface(X, Y, Z,  cmap = 'Spectral', rstride = 1, cstride = 1)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_box_aspect((2, 2, 1))
ax2.view_init(60, 100)
ax2.set_title('Plot surface rstride = cstride = 1, \n elevation = 60, azimuth = 100')
plt.show()

#3D quiver plot
ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
# Make the direction data for the arrows
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *np.sin(np.pi * z))
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
plt.show()