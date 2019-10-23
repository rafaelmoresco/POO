import sys
import pygame
from bullet import *
from enemy import Enemy

def checkEvents(p1, gSettings, screen, bullets):
    # Observa o teclado e mouse por eventos
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
                elif event.key == pygame.K_x:
                    p1.bomb()
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

def updateScreen(gSettings, screen, p1, bullets, enemies, ebullets):
     # Enche o fundo com cinza
    screen.fill(gSettings.getBgColour())
    p1.blitme()
    for bullet in bullets.sprites():
        bullet.drawBullet()
    for enemy in enemies.sprites():
        enemy.blitme()
    for ebullet in ebullets.sprites():
        ebullet.drawEBullet()
    # Apresenta a ultima tela
    pygame.display.flip()

def updateBullets(bullets, enemies):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)

def updateEBullets(ebullets, p1):
    ebullets.update()

    for ebullet in ebullets.copy():
            if ebullet.rect.bottom <= 0 or ebullet.rect.top >= 720 or ebullet.rect.right <= 0 or ebullet.rect.left >= 960:
                ebullets.remove(ebullet)

    if pygame.sprite.spritecollideany(p1, ebullets) and (not p1.getHit()):
        p1.gotHit()
        bullet = pygame.sprite.spritecollideany(p1, ebullets)
        bullet.kill()
