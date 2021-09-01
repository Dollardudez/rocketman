import pygame

"""
This displays text to the screen, like when a player gets a powerup or 
when a player gets to a certain amount of points
"""
class TextOnScreen():

    def __init__(self, text, screen, duration):
        #initialize the ship and set its starting position
        self.screen = screen
        #load ship image
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)

        #start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal values for ship's center
        self.center = float(self.rect.centerx)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    ##update ship's position based on the movement flag
    #update the ship's center value, not the rect
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center
    

    def blitme(self):
        #Draw ship at its current location
        self.screen.blit(self.text, self.rect)

    def center_ship(self):
        """Put the ship onto the center of the screen"""
        self.center = self.screen_rect.centerx
