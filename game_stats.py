class GameStats:
    """ Tracks the statistics for Alien Invasion ."""

    def __init__(self, ai_settings):
        """ Initialising Stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialising stats that change during the game. """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1