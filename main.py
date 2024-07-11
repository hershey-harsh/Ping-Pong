import pygame
from settings import *
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    game = Game(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.pause()
                if event.key == pygame.K_r:
                    game.reset()
                if event.key == pygame.K_SPACE:
                    if game.show_start_screen or game.game_over:
                        game.start_new_game()
                    elif game.paused:
                        game.pause()

        game.update()
        game.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
