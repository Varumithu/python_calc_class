import math
import matplotlib.pyplot as plt
import numpy as np
from cmath import exp, pi
import scipy
import random

import scipy.signal as sig

N = 128


def dft(xs):
    n = len(xs)
    return [sum((xs[k] * exp(-2j * math.pi * i * k / n)
                 for k in range(n))) for i in range(n)]








def simple_convolution(F, G):
    lenA = len(F); lenB = len(G)
    if (lenA < lenB):
        temp = F
        F = G
        G = temp
        temp = lenA
        lenA = lenB
        lenB = temp

    res = [0 for i in range(lenA + lenB -1 )]
    for m in range(lenA):
        for n in range(lenB):
            res[m+n] += F[m] * G[n]
    return res


def autocorrelation(A):
    return simple_convolution(np.conj(A),A[::-1])



def fast_conv(F,G):
    return np.ndarray.flatten(scipy.ifft([scipy.fft(F,n=N + N - 1) *
                                          scipy.fft(G,n=N + N - 1)]))


def create_graph(discrete_f,discrete_g):
    f_wave = fast_conv(discrete_f, discrete_g)
    d_wave = simple_convolution(discrete_f, discrete_g)
    scale = [x for x in range(N + N - 1)]
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(10, 8))
    ax1.scatter(scale, d_wave, s=1)
    ax1.set_title('simple_convolution')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')

    ax2.plot(scale[0: N], discrete_f, linewidth=1)
    ax2.set_title('Original: F')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$y$')

    ax3.plot(scale[0: N], discrete_g, linewidth=1)
    ax3.set_title('Original: G')
    ax3.set_xlabel('$x$')
    ax3.set_ylabel('$y$')

    ax4.scatter(scale, f_wave, s=1)
    ax4.set_title('fast_convolution')
    ax4.set_xlabel('$x$')
    ax4.set_ylabel('$y$')


def cc_graph(F, G):
    f_wave = simple_convolution(F, G[::-1])
    scale = [x for x in range(len(f_wave))]
    fig, (ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=3, figsize=(10, 8))


    ax2.plot(scale[0: N], discrete_f, linewidth=1)
    ax2.set_title('Original: F')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$y$')

    ax3.plot(scale[0: N], discrete_g, linewidth=1)
    ax3.set_title('Original: G')
    ax3.set_xlabel('$x$')
    ax3.set_ylabel('$y$')

    ax4.scatter(scale, f_wave, s=1)
    ax4.set_title('crosscorrelation')
    ax4.set_xlabel('$x$')
    ax4.set_ylabel('$y$')



def comparison(F, G):
    f_wave = simple_convolution(F, G[::-1])
    scale = [x for x in range(len(f_wave))]
    fig, (ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=3, figsize=(10, 8))

    fft_wave = fast_conv(F, G[::-1])
    lib_wave = np.ndarray.flatten(sig.correlate(F, G))

    ax2.plot(scale, f_wave, linewidth=1)
    ax2.set_title('simple cc')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$y$')

    ax3.plot(scale, fft_wave, linewidth=1)
    ax3.set_title('fft cc')
    ax3.set_xlabel('$x$')
    ax3.set_ylabel('$y$')

    ax4.scatter(scale, lib_wave, s=1)
    ax4.set_title('scipy.signal.correlate')
    ax4.set_xlabel('$x$')
    ax4.set_ylabel('$y$')



if __name__ == "__main__":
    discrete_f = [(N // 2 + 20 > x > N // 2 - 20 if 10 else 0)
                  for x in range(N)]

    discrete_g = [(N // 2 + 20 > x > N // 2 - 20 if 10 else 0)
                  for x in range(N)]

    comparison(discrete_f, discrete_g)
    # create_graph(discrete_f, discrete_g)
    # cc_graph(discrete_f, discrete_g)
    discrete_f = [math.sin(2 * math.pi/N*x) for x in range(N)]
    discrete_g = [(N // 2 + 20 > x > N // 2 - 20 if 10 else 0)
                  for x in range(N)]

    comparison(discrete_f, discrete_g)
    # create_graph(discrete_f, discrete_g)
    # cc_graph(discrete_f, discrete_g)
    discrete_f = [random.uniform(-0.1,0.1) + math.sin(2 * math.pi/N*x)
                  for x in range(N)]

    discrete_g = [(N // 2 + 20 > x > N // 2 - 20 if 10 else 0)
                  for x in range(N)]
    comparison(discrete_f, discrete_g)
    # cc_graph(discrete_f, discrete_g)
    # create_graph(discrete_f, discrete_g)

    plt.show()

