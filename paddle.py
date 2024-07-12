import pygame
from settings import *

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def increase_speed(self):
        self.speed *= 1.5

    def decrease_speed(self):
        self.speed /= 1.5

    def increase_size(self):
        self.rect.height *= 1.5

    def decrease_size(self):
        self.rect.height /= 1.5
