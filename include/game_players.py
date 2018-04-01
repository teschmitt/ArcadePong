import random
import arcade

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
