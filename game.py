import pygame
from settings import *
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle2 = Paddle(SCREEN_WIDTH - 45, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.paddle1.rect.top > 0:
            self.paddle1.move(up=True)
        if keys[pygame.K_s] and self.paddle1.rect.bottom < SCREEN_HEIGHT:
            self.paddle1.move(up=False)
        if keys[pygame.K_UP] and self.paddle2.rect.top > 0:
            self.paddle2.move(up=True)
        if keys[pygame.K_DOWN] and self.paddle2.rect.bottom < SCREEN_HEIGHT:
            self.paddle2.move(up=False)

        self.ball.update()
        self.check_collision()

    def check_collision(self):
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.speed_x = -self.ball.speed_x

        if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.speed_x = -self.ball.speed_x
            self.ball.rect.x, self.ball.rect.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
