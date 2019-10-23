import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy
from level import Level

def run_game():
    #Inicia o pygame
    pygame.init()
    #Cria settings
    gSettings = Settings()
    #Cria screen
    screen = pygame.display.set_mode((gSettings.getWidth(), gSettings.getHight()))
    #Define titulo da janela
    pygame.display.set_caption("Touhou Clone")
    #Cria bullet group
    bullets = Group()
    #Cria enemy group
    enemies = Group()
    #Cira enemy bullet group
    ebullets = Group()

    #Cria jogador
    p1 = Player(gSettings, screen,enemies)

    level = Level(screen,gSettings,enemies,p1)

    #Inicializa a sequência de spawn
    #Parametros (em ordem):
        #Formação (0 = spawnLados, 1 = spawnMeioS)
        #Quantas linhas de inimigos
        #Distancia horizontal entre inimigos, se estiverem na formação spawnLados
        #Distância vertical entre inimigos/quanto tempo demoram para entrar na tela
    cont = 0
    spawnQueue = []
    spawnQueue.append([0,1,2,50,500])
    spawnQueue.append([0,3,1,100,200])
    spawnQueue.append([0,4,3,50,100])
    spawnQueue.append([1,1,2,50,500])
    spawnQueue.append([1,3,1,50,200])
    spawnQueue.append([1,4,3,50,100])

    clock = pygame.time.Clock()
    fps = gSettings.getFPS()

    #Inicia o loop principal do jogo.
    while True:
        clock.tick(fps)

        gf.checkEvents(p1, gSettings, screen, bullets)
        gf.updateScreen(gSettings, screen, p1, bullets, enemies, ebullets)
        p1.update(bullets)
        gf.updateBullets(bullets,enemies)
        gf.updateEBullets(ebullets, p1)
        enemies.update(ebullets, p1)

        for enemy in enemies.copy():
             if enemy.rect.top >= 720:
                enemies.remove(enemy)
             if enemy.eType != 1 and enemy.eType!=2:
                if enemy.fired:
                    if enemy.rect.bottom <= 0:
                        enemies.remove(enemy)

        if len(enemies) == 0 and cont < len(spawnQueue):
                level.decodeSpawn(spawnQueue[cont])
                cont+=1

run_game()
