import pygame
import sys

import program

from game import Game

def main():
    # Setting game difficult from arguments
    difficult = 1 # default value -> 1 (normal)

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '1' or arg.lower() == 'easy':
            difficult = 0.9
        elif arg == '2' or arg.lower() == 'medium' or arg.lower() == 'normal':
            difficult = 1
        elif arg == '3' or arg.lower() == 'hard':
            difficult = 1.1
        else:
            raise Exception('argument error') 

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
    game = Game(difficult)
    
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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