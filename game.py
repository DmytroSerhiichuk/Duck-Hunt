import pygame
import program
from duck import Duck

class Game:
    def __init__(self) -> None:
        self.current_duck = Duck(self.handle_duck_leave)
        self.last_duck_removing_time = 0
        self.__TIME_TO_NEXT_DUCK = 2000

        self.pause = False

        self.is_game_over = False

        # Level properties
        self.level = 1
        self.remaining_ducks = 10
        self.missed_ducks = 0
        self.__MAX_MISSES = 5
        self.__MAX_BULLETS_COUNT = 3
        self.bullets_count = self.__MAX_BULLETS_COUNT

        self.score = 0

    def update(self, surface) -> None:
        if self.current_duck != None:
            self.current_duck.move()
        # Друга перевірка потрібна для уникнення помилки, після того, як качка вилетіла
        if self.current_duck != None:
            self.current_duck.draw(surface)
        elif pygame.time.get_ticks() - self.last_duck_removing_time >= self.__TIME_TO_NEXT_DUCK:
            self.add_new_duck()


    def handle_duck_leave(self) -> None:
        self.missed_ducks += 1

        # Check if user lost
        if self.missed_ducks >= self.__MAX_MISSES:
            self.is_game_over = True
            return
        
        self.remove_duck()

    def handle_hit(self) -> None:
        self.score += 1000

        self.remove_duck()

    def handle_miss(self) -> None:
        self.bullets_count -= 1

        # Remove duck if bullets are over
        if self.bullets_count == 0:
            self.current_duck.immediately_leave()


    def remove_duck(self) -> None:
        del self.current_duck
        self.current_duck = None
        self.remaining_ducks -= 1

        self.last_duck_removing_time = pygame.time.get_ticks()

        if self.remaining_ducks == 0:
            self.update_level()

        self.bullets_count = self.__MAX_BULLETS_COUNT

    def update_level(self) -> None:
        self.level += 1
        self.remaining_ducks = 10
        self.missed_ducks = 0

        self.score += 1500

    def add_new_duck(self) -> None:
        self.current_duck = Duck(self.handle_duck_leave)
        

    def shoot(self) -> None:
        if self.bullets_count > 0 and not self.pause and not self.is_game_over and self.current_duck != None:
            mouse_pos = pygame.mouse.get_pos()
            if self.current_duck.is_mouse_over(mouse_pos):
                self.handle_hit()
            else:
                self.handle_miss()


    def display_info(self, surface) -> None:
        # TODO: Create UI for game info
        
        infos = [
            f'Level: {self.level}', 
            f'Bullets: {self.bullets_count}', 
            f'Remaining Ducks: {self.remaining_ducks}',
            f'Misses: {self.missed_ducks}',
            f'Score: {self.score}'
        ]

        x_offset = program.SCREEN_WIDTH * 0.05
        y_main_offset = program.SCREEN_HEIGHT - len(infos) * program.MAIN_FONT_HEIGHT
        y_secondary_offset = 0

        for info in infos:
            text = program.MAIN_FONT.render(info, True, program.WHITE)
            surface.blit(text, (x_offset, y_main_offset + y_secondary_offset))
            y_secondary_offset += program.MAIN_FONT_HEIGHT