import pygame
from settings import *
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle2 = Paddle(SCREEN_WIDTH - 45, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
        self.score1 = 0
        self.score2 = 0
        self.paused = False
        self.game_over = False
        self.show_start_screen = True

    def start_new_game(self):
        self.score1 = 0
        self.score2 = 0
        self.ball.rect.x, self.ball.rect.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        self.ball.speed_x = BALL_SPEED_X if self.ball.speed_x > 0 else -BALL_SPEED_X
        self.ball.speed_y = BALL_SPEED_Y if self.ball.speed_y > 0 else -BALL_SPEED_Y
        self.game_over = False
        self.show_start_screen = False

    def update(self):
        if self.show_start_screen or self.paused or self.game_over:
            return

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

        if self.ball.rect.left <= 0:
            self.score2 += 1
            self.ball.rect.x, self.ball.rect.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            self.ball.speed_x = BALL_SPEED_X
            self.ball.speed_y = BALL_SPEED_Y

        if self.ball.rect.right >= SCREEN_WIDTH:
            self.score1 += 1
            self.ball.rect.x, self.ball.rect.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            self.ball.speed_x = -BALL_SPEED_X
            self.ball.speed_y = BALL_SPEED_Y

        if self.score1 >= WINNING_SCORE or self.score2 >= WINNING_SCORE:
            self.game_over = True

    def pause(self):
        self.paused = not self.paused

    def reset(self):
        self.__init__(self.screen)

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        if self.show_start_screen:
            self.draw_start_screen()
        elif self.game_over:
            self.draw_game_over_screen()
        else:
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_scores()
            if self.paused:
                self.draw_pause_screen()

    def draw_scores(self):
        score_text = self.font.render(f"{self.score1} - {self.score2}", True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    def draw_start_screen(self):
        start_text = self.font.render("Press SPACE to Start", True, (255, 255, 255))
        self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - start_text.get_height() // 2))

    def draw_game_over_screen(self):
        winner_text = self.font.render(f"{'Player 1' if self.score1 >= WINNING_SCORE else 'Player 2'} Wins!", True, (255, 255, 255))
        restart_text = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + winner_text.get_height() // 2))

    def draw_pause_screen(self):
        pause_text = self.font.render("Paused", True, (255, 255, 255))
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - pause_text.get_height() // 2))
