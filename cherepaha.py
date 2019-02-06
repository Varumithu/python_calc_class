import random
import graphics

from graphics import Line
from graphics import Point


class Cherepaha:
    x = 0.0
    y = 0.0
    speed = 1.0


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
    graphwin = graphics.GraphWin()
    turtles = []
    random.seed()
    for i in range(amount):
        turtles.append(Cherepaha())
        turtles[i].x = random.uniform(0.0, 10.0)
        turtles[i].y = random.uniform(0.0, 10.0)
        if i > 0:
            turtles[i - 1].tracked = turtles[i]
    turtles[amount - 1].tracked = turtles[0]
    for i in range(100):

        # simulation steps

        for j in turtles:
            oldx = j.x
            oldy = j.y
            cherepaha_step(j)
            aline = graphics.Line(Point(oldx, oldy), Point(j.x, j.y))
            aline.draw(graphwin)
    while input() != 'q':
        pass


cherepaha_sim(10)
