#!/usr/bin/env python
# coding: utf-8

# # Передискретизация цифровых сигналов



import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, rfft, irfft
import math



def getDataFromFile(path):
    if type(path) != str :
        return None
    f = open(path, 'r')
    elem = f.read().split()
    f.close()
    x = np.array(list(map(float, elem[0::2])))
    y = np.array(list(map(lambda x : float(x), elem[1::2])))
    return (x, y)


def getRange(x, y, start, end):
    startIndex = np.searchsorted(x, start)
    endIndex = np.searchsorted(x, end)
    return (x[startIndex : endIndex], y[startIndex : endIndex])



def downsampling(x, n):
    return x[::n]










def filter(x, r):
    n = len(x) // 2 + 1
    h = np.array([0 + 0j if i < r[0] * n or i > r[1] * n else 1 + 0j for i in range(n)])
    th = (irfft(h))
#     triangle = np.array([(1 - 2 * i / len(th)) if i < len(th) / 2 else 2 * ((i - len(th) / 2) / len(th)) for i in range(0, len(th))])
#     th = th * triangle
    hem = np.array([0.53836 - 0.46164 * math.cos(1. * math.pi + 1 * math.pi * i / (n - 1)) for i in range(len(th))])
    th = th * hem
    h = rfft(th)
    w = rfft(x)
    return irfft(h * w)





def upsampling(x, n):
#     plt.figure(figsize=(20,5))
#     plt.scatter(range(len(rfft(x)))[1:], rfft(x)[1:])
#     plt.plot()
    res = np.zeros(len(x) * n, dtype = x[0].dtype)
    for i in range(len(x)):
        res[ i * n] = x[i]
#     plt.figure(figsize=(20,5))
#     plt.scatter(range(len(rfft(res)))[1:], rfft(res)[1:])
#     plt.plot()
    res = filter(res, [0., 1 / n])
#     plt.figure(figsize=(20,5))
#     plt.scatter(range(len(rfft(res)))[1:], rfft(res)[1:])
#     plt.plot()
    return (res * n)



if __name__ == '__main__':

    # (x, y) = getDataFromFile("tested1.txt")
    # (x, y) = getRange(x, y, 400, 450)
    # x2 = downsampling(x, 2)
    # y2 = downsampling(y, 2)
    # x5 = downsampling(x, 5)
    # y5 = downsampling(y, 5)
    #
    # print("x has length: ", len(x))
    # print("x2 has length: ", len(x2))
    # print("x5 has length: ", len(x5))
    #
    # plt.figure(figsize=(20, 5))
    # plt.scatter(x, y, color='#FF000055', label="original", s=300)
    # plt.scatter(x2, y2, color='#00FF0055', label="downsampling x2", s=100)
    # plt.scatter(x5, y5, color='#0000FF55', label="downsampling x5")
    # plt.legend(loc='upper left')
    # plt.show()

    (x, y) = getDataFromFile("tested1.txt")
    (x, y) = getRange(x, y, 400, 450)
    n2 = 5
    x2 = upsampling(x, 2)
    y2 = upsampling(y, 2)
    x5 = upsampling(x, n2)
    y5 = upsampling(y, n2)

    print("x has length: ", len(x))
    print("x2 has length: ", len(x2))
    print("x5 has length: ", len(x5))

    # print(x)
    # print(x2)

    plt.figure(figsize=(20,5))
    plt.scatter(x, y, color = '#FF000055', label = "original", s = 300)
    plt.scatter(x2, y2, color = '#00FF0055', label = "upsampling x2", s = 100)
    plt.scatter(x5, y5, color = '#0000FF55', label = "upsampling x5")
    plt.legend(loc = 'upper left')
    plt.show()

    plt.figure(figsize=(20,5))
    plt.plot(range(len(y)), y, color = '#FF0000FF', label = "original")
    plt.legend(loc = 'upper left')
    plt.show()
    plt.figure(figsize=(20,5))
    plt.plot(range(len(y2)), y2, color = '#00FF00FF', label = "upsampling x2")
    plt.legend(loc = 'upper left')
    plt.show()
    plt.figure(figsize=(20,5))
    plt.plot(range(len(y5)), y5, color = '#0000FFFF', label = "upsampling x5")
    plt.legend(loc = 'upper left')
    plt.show()


    y1234 = np.zeros(len(y) * n2, dtype = x[0].dtype)
    for i in range(len(y)):
        y1234[ i * n2] = y[i]
    plt.figure(figsize=(20,5))
    plt.scatter(range(len(y1234)), y1234, color = '#FF000055', label = "original", s = 300)
    plt.scatter(range(len(y5)), y5, color = '#0000FF55', label = "upsampling x5")
    plt.ylim(bottom = 1)
    plt.legend(loc = 'upper left')
    plt.show()



