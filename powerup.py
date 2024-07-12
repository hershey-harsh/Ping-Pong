import pygame
from settings import *

class PowerUp:
    def __init__(self, x, y, type):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.type = type
        self.color = (0, 255, 0) if type == "speed" else (0, 0, 255) if type == "size" else (255, 0, 0)

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
