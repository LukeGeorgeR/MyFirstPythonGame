import pygame
class Ship():
    def __init__(self,ai_settings, screen):
        """ Initializing the Ship at it's starting Position"""
        self.screen = screen
        self.ai_settings = ai_settings


        # Load the ship image and it's starting Position and rect    
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom centre of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        print(self.center)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's positon based on the movement flag."""
        # Update the Ship's Center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)


