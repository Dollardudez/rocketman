import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, x, rot):
        """Create a bullet object from the ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet react at (0, 0) then set correct position
        self.surface = pygame.Surface((ai_settings.bullet_width, ai_settings.bullet_height), pygame.SRCALPHA).convert_alpha()
        self.surface.fill((30, 30, 30))
        self.rotatedSurface = pygame.transform.rotate(self.surface, rot).convert_alpha()
        self.rect = self.rotatedSurface.get_rect()
        self.rect.centerx = x.rect.centerx
        

        self.rect.top = x.rect.top

        #Store the bullet's position as a decimal
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color

    #def gun_level_one():
         

    def update(self):
        """Move bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #Update the rect position
        self.rect.y = self.y
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.Surface.blit( self.screen,self.rotatedSurface, self.rect)