import pygame

"""
This displays text to the screen, like when a player gets a powerup or 
when a player gets to a certain amount of points
"""
class TextOnScreen():

    def __init__(self, text, screen, duration):
        #initialize the ship and set its starting position
        self.screen = screen
        #load ship image
        self.text = text
        self.screen_rect = screen.get_rect()
        self.text_color = (30, 30, 30)
        self.duration = duration
        self.text_size = 40
        self.font = pygame.font.SysFont(None, self.text_size)
        self.text_image = self.font.render(text, True, self.text_color)
        self.rect = self.text_image.get_rect()

        #start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 200
        
        # Store decimal values for ship's center
        self.center = [float(self.rect.centerx), float(self.rect.centery)]
        #Movement flag

    
    ##update ship's position based on the movement flag
    #update the ship's center value, not the rect
    def update(self):
        self.text_size += 1

    def delete_text(self):
        eraseText = self.font.render("", False, 0, (70, 12, 178))
        self.screen.blit(eraseText, self.rect)
    

    def blitme(self):
        #Draw ship at its current location
        self.screen.blit(self.text_image, self.rect)

