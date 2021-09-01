import sys
from typing import Text
import pygame
import bullet as Bullet
from alien_bullet import AlienBullet
from shooting_alien import ShootingAlien
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import power_ups
from text_on_screen import TextOnScreen

def run_game():
    #initialize python, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height) )
    pygame.display.set_caption("Alien Invaders")

    #able to store game stats
    stats = GameStats(ai_settings)

    #Initialize instance of scoreboard
    scoreboard = Scoreboard(ai_settings, screen, stats)

    #make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets in
    bullets = Group()

    alien_bullets = Group()

    #Make a group to store aliens in
    aliens = Group()

    pow_ups = Group()

    clock = pygame.time.Clock()

    moving_aliens = Group()

    shooting_aliens = Group()

    textArray = []

    #Make a play button
    play_button = Button(ai_settings, screen, "Play!")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    gf.create_moving_fleet(ai_settings, screen, moving_aliens)

    gf.create_shooting_fleet(ai_settings, screen, shooting_aliens)
    
    pygame.mixer.init()
    #pygame.mixer.music.load("D:/Python_Projects/PythonGame1/Sounds/2019-12-09_-_Retro_Forest_-_David_Fesliyan.wav")
    #pygame.mixer.music.play(-1, 0.0)
    effect = pygame.mixer.Sound('D:/Python_Projects/PythonGame1/Sounds/WHO_IS_THIS.wav')
    effect.play(0)

    passes = 0

    bonus = 0

    textPasses = 0

    #start the loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets)
        if(len(textArray) == 0):
            textPasses = 0
        if(len(textArray) != 0):
            textPasses += 1
        passes += 1
        if stats.game_active == True:
            gf.update_smoke(ship, passes)
            ship.update()
            ship.update_smoke_color(passes)
            gf.update_text(textArray, textPasses)
            gf.update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, bullets, alien_bullets, shooting_aliens, pow_ups)
            gf.update_pow_ups(pow_ups, ship, ai_settings,screen, textArray)
            bonus = gf.update_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets, bonus)
            gf.update_moving_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets)
            gf.update_shooting_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, moving_aliens, shooting_aliens, alien_bullets)
        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, moving_aliens, shooting_aliens, bullets, alien_bullets, play_button, pow_ups, textArray)
        #cap the fps
        clock.tick(50)
        if passes > 4:
            passes = 0
        
        
run_game()
