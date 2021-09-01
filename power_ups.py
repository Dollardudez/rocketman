import pygame
from pygame.sprite import Sprite


class GunPowerup(Sprite):
    """represents a gun power up in the game"""
    def __init__(self, screen, x, y, stats):
        super(GunPowerup, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/gun-power-up.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = float(self.rect.y)
        self.screen_rect = screen.get_rect()

    def update(self):
        """Drop the powerup"""
        if(self.rect.y > self.screen_rect.y + 100):
            self.y += .5
            self.rect.y = self.y

    def blitme(self):
        #Draw power up at its current location
        self.screen.blit(self.image, self.rect)

class SpeedPowerup(Sprite):
    """represents a lightning power up in the game"""
    def __init__(self, screen, x, y, stats):
        super(SpeedPowerup, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/lightning-bolt.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = float(self.rect.y)
        self.screen_rect = screen.get_rect()
        self.stats = stats

    def update(self):
        """Move theh powerup down"""
        if(self.rect.y > self.screen_rect.y + 100):
            self.y += .5
            self.rect.y = self.y

    def blitme(self):
        #Draw power up at its current location
        self.screen.blit(self.image, self.rect)

    
        