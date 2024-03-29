import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ Response to the Keyboard and Mouse Events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:  # Ship Controls
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ Update images on the Screen and flip to new screen in each passing loop ."""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    # Redraw the Screen during each pass of the loop
    ship.blitme()
    aliens.draw(screen)

    # Redraw all the bullets behind ship and alien.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw score information
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

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


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Updates position of the bullets and gets rid of old bullets"""
    bullets.update()
    # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check if any bullet has hit an alien,
    # If so, get rid of that alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()  # Destroy existing bullets, speed up game and create new fleet
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        # Increase Level
        stats.level += 1
        sb.prep_level()


def fire_bullets(ai_settings, screen, ship, bullets):
    """ Fire the bullet if th limit not reached yet. """
    # Create a bullet and add it to the bullet group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """ Determine the number of aliens that fit in the row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine the number of rows of alien that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Create a full fleet of aliens . """
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Alien(ai_settings, screen)  # Create and place the alien in the row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Update teh positions of all aliens in the fleet
    Check if the fleet is at the edge,
    and then update the positions of the aliens in the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """ Respond appropriately if any aliens have reached the edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Respond to ship hit by alien"""
    # Decrement ships left
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # update score board
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new Fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: # Treat this same as the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ Start a new game when player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and play_button.rect.collidepoint(mouse_x, mouse_y):
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats() # Reset the game statistics
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and the center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_high_score(stats, sb):
    """ Check to see if there's a new high score. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
