import random
import arcade
import math
from operator import itemgetter

from .game_constants import *


class Player:

    def __init__(self, paddle, points=0):
        self.paddle = paddle
        self.points = points

    @property
    def paddle(self):
        return self.__paddle

    @paddle.setter
    def paddle(self, paddle):
        self.__paddle = paddle

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points


class HumanPlayer(Player):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComputerPlayer(Player):

    def __init__(self, speed=DEFAULT_OPPONENT_SPEED, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def get_nearest_ball(self, ball_list):
        # get distance of all balls moving towards paddle
        # store them as a list of tuples (Ball, distance from paddle middle)
        c = [(b, math.sqrt((b.x - self.paddle.x)**2 + (b.y - self.paddle.y)**2)) for b in ball_list if b.velocity_x < 0]
        if len(c) > 0:
            nearest_ball = sorted(c, key=itemgetter(1))[0][0]
            return nearest_ball
        else:
            # kinda lazy right now
            # if there are no balls moving towards its paddle,
            # it will just follow ball nr 0
            return ball_list[0]

    def react(self, ball_list):
        if len(ball_list) > 0:
            nearest_ball = self.get_nearest_ball(ball_list)
            self.paddle.move_to(y=nearest_ball.y)
        else:
            self.paddle.move_to(y=0)
