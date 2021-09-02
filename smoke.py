import pygame
from pygame.sprite import Sprite


class Smoke(Sprite):
    """smoke behind the ship"""

    def __init__(self, screen, ship, ai_settings):
        """Create a smoke object from the ship's position"""
        super(Smoke, self).__init__()
        self.screen = screen
        self.ship_speed = ai_settings.ship_speed_factor
        #Create a bullet react at (0, 0) then set correct position
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.centerx = ship.rect.centerx
        
        self.rect.top = ship.rect.bottom
        self.ship = ship

        #Store the bullet's position as a decimal
        self.y = float(self.rect.y)

        self.speed_factor = 2
        self.color = pygame.Color(242, 243, 244)
        self.radius = 12

    def update(self):
        """Move bullet up the screen"""
        self.y += self.speed_factor
        #Update the rect position
        self.rect.y = self.y
        

    def update_color(self):
        colorsTuple = self.__update_color_by_speed()
        if(self.radius >= 0):
            self.radius -= colorsTuple[0]
        if(self.color.r > colorsTuple[4]):
            self.color.r -= colorsTuple[1]
        if(self.color.g > colorsTuple[5]):
            self.color.g -= colorsTuple[2]
        if(self.color.b > colorsTuple[6]):
            self.color.b -= colorsTuple[3]

    def __update_color_by_speed(self):
        if(self.ship_speed > 11):
            return (.4, 1, 30, 30, 10, 90, 100)
        elif(self.ship_speed > 10):
            return (.5, 1, 30, 30, 10, 90, 100)
        elif(self.ship_speed > 9):
           return (.55, 10, 0, 9, 20, 255, 26)
        elif(self.ship_speed > 8):
            return (.6, 0, 20, 0, 255, 30, 255)
        elif(self.ship_speed > 7):
            return (.8, 1, 30, 30, 10, 90, 100)
        
        else:
            return (1, 10, 15, 7, 70, 8, 178)

    def draw_smoke(self):
        """Draw bullet on screen"""
        pygame.draw.circle(self.screen, self.color, [self.rect.centerx, self.rect.centery], self.radius)