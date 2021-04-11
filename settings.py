class Settings:
    """ This Class contains all the settings required for the Alien Invasion Game !"""

    def __init__(self):
        """ Initializing the settings for the Game."""

        # Screen Settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (51, 204, 255)

        # Ship Settings
        self.ship_speed_factor = 2.0

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
