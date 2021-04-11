import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """ Response to the Keyboard and Mouse Events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # Ship Controls
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Update images on the Screen and flip to new screen in each passing loop ."""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    # Redraw the Screen during each pass of the loop
    ship.blitme()
    aliens.draw(screen)
    # Redraw all the bullets behind ship and alien.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recent screen visible and to update the display screen!
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Response to the KeyPresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit(1)


def check_keyup_events(event, ship):
    """ Response to Key Releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """ Updates position of the bullets and gets rid of old bullets"""
    bullets.update()
    # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))


def fire_bullets(ai_settings, screen, ship, bullets):
    """ Fire the bullet if th limit not reached yet. """
    # Create a bullet and add it to the bullet group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """ Create a full fleet of aliens . """
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)  # Create and place the alien in the row.
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
