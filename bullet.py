import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, x, rot, l_r_c):
        """Create a bullet object from the ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.flightpath = l_r_c
        #Create a bullet react at (0, 0) then set correct position
        self.surface = pygame.Surface((ai_settings.bullet_width, ai_settings.bullet_height), pygame.SRCALPHA).convert_alpha()
        self.surface.fill((30, 30, 30))
        self.rotatedSurface = pygame.transform.rotate(self.surface, rot).convert_alpha()
        self.rect = self.rotatedSurface.get_rect()
        self.rect.centerx = x.rect.centerx
        
        self.move_x = self.__fix_flightpath()
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
        self.x += self.speed_factor * self.move_x
        #Update the rect position
        self.rect.y = self.y
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.Surface.blit( self.screen,self.rotatedSurface, self.rect)

    def __fix_flightpath(self):
        if(self.flightpath == "left"):
            return -.66
        elif(self.flightpath == "center"):
            return 0
        elif(self.flightpath == "right"):
            return .66
        elif(self.flightpath == "leftest"):
            return -1
        elif(self.flightpath == "rightest"):
            return 1
        elif(self.flightpath == "slightleft"):
            return -.7
        elif(self.flightpath == "slightright"):
            return .7
        elif(self.flightpath == "centerleft"):
            return -.66
        elif(self.flightpath == "centerright"):
            return .66
        else:
            return 0