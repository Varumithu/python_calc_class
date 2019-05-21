import random
import time
import math
import arcade
from numba import jit


g = 9.8


class Object:
    x = 0.0
    y = 0.0
    time_ratio = 1.0
    image = None

    def step(self):
        pass

    def draw(self):
        pass


class Shard(Object):
    radius = 2.0
    x_speed = 0.0
    y_speed = 0.0

    def __init__(self, x, y, x_speed, y_speed, time_ratio):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.time_ratio = time_ratio

    @jit
    def step(self):
        self.x += self.x_speed * self.time_ratio
        self.y += self.y_speed * self.time_ratio
        self.y_speed -= g * self.time_ratio
        if self.y <= 0:
            self.x_speed = 0
            self.y_speed = 0
            return 1

        return 0

    @jit
    def draw(self):
        self.image = arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.SPANISH_CRIMSON)


class Rocket(Object):
    max_height = 600
    radius = 10.0
    speed = 100.0
    shard_amount = 50
    next_rocket = None

    @jit
    def step(self):
        if self.y >= self.max_height:
            if self.next_rocket is not None:
                self.next_rocket.speed = self.speed

            return 3  # explolsion
        self.y += self.speed * self.time_ratio
        return 0

    @jit
    def draw(self):
        self.image = arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.SPANISH_CRIMSON)


@jit
def graphics_draw(shards_arr):
    arcade.start_render()
    for shard in shards_arr:
        shard.draw()

    arcade.finish_render()


@jit
def explosion_simulation(amount=5, init_y=600, init_x=400, time_ratio=0.1):
    shardlist = []
    random.seed()
    shard_speed = 20.0
    for i in range(amount):
        shardlist.append(Rocket())
        shardlist[i].time_ratio = time_ratio
        shardlist[i].x = 950 * i / amount + 100
        shardlist[i].speed = 0
        if i > 0:
            shardlist[i].next_rocket = shardlist[i - 1]

    shardlist[0].next_rocket = shardlist[len(shardlist) - 1]
    shardlist[0].speed = 100.0

    while len(shardlist) > 0:
        graphics_draw(shardlist)
        to_be_removed = []
        for shard in shardlist:
            if shard.y < 0:
                to_be_removed.append(shard)
            if shard.step() == 3:
                for ind in range(shard.shard_amount):
                    # theta = random.uniform(0, math.pi)
                    # phi = random.uniform(0, math.pi * 2)
                    while True:
                        spx = random.uniform(-1.0, 1.0)
                        spy = random.uniform(-1.0, 1.0)
                        spz = random.uniform(-1.0, 1.0)
                        absquared = spx**2 + spy**2 + spz**2
                        if absquared <= 1:
                            break

                    spx = shard_speed * spx / math.sqrt(absquared)
                    spy = shard_speed * spy / math.sqrt(absquared)
                    radius = random.randint(1, 4)
                    shardlist.append(Shard(shard.x, shard.y,
                                           # math.sin(theta) * math.cos(phi) * shard_speed,
                                           # math.sin(theta) * math.sin(phi) * shard_speed,
                                           spx, spy,
                                           time_ratio))
                    shardlist[len(shardlist) - 1].radius = radius
                shardlist.remove(shard)
        for shard in to_be_removed:
            shardlist.remove(shard)

        to_be_removed.clear()


if __name__ == '__main__':
    arcade.open_window(1000, 800, 'fireworks')
    explosion_simulation()











