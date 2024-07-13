import pygame
import random
from settings import *

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
        self.color = (255, 255, 255)  # Default ball color

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def change_color(self, new_color):
        self.color = new_color

    def increase_speed(self):
        self.speed_x *= 1.05
        self.speed_y *= 1.05

    def reset_speed(self):
        self.speed_x = BALL_SPEED_X if self.speed_x > 0 else -BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y if self.speed_y > 0 else -BALL_SPEED_Y

    def random_direction(self):
        if random.random() < 0.1:  # 10% chance to change direction
            self.speed_x = -self.speed_x
