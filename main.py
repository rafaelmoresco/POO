import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy

def run_game():
    k = 0
    l = 0
    m = 0
    # Initialize game and create a screen object.
    pygame.init()
    #Create settings
    gSettings = Settings()
    #Create screen
    screen = pygame.display.set_mode((gSettings.getWidth(), gSettings.getHight()))
    #Set Screen title
    pygame.display.set_caption("Touhou Clone")
    #Create player
    p1 = Player(gSettings, screen)
    #Create bullet group
    bullets = Group()
    #Create enemy group
    enemies = Group()
    # Start the main loop for the game.
    while True:
        gf.checkEvents(p1, gSettings, screen, bullets)
        gf.updateScreen(gSettings, screen, p1, bullets, enemies)
        p1.update(bullets)
        bullets.update()
        enemies.update()
        k += 1
        l += 1
        m += 1
        if k == 200:
            new_enemy = Enemy(gSettings, screen, 1, gSettings.getWidth()/2)
            enemies.add(new_enemy)
            k = 0
        if l == 1500:
            new_enemy = Enemy(gSettings, screen, 2, 650)
            enemies.add(new_enemy)
            l = 0
        if m == 999:
            new_enemy = Enemy( gSettings, screen, 3, 300)
            enemies.add(new_enemy)
            m = 0

        

run_game()
