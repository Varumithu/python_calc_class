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

    def step(self):
        self.x += self.delta_x
        self.y += self.delta_y

        start_x = self.x
        start_y = self.y

        x_diff = self.tracked.x - start_x
        y_diff = self.tracked.y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.delta_x = math.cos(angle) * self.speed
        self.delta_y = math.sin(angle) * self.speed


Cherepaha.tracked = Cherepaha()


def cherepaha_step(cherepaha: Cherepaha):
    delta_x = cherepaha.tracked.x - cherepaha.x
    delta_y = cherepaha.tracked.y - cherepaha.y
    hypotenuse = (delta_x ** 2 + delta_y ** 2) ** 0.5
    vel_x = cherepaha.speed * (hypotenuse / delta_x)
    vel_y = cherepaha.speed * (hypotenuse / delta_y)
    cherepaha.x += vel_x
    cherepaha.y += vel_y


def cherepaha_sim(amount):
    graphwin = graphics.GraphWin('Cherepaha', 400, 400)
    turtles = []
    random.seed()
    for i in range(amount):
        turtles.append(Cherepaha())
        turtles[i].x = random.uniform(0.0, 100.0)
        turtles[i].y = random.uniform(0.0, 100.0)
        if i > 0:
            turtles[i - 1].tracked = turtles[i]
    turtles[amount - 1].tracked = turtles[0]
    for i in range(100):

        # simulation steps

        for j in turtles:
            # oldx = j.x
            # oldy = j.y
            j.step()
            # aline = Line(Point(oldx, oldy), Point(j.x, j.y))
            # aline.draw(graphwin)
            Point(j.x, j.y).draw(graphwin)
        time.sleep(0.1)
    graphwin.getKey()


cherepaha_sim(10)
