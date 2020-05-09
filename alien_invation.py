import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from time import sleep
def run_game():
    """This is what that starts the entire game"""
    #Initialize game,settings and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invation")

    # MAke a Ship, a group of bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens. 
    gf.create_fleet(ai_settings, screen,ship, aliens)
    #Start the main loop for the Game.

    while True:

        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)
run_game()

