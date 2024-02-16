import pygame
from duck import Duck

class Game:
    def __init__(self) -> None:
        self.current_duck = Duck(self.handle_duck_leave)

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
        self.current_duck.move()
        self.current_duck.draw(surface)


    def handle_duck_leave(self) -> None:
        self.missed_ducks += 1

        # Check if user lost
        if self.missed_ducks >= self.__MAX_MISSES:
            self.is_game_over = True
            return
        
        self.remove_duck()
        self.add_new_duck()

    def handle_hit(self) -> None:
        self.score += 1000

        self.remove_duck()
        self.add_new_duck()

    def handle_miss(self) -> None:
        self.bullets_count -= 1

        # Remove duck if bullets are over
        if self.bullets_count == 0:
            self.handle_duck_leave()


    def remove_duck(self) -> None:
        del self.current_duck
        self.remaining_ducks -= 1

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
        mouse_pos = pygame.mouse.get_pos()
        if self.current_duck.is_mouse_over(mouse_pos):
            self.handle_hit()
        else:
            self.handle_miss()