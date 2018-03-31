import random
import arcade

from include.game_constants import *
from include.game_objects import Paddle, Ball


def make_ball(paddles=[]):
    vel_x = random.randrange(-400, 401) / 100
    if vel_x > 0:
        vel_x += 2
    else:
        vel_x -= 2
    ball = Ball(
        velocity_x = vel_x,
        velocity_y = random.randrange(-500, 501) / 100,
        paddles=paddles
    )
    return ball


class MyGame(arcade.Window):


    def __init__(self, width, height):
        super().__init__(width, height, 'ArcadePong!')
        self.set_update_rate(1/60)

        arcade.set_background_color(arcade.color.AMAZON)

        self.ball_list = []
        self.paddle_p1 = None
        self.paddle_p2 = None
        self.object_list = []

    def get_kills (self, balls):
        for b in balls:
            if b.x > SCREEN_WIDTH + BALL_KILL_THRESH or \
                    b.x < -BALL_KILL_THRESH:
                yield b


    def setup(self):
        self.paddle_p1 = Paddle(color=arcade.color.RED, x=PADDLE_WIDTH // 2)
        self.paddle_p2 = Paddle(color=arcade.color.BLUE, x=SCREEN_WIDTH - (PADDLE_WIDTH // 2))
        paddles = [self.paddle_p1, self.paddle_p2]
        self.ball_list = [make_ball(paddles=paddles) for _ in range(5)]
        self.object_list = paddles + self.ball_list


    def on_draw(self):
        arcade.start_render()

        for obj in self.object_list:
            obj.draw()

        if DEBUG:
            self.debug_output()


    def update(self, delta_time):
        for ball in self.ball_list:
            ball.update()

        for b in self.get_kills(self.ball_list):
            self.ball_list.remove(b)
            self.object_list.remove(b)


    def on_key_press(self, key, key_modifiers):
        pass


    def on_key_release(self, key, key_modifiers):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.paddle_p2.move_to(y, dy)

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

    def debug_output(self):
        arcade.draw_text(f'Paddle2 velocity: {self.paddle_p2.velocity_y}', 800, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f'Number of balls in game: {len(self.ball_list)}', 800, 40, arcade.color.WHITE, 14)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
