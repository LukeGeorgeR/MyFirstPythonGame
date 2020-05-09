class Settings():
    """A Class to store all settings for Alen Invation.."""

    def __init__(self):
        """ This is initializing class for the Game Settings """
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800 
        self.bg_color = (255,255,255)

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right, -1 represents letf
        self.fleet_direction = 1
    


