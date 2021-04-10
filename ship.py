import pygame


class Ship:
    def __init__(self, screen):
        """ Initialising the ship and it's position"""
        self.screen = screen
        self.image = pygame.image.load("images/ship_final.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ship at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Draw the Ship at the current location"""
        self.screen.blit(self.image, self.rect)
