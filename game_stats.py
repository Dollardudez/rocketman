class GameStats():
    """ Track all the stats for Alien Invaders game"""
    def __init__(self, ai_settings):
        """initialize the game statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.number_of_gun_ups = 0
        self.number_of_speed_ups = 0