import math
import cmath
import numpy
import matplotlib.pyplot as plt
import scipy.signal


def basic_furier(list_of_values):
    res_list = []
    i = complex('0+1j')
    for count1 in range(len(list_of_values)):
        res = 0
        for count2 in range(len(list_of_values)):
            res += list_of_values[count2] * cmath.exp(- 2 * math.pi * i * count1 * count2 / len(list_of_values))

        res_list.append(res)

    return res_list


def brsin_test():
    min_value = 0
    max_value = math.pi * 7 / 2
    point_amount = 100
    # _list = [math.sin(x * 0.1) for x in range(100)]
    # _list = [math.sin(x) for x in numpy.linspace(min_value, max_value, point_amount)]
    list1 = [math.sin(x) for x in numpy.linspace(min_value, math.pi, point_amount // 4)]
    list2 = [math.sin(x + math.pi / 4) for x in numpy.linspace(math.pi + math.pi / 25, math.pi * 4, point_amount * 3 // 4)]
    _list = list1 + list2
    # _list_windowed = _list * scipy.signal.windows.barthann(100, True)
    processed = basic_furier(_list)
    numpy_processed = numpy.fft.fft(_list)
    # windowed_processed = basic_furier(_list_windowed)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('My Tranformation')

    processed_amp = []
    processed_phase = []
    # windowed_amp = [abs(x) for x in windowed_processed]
    # windowed_phase = [cmath.phase(x) for x in windowed_processed]
    for ind in range(point_amount // 2):
        processed_amp.append(abs(processed[ind]))
        processed_phase.append(cmath.phase(processed[ind]))

    ax1.plot(numpy.linspace(min_value, max_value / 2, point_amount // 2), processed_amp, linewidth=1)
    ax2.plot(numpy.linspace(min_value, max_value / 2, point_amount // 2), processed_phase, linewidth=1)
    ax3.scatter(numpy.linspace(min_value, max_value, point_amount), _list)

    winfig, (winax1, winax2, winax3) = plt.subplots(1, 3)
    winfig.suptitle('Windowed Transformation')
    win_list = _list * scipy.signal.windows.barthann(point_amount)
    win_proc = basic_furier(win_list)
    win_amp = [abs(win_proc[x]) for x in range(len(win_proc) // 2)]
    win_phase = [cmath.phase(win_proc[x]) for x in range(len(win_proc) // 2)]

    winax1.scatter(numpy.linspace(min_value, max_value / 2, point_amount // 2), win_amp, s=9)
    winax2.plot(numpy.linspace(min_value, max_value / 2, point_amount // 2), win_phase, linewidth=1)
    winax3.scatter(numpy.linspace(min_value, max_value, point_amount), win_list)

    plt.show()


def longsin_test():
    max_number = math.pi * 2
    amount_of_points = 1000
    _list = [math.sin(40 * x) for x in numpy.linspace(0, max_number, amount_of_points)]
    myfur = basic_furier(_list)
    numfur = numpy.fft.fft(_list)
    diflist = [myfur[x] - numfur[x] for x in range(len(myfur))]
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('phase')
    ax1.plot(numpy.linspace(0, max_number, amount_of_points // 2), [cmath.phase(x) for x in myfur[: amount_of_points // 2]], linewidth=1)
    ax2.plot(numpy.linspace(0, max_number, amount_of_points // 2), [cmath.phase(x) for x in numfur[: amount_of_points // 2]], linewidth=1)
    ax3.scatter(numpy.linspace(0, max_number, len(diflist)), [cmath.phase(myfur[x]) - cmath.phase(numfur[x]) for x in range(len(myfur))], s=1)

    abfig, (abax1, abax2, abax3) = plt.subplots(1, 3)
    abfig.suptitle('amplitude')

    abax1.scatter(numpy.linspace(0, max_number / 2, amount_of_points // 2), [abs(x) for x in myfur[: amount_of_points // 2]], s=1)
    abax2.scatter(numpy.linspace(0, max_number / 2, amount_of_points // 2), [abs(x) for x in numfur[: amount_of_points // 2]], s=1)
    abax3.scatter(numpy.linspace(0, max_number, len(diflist)), [abs(x) for x in diflist], s=1)

    sigfig, sigax = plt.subplots()
    sigfig.suptitle = 'signal'
    sigax.plot(numpy.linspace(0, max_number, len(_list)), _list)
    plt.show()


if __name__ == '__main__':
    # brsin_test()
    longsin_test()
