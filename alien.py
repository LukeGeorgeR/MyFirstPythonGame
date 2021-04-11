import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initializing the alien and settings its starting position. """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/ALIEN_small.png")
        self.rect = self.image.get_rect()

        # Start the alien near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the alien at the current location"""
        self.screen.blit(self.image, self.rect)
