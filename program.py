import pygame

# Constants

WORLD_WIDTH = 0
WORLD_HEIGHT = 0

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
SCREEN_ASPECT_RATIO = 0

SCREEN_TO_WORLD_RATIO = 0

# Fonts
MAIN_FONT = None
MAIN_FONT_HEIGHT = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 191, 255)
WHITISH = (190, 190, 190)

# Backgrounds 

BACKGROUND = 0

GAME_BACKGROUND = None
MENU_BACKGROUND = None

def init() -> None:
    global WORLD_WIDTH, WORLD_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_ASPECT_RATIO, SCREEN_TO_WORLD_RATIO
    global MAIN_FONT, MAIN_FONT_HEIGHT
    global GAME_BACKGROUND, MENU_BACKGROUND

    info = pygame.display.Info()

    SCREEN_WIDTH = info.current_w 
    SCREEN_HEIGHT = info.current_h
    SCREEN_ASPECT_RATIO = SCREEN_WIDTH / SCREEN_HEIGHT

    WORLD_WIDTH = 1
    WORLD_HEIGHT = 1 / SCREEN_ASPECT_RATIO

    SCREEN_TO_WORLD_RATIO = SCREEN_WIDTH / WORLD_WIDTH

    MAIN_FONT = pygame.font.Font(None, 36)
    MAIN_FONT_HEIGHT = 40

    GAME_BACKGROUND = pygame.transform.scale(
        pygame.image.load('./assets/game_background.jpg'), 
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    MENU_BACKGROUND = pygame.transform.scale(
        pygame.image.load('./assets/main_menu_background.jpg'), 
        (SCREEN_WIDTH, SCREEN_HEIGHT))

def world_to_screen(x, y):
    return (x * SCREEN_TO_WORLD_RATIO, y * SCREEN_TO_WORLD_RATIO)

