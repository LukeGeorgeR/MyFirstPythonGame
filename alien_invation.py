import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """ This Function initialises the Alien Invasion Game by importing all the preferences.!"""

    # Initializing the Pygame modules, Game Settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Making a Ship
    ship = Ship(ai_settings, screen)

    while True:
        # Checking for keyboard and mouse events
        gf.check_events(ship)

        # Updating the position of the Ship
        ship.update()
        # Updating the screen !
        gf.update_screen(ai_settings, screen, ship)  # updating the ship and the screen with required settings


# Running the Game.
run_game()
