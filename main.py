import pygame
import sys

import program

from game import Game

def main():
    # Init
    pygame.init()
    
    # Create surface
    surface = pygame.display.set_mode(flags=pygame.FULLSCREEN)

    # Init Screen properties
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
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        # Draw background
        surface.fill((0, 0, 0))

        # Update game
        game.update(surface)
        
        # Update screen
        pygame.display.update()
        

if __name__ == '__main__':
    main()