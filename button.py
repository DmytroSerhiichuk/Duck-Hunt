class Button():
    def __init__(self, pos, text_input, font, base_color, howering_color):

        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.font = font
        self.base_color = base_color
        self.howering_color = howering_color
        self.text_input = text_input
        
        self.text = self.font.render(text_input, True, self.base_color)
        self.rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, surface):
        """
        Renders the button on the screen

        Params:
        - surface: screen surface
        """
        surface.blit(self.text, self.rect)
    
    def checkForInput(self, position):
        """
        Checks if the mouse is over the button 

        Params:
        - position: mouse position

        Returns:
        - bool: The value of whether the mouse is over the button
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        """
        Sets the color of the button

        Params:
        - position: mouse position
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.howering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)