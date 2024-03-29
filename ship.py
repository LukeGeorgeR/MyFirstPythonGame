import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """ Initialising the ship and it's position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/ship_final.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Start the ship at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Storing the decimal value of the ship's center
        self.center = float(self.rect.centerx)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Draw the Ship at the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Updating the ship position based on the Movement Flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        # update rect object from self.center
        # self.rect.centerx = self.center

    def center_ship(self):
        """ Center the ship on the screen ."""
        self.center = self.screen_rect.centerx
