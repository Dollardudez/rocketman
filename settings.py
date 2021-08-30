class Settings():
    #a class to store all settings for alien invasion
    def __init__(self):
        #initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed_factor = 1.5
        self.ships_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.alien_bullet_color = 18, 178, 87
        self.bullets_allowed = 15

        # Alien settings
        self.alien_speed_factor = .7
        self.fleet_drop_speed = 10
        #direction of 1 = right, direction -1 = left
        self.fleet_direction = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Scoring
        self.alien_points = 25
        self.moving_points = 50