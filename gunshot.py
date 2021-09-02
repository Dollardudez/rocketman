import pygame

"""
This displays text to the screen, like when a player gets a powerup or 
when a player gets to a certain amount of points
"""
class Gunshot():

    #static image
    
    def __init__(self, screen, duration, ship):
        string = "D:/Python_Projects/AlienInvaders/Images/explosion/Explosion/"
        self.sprites = []
        self.sprites.append(pygame.image.load(string + '4.png'))
        self.sprites.append(pygame.image.load(string + '5.png'))
        self.sprites.append(pygame.image.load(string + '6.png'))
        self.sprites.append(pygame.image.load(string + '7.png'))
        self.sprites.append(pygame.image.load(string + '9.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        #initialize the ship and set its starting position
        self.screen = screen
        #load ship image
        self.screen_rect = screen.get_rect()
        self.duration = duration
        self.rect = self.image.get_rect()
        self.ship = ship
        #start each ship at the bottom of the screen
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top - 10
        
        # Store decimal values for ship's center.
        self.center = [float(self.rect.centerx), float(self.rect.centery)]
        #Movement flag

    
    def update(self, passes):
        if(self.duration < passes):
            return True
        self.current_sprite += .25
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.centerx = self.ship.rect.centerx
        self.rect.centery = self.ship.rect.top - 10
        return False
    

    def blitme(self):
        #Draw ship at its current location
        self.screen.blit(self.image, self.rect)

