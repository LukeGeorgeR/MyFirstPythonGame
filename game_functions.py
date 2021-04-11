import sys
import pygame


def check_events(ship):
    """ Response to the Keyboard and Mouse Events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # Ship Controls
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """ Update images on the Screen and flip to new screen in each passing loop ."""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    # Redraw the Screen during each pass of the loop
    ship.blitme()
    # Make the most recent screen visible and to update the display screen!
    pygame.display.flip()
