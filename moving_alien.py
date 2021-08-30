import pygame
from pygame.sprite import Sprite

class MovingAlien(Sprite):
    """A class to represent a single alien in a fleet"""
    def __init__(self, ai_settings, screen, x, y):
        """Initialize the alien and its starting position"""
        super(MovingAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/alien-ship.bmp').convert()
        self.rect = self.image.get_rect()

        #start each alien at the top left of the screen
        self.rect.x = x
        self.rect.y = y

        #Store the alien's exact x,y pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def blitme(self):
        """Draw the alien to the screen at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the moving alien"""
        self.x += .5
        self.y += .5
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """checks to see if an alien has reached the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
