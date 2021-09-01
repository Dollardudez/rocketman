import pygame
from pygame.sprite import Sprite, Group
from smoke import Smoke

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        #initialize the ship and set its starting position
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #load ship image
        self.image = pygame.image.load('D:/Python_Projects/PythonGame1/Images/rocket.bmp')
        #make a rect out of the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom

        self.smoke_stack = Group()

        
        # Store decimal values for ship's center
        self.center = [float(self.rect.centerx), float(self.rect.centery)]
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    ##update ship's position based on the movement flag
    #update the ship's center value, not the rect
    def update(self):
        self.smoke_stack.update()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center[0]
        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center[0]
        if self.moving_up and self.rect.y > 0:
            self.center[1] -= self.ai_settings.ship_speed_factor
            self.rect.centery = self.center[1]
        if self.moving_down and self.rect.y < 756:
            self.center[1] += self.ai_settings.ship_speed_factor
            self.rect.centery = self.center[1]

        #update rect object from self.center
        
    def generate_smoke(self, x):
        if x == 4:
            smoke = Smoke(self.screen, self, self.ai_settings)
            self.smoke_stack.add(smoke)
        return

    def update_smoke_color(self, x):
        if x == 4:
            for smoke in self.smoke_stack:
                smoke.update_color()
        return
    

    def blitme(self):
        #Draw ship at its current location
        for smoke in self.smoke_stack:
            smoke.draw_smoke()
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put the ship onto the center of the screen"""
        self.center = [self.screen_rect.centerx, self.screen_rect.bottom]
