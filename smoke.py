import pygame
from pygame.sprite import Sprite


class Smoke(Sprite):
    """smoke behind the ship"""

    def __init__(self, screen, ship, ai_settings):
        """Create a smoke object from the ship's position"""
        super(Smoke, self).__init__()
        self.screen = screen

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
        if(self.radius >=0):
            self.radius -= .5
        if(self.color.r > 70):
            self.color.r -= 10
        if(self.color.g > 8):
            self.color.g -= 20
        if(self.color.b > 178):
            self.color.b -= 5

    def draw_smoke(self):
        """Draw bullet on screen"""
        pygame.draw.circle(self.screen, self.color, [self.rect.centerx, self.rect.centery], self.radius)