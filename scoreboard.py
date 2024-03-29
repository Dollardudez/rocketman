import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.prep_ships()

        #Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Display the score at the top-right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)

        #Draw ships
        self.ships.draw(self.screen)

    def prep_ships(self):
        """How many ships are left"""
        self.ships = Group()
        for ships_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ships_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)