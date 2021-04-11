class GameStats():
    """ Tracks the statistics for Alien Invation ."""

    def __int__(self, ai_settings):
        """ Initialising Stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialising stats that change during the game. """
        self.ships_left = self.ai_settings.ship_limit
        self.ship_limit = 3;