import pygame
from settings import *

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.reversed_controls = False

    def move(self, up=True):
        if self.reversed_controls:
            up = not up
        
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        # Keep paddle within screen bounds
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

    def reverse_controls(self):
        self.reversed_controls = not self.reversed_controls

    def shrink(self):
        self.rect.height /= 1.5
