import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    ai_settings = Settings()
   
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    play_button = Button(ai_settings,screen,"Play")
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    alien = Group()

    gf.create_fleet(ai_settings, screen, ship,alien)
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)

    while True:

        
        gf.check_events(ai_settings, screen,stats,play_button, ship,alien,   bullets)
        gf.update_screen(ai_settings, screen,stats,sb,ship, alien,bullets,play_button)  

        if stats.game_active:
            ship.update()
            bullets.update()
        #     #print(len(bullets))
           
            gf.update_bullets(ai_settings,screen,stats,sb,ship,alien,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,alien,bullets)
        
        
       
        

run_game()
