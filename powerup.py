import pygame
from settings import *

class PowerUp:
    def __init__(self, x, y, type):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.type = type
        self.color = self.get_color()

    def get_color(self):
        if self.type == "speed":
            return (0, 255, 0)
        elif self.type == "size":
            return (0, 0, 255)
        elif self.type == "ball_speed":
            return (255, 0, 0)
        elif self.type == "reverse":
            return (255, 255, 0)
        elif self.type == "shrink":
            return (255, 0, 255)
        elif self.type == "extra_life":
            return (0, 255, 255)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def apply(self, game):
        if self.type == "speed":
            game.paddle1.increase_speed()
            game.paddle2.increase_speed()
        elif self.type == "size":
            game.paddle1.increase_size()
            game.paddle2.increase_size()
        elif self.type == "ball_speed":
            game.ball.increase_speed()
        elif self.type == "reverse":
            game.paddle1.reverse_controls()
            game.paddle2.reverse_controls()
        elif self.type == "shrink":
            game.paddle1.shrink()
            game.paddle2.shrink()
        elif self.type == "extra_life":
            game.add_life()
