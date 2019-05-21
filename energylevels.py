import matplotlib.pyplot as plt
import numpy as np
import math

N = 10**2
h = 1.0545837 * 10**-34
m = 1.573554 * 10**(-27)
aBor = 0.74155 * (10**(-10)) #m
a0 = aBor/(2**(1/6))
a0 = 0.660744*10**-10
U0 = 7.595 * 10**-19 #J/mol

GAMMA = a0/(h) * math.sqrt(m * U0)
#GAMMA = 22
RANGE = [1/1.02,1*2.9]


STEP = 1/N



def potention(r):
    return 4*((1/r)**12 - (1/r)**6)

def pot_sqrt(r, callable):
    return (-1 * callable(r))**(1/2)

def parabolic_potentioal(r):
    return (r - 2)**2 - 1


def simpson_uniform(x, f):

    N = len(x) - 1
    h = np.diff(x)

    result = 0.0
    for i in range(1, N, 2):
        hph = h[i] + h[i - 1]


        result += (4 * f[i] + f[i -1] + f[i + 1]) * hph / 6

    return result


def find_root(func,leftX,rightX,accur):
    while abs(rightX - leftX) > accur:
        a = func(leftX)
        b = func(rightX)
        if (a*b > 0):
            return 1
        if a == 0:
            return a
        if b == 0:
            return b
        if ((func((leftX + rightX)/2)*a) <= 0):
            rightX = (leftX + rightX)/2
        elif((func((leftX + rightX)/2)*b) <= 0):
            leftX = (leftX + rightX)/2;
        else:
            print("incorect leftX and right X")
            break
    return (leftX + rightX)/2


def findX1X2(E):
    y1 = 1/2 + 1/2*((1+E)**(1/2))
    y2 = 1/2 - 1/2*((1+E)**(1/2))
    x1 = 1/(y1)**(1/6)
    x2 = 1/(y2)**(1/6)
    return [x1,x2]

def parafindX1X2(E):
    pass

def toIntegrate(E,x):
    return (E - potention(x))**(1/2)

def kvantovanie(n, callable):
    def func(E):
        x1,x2 = findX1X2(E)
        toIntVal = [(pot_sqrt(r, callable)) for r in np.arange(x1,x2,STEP)]
        toIntArg = np.arange(x1,x2,STEP)
        integrall = simpson_uniform(toIntArg,toIntVal)
        val = GAMMA*integrall - n - 1/2
        return val
    return func


if __name__ == '__main__':
    potVal = [potention(r) for r in np.arange(RANGE[0],RANGE[1],STEP)]
    potArg = np.arange(RANGE[0],RANGE[1],STEP)

    fig, (ax1) = plt.subplots(
        nrows=1, ncols=1,
        figsize=(8, 8)
    )

    print('Gamma = ', GAMMA)

    ax1.plot(potArg,potVal)

    x1, x2 = findX1X2(-0.0001)
    toIntVal = [(r) for r in np.arange(x1, x2, STEP)]
    toIntArg = np.arange(x1, x2, STEP)
    integrall = simpson_uniform(toIntArg, toIntVal)
    max_n_val = int(round(integrall - 0.5))

    print('maximum level = ', max_n_val)

    # TODO тест на параболе!

    for n in range (max_n_val):
        func = kvantovanie(n, potention)
        root = find_root(func,-1 + STEP,0 - STEP,STEP)
        print(root)
        x1,x2 = findX1X2(root)
        funcArg = np.linspace(x1,x2,2)
        funcVal = [root for r in funcArg]
        ax1.plot(funcArg,funcVal)





    ax1.set_title('Scatter: $x$ versus $y$')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')

    plt.show()