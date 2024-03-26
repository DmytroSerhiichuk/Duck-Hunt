import pygame
import sys
import program

from game import Game
from button import Button

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
        if program.BACKGROUND == 0:
            # Main menu background setup
            surface.blit(program.MENU_BACKGROUND, (0, 0))
            # Track down mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Finding screen center 
            screen_center_x = program.SCREEN_WIDTH // 2
            y = program.SCREEN_HEIGHT // 2

            #Setting up buttons
            start_button = Button(pos = (screen_center_x, y), text_input='Start', font = program.MAIN_FONT, 
                                  base_color=program.WHITE, howering_color=program.WHITISH)
            exit_button = Button(pos = (screen_center_x, y + program.MAIN_FONT_HEIGHT + 10),
                                  text_input='Exit', font=program.MAIN_FONT, base_color=program.WHITE, howering_color=program.WHITISH)
            
            for button in [start_button, exit_button]:
                button.changeColor(mouse_pos)
                button.update(surface)

            # Menu_Loop    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.checkForInput(mouse_pos):
                        program.BACKGROUND = 1
                    elif exit_button.checkForInput(mouse_pos):
                        sys.exit()
            pygame.display.update()

        elif program.BACKGROUND == 1:
            #Game loop
            if not game.is_game_over:
                for event in pygame.event.get():
                    # Handle quit
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # Handle Keyboard
                    elif event.type == pygame.KEYDOWN:
                        # Exit game
                        if event.key == pygame.K_ESCAPE:
                            program.BACKGROUND = 0
                        # Pause game
                        elif event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                            game.pause = not game.pause
                    # Check if the duck was hitb 
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        game.shoot()
            else:
                program.BACKGROUND = 0

            if not game.pause:
                # Draw background            
                surface.blit(program.GAME_BACKGROUND, (0, 0))

                # Update game
                game.update(surface)

                # Display game info
                game.display_info(surface)

                # Update screen
                pygame.display.update()
        # elif screen == 2:
        #     print("Gameover")

        

if __name__ == '__main__':
    main()