import arcade
import math
import numpy

class Charge:
    x = 0.0
    y = 0.0
    z = 0.0
    charge = 0.0

    def __init__(self, x, y, z, charge):
        self.x = x
        self.y = y
        self.charge = charge


class PotentialCalculator:
    charges = []
    x_size = 0
    y_size = 0
    pot_factor = 1.0
    factor_changed = True

    def __init__(self, chargelist, x_size, y_size, pot_factor=1000.0):
        self.charges = chargelist
        self.x_size = x_size
        self.y_size = y_size
        self.pot_factor = pot_factor

    def draw(self):
        for i in range(self.x_size):
            for j in range(self.y_size):
                potential = 0
                for charge in self.charges:
                    dist = math.sqrt((charge.x - i)**2 + (charge.y - j)**2 + charge.z**2)
                    if dist == 0:
                        potential = 0
                        break
                    potential += self.pot_factor * charge.charge / (math.sqrt((charge.x - i)**2 + (charge.y - j)**2))
                if potential > 0:
                    arcade.draw_point(float(i), float(j), [abs(int(potential) % 256), 0, 0], 1.0)
                else:
                    arcade.draw_point(float(i), float(j), [0, 0, abs(int(potential) % 256)], 1.0)
        # arcade.finish_render()
        self.factor_changed = False


class Chwin(arcade.Window):
    potcalc = None
    change_made = True

    def __init__(self, win_width, win_height, name, chargelist):
        super().__init__(win_width, win_height, name)
        self.potcalc = PotentialCalculator(chargelist, win_width, win_height)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.potcalc.pot_factor += 10000

        elif symbol == arcade.key.LEFT:
            self.potcalc.pot_factor -= 10000

        self.change_made = True

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        arcade.start_render()
        self.potcalc.draw()
        self.change_made = False

    def update(self, delta_time: float):
        pass


if __name__ == '__main__':
    chargelist = []
    for i in range(50, 350, 20):
        chargelist += [Charge(i, 200, x, 1) for x in range(-5, 5, 1)]
    for i in range(50, 350, 20):
        chargelist += [Charge(i, 250, x, -1) for x in range(-5, 5, 1)]
    # chargelist = [Charge(199, 200, 0, 1), Charge(201, 200, 0, -1)]
    # charges = [Charge(100, 100, -10, 1), Charge(100, 110, 10, -1)]
    # pc = PotentialCalculator(charges, 400, 400)
    # pc.draw()
    # arcade.run()
    win = Chwin(400, 400, 'potcalc', chargelist)
    arcade.run()
