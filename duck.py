import pygame
import program
import random

class Duck:
    def __init__(self, leaving_callback, falling_callback, level, difficult) -> None:
        self.width = 0.05
        self.height = 0.05
        
        # TODO: chande to image
        self.surface = pygame.Surface(program.world_to_screen(self.width, self.height))
        self.surface.fill(program.WHITE)
        
        # generate pathes
        self.generate_start_position()
        self.generate_path()

        # move properties
        self.speed = 0.001
        self.__LEVEL_SPEED_COEFFICIENT = 0.002 * level
        # Values: 0.9 -> Easy; 1.0 -> Normal (Medium); 1.1 - Hard
        self.__DIFFICULT_SPEED_COEFFICIENT = difficult
        self.__FALLING_SPEED = 0.005
        self.last_node_index = 0
        self.distance = 0

        self.is_falling = False

        # callbacks
        self.leave = leaving_callback
        self.fall = falling_callback

        self.rect = self.surface.get_rect(topleft=program.world_to_screen(self.current_position.x, self.current_position.y))

    def draw(self, surface) -> None:
        surface.blit(self.surface, program.world_to_screen(self.current_position.x, self.current_position.y))

    def move(self) -> None:
        if self.last_node_index < len(self.path) - 1:
            start = self.path[self.last_node_index]
            end = self.path[self.last_node_index + 1]

            vec = end - start
            
            dir = vec.normalize()
            length = vec.magnitude()

            speed = 0

            if self.is_falling:
                speed = self.__FALLING_SPEED
            else:
                speed = (self.speed + self.__LEVEL_SPEED_COEFFICIENT) * self.__DIFFICULT_SPEED_COEFFICIENT

            self.distance += speed
            next_position = self.current_position + dir * speed

            if self.distance >= length :
                self.current_position = end
                self.last_node_index += 1
                self.distance = 0
            else:
                self.current_position = next_position
        elif self.is_falling:
            self.fall()
        else:
            self.leave()


    def generate_start_position(self) -> None:
        x_offset = (program.WORLD_WIDTH * 0.2)

        self.current_position = pygame.math.Vector2((
            random.uniform(x_offset, program.WORLD_WIDTH - x_offset), 
            program.WORLD_HEIGHT / 2 - self.height / 2
        ))

    def generate_path(self) -> None:
        self.path = []

        # Offsets
        x_offset = (program.WORLD_WIDTH * 0.2)
        y_bottom_offset = (program.WORLD_HEIGHT / 2 - program.WORLD_HEIGHT * 0.1)
        y_top_offset = (program.WORLD_HEIGHT * 0.1)

        # Add Start node
        self.path.append(pygame.math.Vector2(
            self.current_position.x,
            self.current_position.y
        ))

        # Add path nodes
        for node in range(4):
            self.path.append(pygame.math.Vector2(
                random.uniform(x_offset, program.WORLD_WIDTH - x_offset), 
                random.uniform(y_top_offset, y_bottom_offset)
        ))

        # Add final node
        self.path.append(pygame.math.Vector2(
            random.uniform(x_offset, program.WORLD_WIDTH - x_offset),
            0 - self.height
        ))
    
    def is_mouse_over(self, mouse_pos) -> bool:
        duck_rect = pygame.Rect(program.world_to_screen(self.current_position.x, self.current_position.y), program.world_to_screen(self.width, self.height))
        return duck_rect.collidepoint(mouse_pos)

    # Updates the duck's path
    def update_path_leave(self) -> None:
        self.path = [
            pygame.math.Vector2(self.current_position.x, self.current_position.y),
            pygame.math.Vector2(self.current_position.x, 0 - self.height)
        ] 
        self.distance = 0
        self.last_node_index = 0

    def update_path_fall(self) -> None:
        self.path = [
            pygame.math.Vector2(self.current_position.x, self.current_position.y),
            pygame.math.Vector2(self.current_position.x, program.WORLD_HEIGHT / 2 - self.height / 2)
        ] 
        self.distance = 0
        self.last_node_index = 0

        self.is_falling = True
