import pygame
from duck import Duck

class Game:
    def __init__(self) -> None:
        self.current_duck = Duck(self.handle_duck_leave)
        self.pause = False

    def update(self, surface) -> None:
        self.current_duck.move()
        self.current_duck.draw(surface)

    def handle_duck_leave(self) -> None:
        del self.current_duck
        self.current_duck = Duck(self.handle_duck_leave)