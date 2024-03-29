import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in a fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/alien.png').convert_alpha()
        self.rect = self.image.get_rect()

        #start each alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact x,y pos
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien to the screen at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """checks to see if an alien has reached the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    