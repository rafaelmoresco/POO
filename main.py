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
    #Inicia o pygame
    pygame.init()
    #Cria settings
    gSettings = Settings()
    #Cria screen
    screen = pygame.display.set_mode((gSettings.getWidth(), gSettings.getHight()))
    #Define titulo da janela
    pygame.display.set_caption("Touhou Clone")
    #Cria jogador
    p1 = Player(gSettings, screen)
    #Cria bullet group
    bullets = Group()
    #Cria enemy group
    enemies = Group()
    #Cira enemy bullet group
    ebullets = Group()
    #Inicia o loop principal do jogo.
    while True:
        gf.checkEvents(p1, gSettings, screen, bullets)
        gf.updateScreen(gSettings, screen, p1, bullets, enemies, ebullets)
        p1.update(bullets)
        gf.updateBullets(bullets, enemies)
        ebullets.update()
        enemies.update(ebullets, p1)
        m += 1
        if m == 999:
            new_enemy = Enemy( gSettings, screen, 3, 300, p1)
            enemies.add(new_enemy)
            m = 0
 
    for ebullet in ebullets.copy():
        if ebullet.rect.bottom <= 0 or ebullet.rect.top >= 720 or ebullet.rect.right <= 0 or ebullet.rect.left >= 960:
            ebullets.remove(ebullet)
    for enemy in enemies.copy():
         if enemy.rect.bottom <= 0 or enemy.rect.top >= 720 or enemy.rect.right <= 0 or enemy.rect.left >= 960:
            enemy.remove(enemies)
            print(len(enemies))

        

run_game()
