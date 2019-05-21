from math import sqrt


def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0, 0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0][0] = y[0] = y0[0]
    vy[0][1] = y[1] = y0[1]
    for i in range(1, n + 1):
        k1 = h * f(x, y[0], y[1])
        k2 = h * f(x + 0.5 * h, y[0] + 0.5 * k1, y[1] + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y[0] + 0.5 * k2, y[1] + 0.5 * k2)
        k4 = h * f(x + h, y[0] + k3, y[1] + k3)
        vx[i] = x = x0 + i * h
        vy[i][0] = y[0] = y[0] + (k1[0] + k2[0] + k2[0] + k3[0] + k3[0] + k4[0]) / 6
        vy[i][1] = y[1] = y[1] + (k1[1] + k2[1] + k2[1] + k3[1] + k3[1] + k4[1]) / 6
    return vx, vy


def f1(m, p, r):
    return r ** 2 * p


def n(p):
    return p ** (3 / 2) / (3 * sqrt(1 + p ** (2 / 3)))


def f2(m, p, r):
    return m * p / n(p) * r


def test1(m, p, r):
    return [1, 1]


vx, vy = rk4(test1, 0, 0, 10, 100)
for x, y in list(zip(vx[0], vy[0]))[::10]:
    print("%4.1f %10.5f %+12.4e" % (x, y, y - (4 + x * x) ** 2 / 16))
for x, y in list(zip(vx[1], vy[1]))[::10]:
    print("%4.1f %10.5f %+12.4e" % (x, y, y - (4 + x * x) ** 2 / 16))
