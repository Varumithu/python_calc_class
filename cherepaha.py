import random
import graphics
import time
import math

from graphics import Line
from graphics import Point


class Cherepaha:
    x = 0.0
    y = 0.0
    speed = 1.0
    delta_x = 0
    delta_y = 0
    time_ratio = 0.1
    tracked = None
    point = None

    def __init__(self, x=0.0, y=0.0, speed=1.0, ratio=0.1):
        self.x = x
        self.y = y
        self.speed = speed
        self.time_ratio = ratio

    def step(self):
        self.x += self.delta_x
        self.y += self.delta_y

        start_x = self.x
        start_y = self.y

        x_diff = self.tracked.x - start_x
        y_diff = self.tracked.y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.delta_x = math.cos(angle) * self.speed * self.time_ratio
        self.delta_y = math.sin(angle) * self.speed * self.time_ratio

        if x_diff ** 2 + x_diff ** 2 < self.speed ** 2 * self.time_ratio:  # #condition  close
            return True
        else:
            return False


Cherepaha.tracked = Cherepaha()


def cherepaha_arrange_random(amount, second_to_time_unit_ratio=0.01):
    _turtles = []
    for i in range(amount):
        _turtles.append(Cherepaha(random.uniform(0.0, 1000.0), random.uniform(0.0, 1000.0),
                                  3.0, second_to_time_unit_ratio))
        if i > 0:
            _turtles[i - 1].tracked = _turtles[i]

    _turtles[amount - 1].tracked = _turtles[0]
    return _turtles


def cherepaha_arrange_circle(amount, second_to_time_unit_ratio=0.01, radius=10.0):
    _turtles = []
    for i in range(amount):
        _turtles.append(Cherepaha(radius * math.cos(2 * math.pi * i / amount),
                                  radius * math.sin(2 * math.pi * i / amount),
                                  3.0, second_to_time_unit_ratio))
        if i > 0:
            _turtles[i - 1].tracked = _turtles[i]

    _turtles[amount - 1].tracked = _turtles[0]
    return _turtles


def cherepaha_sim(amount, second_to_time_unit_ratio=1.0):
    graphwin = graphics.GraphWin('Cherepaha', 900, 700)
    random.seed()
    size_scaling_factor_x = 1
    size_scaling_factor_y = 1
    size_shift_x = 200
    size_shift_y = 200
    turtles = cherepaha_arrange_random(amount, second_to_time_unit_ratio)
    # turtles = cherepaha_arrange_circle(amount, second_to_time_unit_ratio, 3000.0)
    time_spent = 0
    while True:
        all_turtles_together = True
        # simulation steps
        for j in turtles:
            if j.point is not None:
                j.point.undraw()

            if not j.step():
                all_turtles_together = False

            j.point = Point((j.x + size_shift_x) * size_scaling_factor_x,
                  (j.y + size_shift_y) * size_scaling_factor_y).draw(graphwin)

        if all_turtles_together:
            break
        time_spent += second_to_time_unit_ratio
        # time.sleep(0.1)
    # graphwin.getKey()
    print(time_spent)


if __name__ == '__main__':
    cherepaha_sim(20, 0.1)
