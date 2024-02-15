import pygame
from pygame._sdl2 import Window
import sys

def main():
    # Init
    pygame.init()
    pygame.display.set_mode((1080, 720), flags=pygame.RESIZABLE)

    # Maximize window
    Window.from_display_module().maximize()

    # Set FPS
    clock = pygame.time.Clock()
    FPS = 60

    # Start render
    pygame.display.update()
    
    while 1:
        clock.tick(FPS)
    
        for i in pygame.event.get():
            # Handle quit
            if i.type == pygame.QUIT:
                sys.exit()
        
        # Update screen
        pygame.display.update()


if __name__ == '__main__':
    main()