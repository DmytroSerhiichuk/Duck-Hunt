import pygame
import sys

import program

from game import Game
from duck import Duck

def main():
    # Init
    pygame.init()
    
    # Create surface
    surface = pygame.display.set_mode(flags=pygame.FULLSCREEN)

    # Init program properties
    program.init()

    # Set FPS
    clock = pygame.time.Clock()
    FPS = 60

    # Start render
    pygame.display.update()

    # Create game object
    game = Game()
    
    # Main loop
    while 1:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Handle quit
            if event.type == pygame.QUIT:
                sys.exit()
            # Handle Keyboard
            elif event.type == pygame.KEYDOWN:
                # Exit game
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                # Pause game
                elif event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    game.pause = not game.pause
            # Check if the duck was hit
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game.pause and not game.is_game_over:
                game.shoot()

        if not game.pause:
            # Draw background            
            surface.fill(program.BLUE)

            # Update game
            game.update(surface)

            # Display game info
            game.display_info(surface)

            # Update screen
            pygame.display.update()

        

if __name__ == '__main__':
    main()