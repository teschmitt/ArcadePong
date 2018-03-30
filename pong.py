import random
import arcade

from include.game_constants import *
from include.game_objects import Paddle, Ball


def make_ball():
    ball = Ball(
        velocity_x= 5, #random.randrange(-2, 3),
        velocity_y=random.randrange(-2, 3))
    return ball


class MyGame(arcade.Window):


    def __init__(self, width, height):
        super().__init__(width, height, 'Pong, muthafucka!')

        arcade.set_background_color(arcade.color.AMAZON)

        self.ball_list = []
        self.paddle_p1 = None
        self.paddle_p2 = None


    def check_hits(self, paddles, balls):
        hits = []
        for p in paddles:
            for b in balls:
                # check for hit to the right or left paddle
                if (b.x + b.size > p.x - p.width // 2 and \
                    p.x > b.x and (
                        b.y + b.size < p.y + p.height // 2 and \
                        b.y - b.size > p.y - p.height // 2) and \
                    b.velocity_x > 0) \
                    or \
                    (b.x - b.size < p.x + p.width // 2 and \
                    p.x < b.x and (
                        b.y + b.size < p.y + p.height // 2 and \
                        b.y - b.size > p.y - p.height // 2) and \
                    b.velocity_x < 0):
                    hits.append((b, p))
        return hits


    def setup(self):
        ball = make_ball()
        self.ball_list = [make_ball() for _ in range(5)]
        self.paddle_p1 = Paddle(color=arcade.color.RED, x=PADDLE_WIDTH // 2)
        self.paddle_p2 = Paddle(color=arcade.color.BLUE, x=SCREEN_WIDTH - (PADDLE_WIDTH // 2))


    def on_draw(self):
        arcade.start_render()

        for ball in self.ball_list:
            ball.draw()
        self.paddle_p1.draw()
        self.paddle_p2.draw()


    def update(self, delta_time):
        for ball in self.ball_list:
            ball.update()

        hits = self.check_hits([self.paddle_p1, self.paddle_p2], self.ball_list)
        if len(hits) > 0:
            for (ball, paddle) in hits:
                ball.update_velocity_after_hit(paddle)
        # self.paddle_p1.update()
        # self.paddle_p2.update()


    def on_key_press(self, key, key_modifiers):
        pass


    def on_key_release(self, key, key_modifiers):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.paddle_p2.y = y
        self.paddle_p2.velocity_y = dy



    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
