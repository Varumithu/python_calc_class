import arcade
import random
import button
import math
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Balls"
SPEED = 1

class Ball:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.change_x = 1
        self.change_y = 1
        self.radius = 10
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
        self.follow = None  # ссылка на другой объект, за кем нужно следовать

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        start_x = self.x
        start_y = self.y

        x_diff = self.follow.x - start_x
        y_diff = self.follow.y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * SPEED
        self.change_y = math.sin(angle) * SPEED

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.ball_list = []
        self.pause = True
        self.mouse_x = None
        self.mouse_y = None
        self.button_list = []
        self.background = arcade.load_texture("image/grass.jpg")

    def setup(self):
        play_button = button.StartTextButton(60, 570, self.resume_program)
        self.button_list.append(play_button)

        quit_button = button.StopTextButton(60, 515, self.pause_program)
        self.button_list.append(quit_button)


    def pause_program(self):
        self.pause = True

    def resume_program(self):
        self.pause = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        for button in self.button_list:
            button.draw()

        for ball in self.ball_list:
            ball.draw()

        output = "Balls: {}".format(len(self.ball_list))
        coordinate_x = "X: {}".format(self.mouse_x)
        coordinate_y = "Y: {}".format(self.mouse_y)
        arcade.draw_text(coordinate_x, 10, 50, arcade.color.WHITE, 14)
        arcade.draw_text(coordinate_y, 10, 70, arcade.color.WHITE, 14)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        if self.pause :
            return

        for ball in self.ball_list:
            ball.update()
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.radius:
                ball.change_x *= -1

            if ball.y < ball.radius:
                ball.change_y *= -1

            if ball.x > SCREEN_WIDTH - ball.radius:
                ball.change_x *= -1

            if ball.y > SCREEN_HEIGHT - ball.radius:
                ball.change_y *= -1

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_press(self, x, y, button_, modifiers):
        if button.check_mouse_press_for_buttons(x, y, self.button_list):
            return

        ball = Ball(self.mouse_x, self.mouse_y)
        if len(self.ball_list) != 0:
            ball.follow = self.ball_list[-1]
            self.ball_list[0].follow = ball
        else:
            ball.change_x = 0
            ball.change_y = 0
        self.ball_list.append(ball)


    def on_mouse_release(self, x, y, button_, key_modifiers):
        button.check_mouse_release_for_buttons(x, y, self.button_list)


def main():
    win = Window()
    win.setup()
    arcade.run()

if __name__ == "__main__":
    main()