import sys
import random
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien
from shooting_alien import ShootingAlien
from moving_alien import MovingAlien
from time import sleep
import power_ups
import random

def get_number_rows(ai_settings, ship_height, alien_height):
    """Find the number of rows that fit on a screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Get the number of aliens that can fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is eaqual to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
     #create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets):
    #respond to key presses and mouse clicks
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               # if key is pressed
               check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                #if key is released
                check_keyup_events(event, ship)
            elif event.type == pygame.K_q:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x)
                check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Hide the mouse
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        #clear all aliens and bullets
        aliens.empty()
        bullets.empty()

        scoreboard.prep_ships()
        scoreboard.show_score()
        #Create a new fleet and reset the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets, play_button, pow_ups):
    #redraw the screen with each pass through the loop
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    if(stats.game_active == True):
        moving_aliens.draw(screen)
        shooting_aliens.draw(screen)
        aliens.draw(screen)
        #redraw all bullets behind the ship
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        for bullet in alien_bullets.sprites():
            bullet.draw_bullet()

    pow_ups.draw(screen)
    #Draw scoreboard info
    scoreboard.show_score()

    if not stats.game_active:
        play_button.draw_button()
    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, bullets, alien_bullets, shooting_aliens, pow_ups):
    """Update position of bullets and get rid of old bullets"""
    # Get rid of bullets that have disappeared
    bullets.update()
    alien_bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in alien_bullets.copy():
        if bullet.rect.bottom >= 800:
            alien_bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, bullets, alien_bullets, shooting_aliens, pow_ups)

def check_bullet_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, bullets, alien_bullets, shooting_aliens, pow_ups):
    """When a bullet collides with an alien, both of the objects are destroyed"""
    randy = random.randint(0, 20)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    x = 0
    y = 0
    if collisions:
        effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/gross-sound-1.wav')
        effect.play(0)
        for bullet in collisions.keys():
            x = bullet.rect.x
            y = bullet.rect.y
        if randy == 7 or randy == 8:
            if randy % 2 == 0:
                create_gun_ups(ai_settings, screen, x, y, pow_ups, stats)
            if randy % 2 == 1:
                create_speed_ups(ai_settings, screen, x, y, pow_ups, stats)
        stats.score += ai_settings.alien_points
        scoreboard.prep_score()

    moving_collisions = pygame.sprite.groupcollide(bullets, moving_aliens, True, True)
    if moving_collisions:
        stats.score += ai_settings.moving_points
        scoreboard.prep_score()

    shooting_collisions = pygame.sprite.groupcollide(bullets, shooting_aliens, True, True)
    if shooting_collisions:
        stats.score += ai_settings.moving_points
        scoreboard.prep_score()

    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)

    if len(aliens) == 0:
        #destroy all bullets and create a new fleet
        bullets.empty()
        if ai_settings.alien_speed_factor < 2:
            ai_settings.alien_speed_factor += .1
        create_fleet(ai_settings, screen, ship, aliens)
        create_shooting_fleet(ai_settings, screen, shooting_aliens)

def ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets):
    """Respond to the user's ship getting hit by an alien ship"""
    #Destroy all aliens and bullets
    aliens.empty()
    bullets.empty()
    moving_aliens.empty()
    shooting_aliens.empty()
    alien_bullets.empty()

    if stats.ships_left > 0:
        if stats.ships_left == 3:
            effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/horse_meat_roy.wav')
            effect.play(0)
        if stats.ships_left == 2:
            effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/jeb_death_N.wav')
            effect.play(0)
        if stats.ships_left == 1:
            effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/horse_meat_roy.wav')
            effect.play(0)
        stats.ships_left -= 1
        sleep(2)
        effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/get_back_to_it_jeb.wav')
        effect.play(0)


        

        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        create_moving_fleet(ai_settings, screen, moving_aliens)
        create_shooting_fleet(ai_settings, screen, shooting_aliens)
        ship.center_ship()

        #Update number of ships on scoreboard
        scoreboard.prep_ships()

        #Pause the game
        sleep(3)
    else:
        effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/game_over.wav')
        effect.play(0)
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
def update_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets, bonus):
    """Update the position of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Check if any alien hits the bottom of the screen
    check_aliens_bottom(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)
    if stats.score >= 1000 and bonus == 0:
        bonus += 1
        effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/shit_yeah_boys.wav')
        effect.play(0)
    return bonus
        
    #scan for an alien colliding with the player's ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)

def create_moving_alien(ai_settings, screen, moving_aliens, x):
    """create an alien and place it in the row"""
    moving_alien = MovingAlien(ai_settings, screen, x, -200)
    moving_aliens.add(moving_alien)
    
def create_moving_fleet(ai_settings, screen, moving_aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is eaqual to one alien width
    #create the first row of aliens
    num_aliens = random.randrange(4, 8)
    x = random.randrange(-100, 10)
    for num in range(num_aliens):
        #create an alien and place it in the row
        create_moving_alien(ai_settings, screen, moving_aliens, x)
        x += 200

def update_moving_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets):
    """Update the position of all aliens in the fleet"""
    for moving_alien in moving_aliens:
        moving_alien.update()

    screen_rect = screen.get_rect()
    for alien in moving_aliens:
        if alien.rect.bottom >= screen_rect.bottom:
        #as if the ship got hit
            moving_aliens.empty()
            shooting_aliens.empty()
            create_moving_fleet(ai_settings, screen, moving_aliens)
            break

    if pygame.sprite.spritecollideany(ship, moving_aliens):
        ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)


def create_shooting_alien(ai_settings, screen, shooting_aliens, x, y):
    """create an alien and place it in the row"""
    shooting_alien = ShootingAlien(ai_settings, screen, x, y)
    shooting_aliens.add(shooting_alien)
    
def create_shooting_fleet(ai_settings, screen, shooting_aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is eaqual to one alien width
    #create the first row of aliens
    num_aliens = random.randrange(4, 8)
    y = random.randrange(-100, 10)
    x = random.randrange(-100, 10)
    for num in range(num_aliens):
        #create an alien and place it in the row
        create_shooting_alien(ai_settings, screen, shooting_aliens, x, y)
        y += 100
        x -= 15
        if y >= 650:
            break

def update_shooting_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, alien_bullets):
    """Update the position of all aliens in the fleet"""
    for shooting_alien in shooting_aliens:
        shooting_alien.update()
        if shooting_alien.fire_bullet() == 0:
            new_bullet = AlienBullet(ai_settings, screen, shooting_alien)
            alien_bullets.add(new_bullet)

    screen_rect = screen.get_rect()
    for shooting_alien in shooting_aliens:
        if shooting_alien.rect.right >= screen_rect.right:
        #as if the ship got hit
            shooting_aliens.remove(shooting_alien)
    if len(shooting_aliens) == 0:
        #as if the ship got hit
        create_shooting_fleet(ai_settings, screen, shooting_aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if the limit of bullets allowed on screen is not reached"""
    effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/science_fiction_laser_006.wav')
    effect.play(0)
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)  


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key-presses"""
    if event.key == pygame.K_d:
        #move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_a:
        #move ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create new bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets) 

"""Respond to key-releases"""
def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        #move ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_a:
        #move ship to the left
        ship.moving_left = False

def check_fleet_edges(ai_settings, aliens):
        """Respond if an alien has reached an edge"""
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
        #as if the ship got hit
            ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)
            break

def create_gun_ups(ai_settings, screen, x, y, pow_ups, stats):
    gun = power_ups.GunPowerup(screen, x, y, stats)
    pow_ups.add(gun)

def create_speed_ups(ai_settings, screen, x, y, pow_ups, stats):
    bolt = power_ups.SpeedPowerup(screen, x, y, stats)
    pow_ups.add(bolt)

def update_pow_ups(pow_ups, ship, ai_settings):
    pow_ups.update()
    collided_pow_up = pygame.sprite.spritecollideany(ship, pow_ups)
    if collided_pow_up:
        pow_ups.empty()
        if ai_settings.ship_speed_factor == 4:
                return
        if type(collided_pow_up) is power_ups.SpeedPowerup:
            ai_settings.ship_speed_factor += .25
            return
        if type(collided_pow_up) is power_ups.GunPowerup:
            return
        


