from numpy.fft import rfft, rfftfreq, irfft, fft, ifft, fftfreq
import numpy.fft
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np
import cmath

N = 3000

def BandPassFilter(sig, left, right):
    freq_axis = fftfreq(N)
    time_axis = np.arange(N)
    filter = np.zeros(len(freq_axis), dtype=complex)
    border = left + right
    phase = 0
    # for i in range(2*(int(N/2) - border )):
    #     filter[i + int(N/2) - (int(N/2) - border)] = 1

    for i in range(left, right):
        filter[i] = cmath.rect(1, phase)
        filter[i + N - left - right] = cmath.rect(1, -phase)
        phase += 2 * cmath.pi / len(range(left, right))

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(nrows=7, ncols=1, figsize=(12, 10))

    ax1.plot(freq_axis, abs(filter))
    ax1.set_xlabel('f, c')
    ax1.set_ylabel('U, мВ')

    spectrum = ifft(filter)
    # spectrum -= spectrum.imag * 1j
    # spectrum = abs(spectrum)

    for i in range(len(spectrum)):
        if time_axis[i] > 500 and (time_axis[i] < (time_axis[len(spectrum) - 1] - 500)):
            spectrum[i] = 0

    ax2.plot(np.arange(len(spectrum)), spectrum.real)
    ax2.set_xlabel('t, s')
    ax2.set_ylabel('U, мВ')

    filter = fft(spectrum)

    ax3.plot(freq_axis, abs(filter))
    ax3.set_xlabel('f, c')
    ax3.set_ylabel('U, мВ')

    ax4.plot(np.arange(len(sig)), sig)
    ax4.set_xlabel('t, c')
    ax4.set_ylabel('U, мВ')

    fourier_of_sig = fft(sig)

    ax5.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))
    ax5.set_xlabel('f, Гц')
    ax5.set_ylabel('U, мВ')

    fourier_of_sig = fourier_of_sig * abs(filter)

    ax6.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))
    ax6.set_xlabel('f, Гц')
    ax6.set_ylabel('U, мВ')
    filtered_sig = ifft(fourier_of_sig)
    ax7.plot(np.arange(len(filtered_sig)), filtered_sig)
    ax7.set_xlabel('t, c')
    ax7.set_ylabel('U, мВ')

    plt.show()


def HighPassFilter(sig, border):
    freq_axis = fftfreq(N)
    time_axis = np.arange(N)
    filter = np.zeros(len(freq_axis), dtype=complex)

    phase = 0
    # for i in range(2*(int(N/2) - border )):
    #     filter[i + int(N/2) - (int(N/2) - border)] = 1

    for i in range(2*(int(N/2) - border )):
        filter[i + int(N/2) - (int(N/2) - border)] = cmath.rect(1, phase)
        phase += 2 * cmath.pi / (2*(int(N/2) - border ))

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(nrows=7, ncols=1, figsize=(12, 10))

    ax1.plot(freq_axis, abs(filter))

    spectrum = fft(filter)
    for i in range(len(spectrum)):
        if time_axis[i] > 300 and time_axis[i] < (N - 200):
            spectrum[i] = 0

    ax2.plot(spectrum.real)
    filter = ifft(spectrum)
    ax3.plot(freq_axis, abs(filter))

    ax4.plot(np.arange(len(sig)), sig)

    fourier_of_sig = fft(sig)
    ax5.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))

    fourier_of_sig = fourier_of_sig * abs(filter)

    ax6.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))

    filtered_sig = ifft(fourier_of_sig)

    ax7.plot(time_axis, filtered_sig)

    plt.show()



def LowPassFilter(sig, border):

    freq_axis = fftfreq(N)
    time_axis = np.arange(N)
    filter = np.zeros(len(freq_axis), dtype=complex)

    phase = 0


    for i in range(border):

        filter[i + len(freq_axis) - border] = cmath.rect(1, phase)
        filter[i] = cmath.rect(1, -phase)

        phase += 2 * cmath.pi / border

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(nrows=7, ncols=1, figsize=(12, 10))

    ax1.plot(freq_axis, abs(filter))
    ax1.set_xlabel('f, c')
    ax1.set_ylabel('U, мВ')

    spectrum = ifft(filter)
    # spectrum -= spectrum.imag * 1j
    # spectrum = abs(spectrum)

    for i in range(len(spectrum)):
        if time_axis[i] > 500 and (time_axis[i] < (time_axis[len(spectrum) - 1] - 500)):
            spectrum[i] = 0

    ax2.plot(np.arange(len(spectrum)), spectrum.real)
    ax2.set_xlabel('t, s')
    ax2.set_ylabel('U, мВ')

    filter = fft(spectrum)

    ax3.plot(freq_axis, abs(filter))
    ax3.set_xlabel('f, c')
    ax3.set_ylabel('U, мВ')

    ax4.plot(np.arange(len(sig)), sig)
    ax4.set_xlabel('t, c')
    ax4.set_ylabel('U, мВ')

    fourier_of_sig = fft(sig)

    ax5.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))
    ax5.set_xlabel('f, Гц')
    ax5.set_ylabel('U, мВ')

    fourier_of_sig = fourier_of_sig * abs(filter)

    ax6.plot(fftfreq(len(fourier_of_sig)), abs(fourier_of_sig))
    ax6.set_xlabel('f, Гц')
    ax6.set_ylabel('U, мВ')
    filtered_sig = ifft(fourier_of_sig)
    ax7.plot(np.arange(len(filtered_sig)), filtered_sig)
    ax7.set_xlabel('t, c')
    ax7.set_ylabel('U, мВ')

    plt.show()


if __name__ == '__main__':
    T = fftfreq(N)
    print(T)
    sig = np.asarray([6. * sin(t*100) + 2*sin(t*2000) + sin(t*300) +6. * sin(t*15) +  + 3*sin(t*3000) for t in T])
    # LowPassFilter(sig, 200)
    HighPassFilter(sig, 300)
    # BandPassFilter(sig, 200, 800)
