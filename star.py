from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

M = 1
K = 10000 / M

def func_planet(t, Y):
    x = Y[0]
    y = Y[1]
    vx = Y[2]
    vy = Y[3]
    val = [vx, vy, -K*x/((x**2 + y**2)**1.5), -K*y/((x**2 + y**2)**1.5)]
    return np.asarray(val)

def runge_kutta(f, T, y0):
    y = y0
    Res = []
    for t in T:
        Res.append(y)
        k1 = dt * f(t, y)
        k2 = dt * f(t + dt / 2, y + k1 / 2)
        k3 = dt * f(t + dt / 2, y + k2 / 2)
        k4 = dt * f(t + dt, y + k3)
        y = y + (k1 + 2 * (k2 + k3) + k4) / 6
    return Res

def eiler(f, T, y0):
    y = y0
    Res = []
    for t in T:
        Res.append(y)
        y = y + dt * f(t, y);
    return Res

dt = 0.2
N = 120
T = np.arange(0, N*dt, dt)
Y0 = [100, 0, 0, 5]

rk = runge_kutta(func_planet, T, np.asarray(Y0))
eil = eiler(func_planet, T, np.asarray(Y0))

x_rk = []
y_rk = []
for i in range(N):
    x_rk.append(rk[i][0])
    y_rk.append(rk[i][1])

x_eil = []
y_eil = []
for i in range(N):
    x_eil.append(eil[i][0])
    y_eil.append(eil[i][1])


#colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))**2
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.scatter(np.asarray(x_rk), np.asarray(y_rk))
plt.scatter(np.asarray(x_eil), np.asarray(y_eil))
plt.scatter(0, 0, c = "#FFFF00", s = 1000)
plt.show()
