import sys
import pygame
from bullet import PBullet
from enemy import Enemy

def checkEvents(p1, gSettings, screen, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Key Down events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    p1.sm = True
                elif event.key == pygame.K_RIGHT:
                    p1.mr = True
                elif event.key == pygame.K_LEFT:
                    p1.ml = True
                elif event.key == pygame.K_UP:
                    p1.mu = True
                elif event.key == pygame.K_DOWN:
                    p1.md = True
                elif event.key == pygame.K_z:
                    p1.fi = True
            #Key Up events
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    p1.sm = False
                elif event.key == pygame.K_RIGHT:
                    p1.mr = False
                elif event.key == pygame.K_LEFT:
                    p1.ml = False
                elif event.key == pygame.K_UP:
                    p1.mu = False
                elif event.key == pygame.K_DOWN:
                    p1.md = False
                elif event.key == pygame.K_z:
                    p1.fi = False

def updateScreen(gSettings, screen, p1, bullets, enemies):
     # Fill backgrouns with grey
    screen.fill(gSettings.getBgColour())
    p1.blitme()
    for bullet in bullets.sprites():
        bullet.drawBullet()
    for enemy in enemies.sprites():
        enemy.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()