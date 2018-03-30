import random
import arcade

from .game_constants import *


class Paddle:

    def __init__(
            self,
            width=PADDLE_WIDTH, height=PADDLE_INITIAL_LENGTH,
            color=arcade.color.WHITE,
            x=0, y=SCREEN_HEIGHT // 2,
            velocity_x=0, velocity_y=0):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


class Ball:

    def __init__(
            self,
            size=BALL_SIZE,
            color=arcade.color.WHITE,
            x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
            velocity_x=0, velocity_y=0):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update_velocity_after_hit(self, paddle):
        self.reverse_velocity_x()
        self.velocity_y += paddle.velocity_y // 4         # Todo: Change this to a sloped delta with max of 10 or smth

    def reverse_velocity_x(self):
        self.velocity_x = -self.velocity_x

    def reverse_velocity_y(self):
        self.velocity_y = -self.velocity_y

    def update(self):
        if (self.y + self.size + self.velocity_y > SCREEN_HEIGHT and self.velocity_y > 0) \
                or (self.y - self.size + self.velocity_x < 0 and self.velocity_y < 0):
            self.reverse_velocity_y()
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
