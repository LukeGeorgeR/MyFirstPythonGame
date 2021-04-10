import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    """ This Function initialises the Alien Invasion Game by importing all the preferences.!"""

    # Initializing the Pygame modules, Game Settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Making a Ship
    ship = Ship(screen)

    while True:
        # Fill the screen with color
        screen.fill(ai_settings.bg_color)
        # Redraw the Screen during each pass of the loop
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            pygame.display.flip()  # To update the display screen !


# Running the Game.
run_game()
