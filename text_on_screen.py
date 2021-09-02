import pygame

"""
This displays text to the screen, like when a player gets a powerup or 
when a player gets to a certain amount of points
"""
class TextOnScreen():

    def __init__(self, text, screen, duration, color):
        #initialize the ship and set its starting position
        self.screen = screen
        #load ship image
        self.text = text
        self.screen_rect = screen.get_rect()
        self.text_color = color
        self.duration = duration
        self.text_size = 40
        self.font = pygame.font.SysFont(None, self.text_size)
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.rect = self.text_image.get_rect()

        #start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 200
        
        # Store decimal values for ship's center.
        self.center = [float(self.rect.centerx), float(self.rect.centery)]
        #Movement flag

    
    def update(self, passes):
        if(self.duration < passes):
            return True
        if(passes < 15):

            self.text_size += 1
        self.rect.centery -= 2
        return False
    

    def blitme(self):
        #Draw ship at its current location
        self.screen.blit(self.text_image, self.rect)

