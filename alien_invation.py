import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    """ This Function initialises the Alien Invasion Game by importing all the preferences.!"""

    # Initializing the Pygame modules, Game Settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Making a Ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # Checking for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        # Updating the position of the Ship
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        # Updating the screen !
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # updating the screen with required settings


# Running the Game.
run_game()
