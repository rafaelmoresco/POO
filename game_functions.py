import sys
import pygame
from bullet import *

score = 0

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

def drawGUI(screen,gSettings,p1):
    barCoords = (0,gSettings.getHight()-100,gSettings.getWidth(),100)
    pygame.draw.rect(screen,(0,0,0),barCoords)

    if p1.getLife()>0:
        heart = pygame.image.load('images/vida.png')

        for i in range(p1.getLife()):
            screen.blit(heart,(64+(64*i)+(20*(i+1)),gSettings.getHight()-80,gSettings.getWidth(),100))

    if p1.getBombs() > 0:
        bomb = pygame.image.load('images/bomb.png')
        bombCoords = (392,gSettings.getHight()-70,gSettings.getWidth(),100)
        for i in range(p1.getBombs()):
            screen.blit(bomb,(392+(64*i)+(20*(i+1)),gSettings.getHight()-80,gSettings.getWidth(),100))

    font = gSettings.getGUIFont()
    text_surface = font.render("Score: %d" % (score),False,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (gSettings.getWidth()-200,gSettings.getHight()-50)
    screen.blit(text_surface,text_rect)

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
    drawGUI(screen,gSettings,p1)
    # Apresenta a ultima tela
    pygame.display.flip()

def updateBullets(bullets, enemies,soundController):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        global score
        score+=100
        soundController.playSound(1)

def updateEBullets(ebullets, p1):
    ebullets.update()

    for ebullet in ebullets.copy():
            if ebullet.rect.bottom <= 0 or ebullet.rect.top >= 720 or ebullet.rect.right <= 0 or ebullet.rect.left >= 960:
                ebullets.remove(ebullet)

    if pygame.sprite.spritecollideany(p1, ebullets) and (not p1.getHit()):
        p1.gotHit()
        bullet = pygame.sprite.spritecollideany(p1, ebullets)
        bullet.kill()

def updateEnemies(enemies, p1, ebullets):
    enemies.update(ebullets, p1)

    for enemy in enemies.copy():
             if enemy.rect.top >= 720:
                enemies.remove(enemy)
             if enemy.eType != 1 and enemy.eType!=2:
                if enemy.fired:
                    if enemy.rect.bottom <= 0:
                        enemies.remove(enemy)

    if pygame.sprite.spritecollideany(p1, enemies) and (not p1.getHit()):
        p1.gotHit()
        enemy = pygame.sprite.spritecollideany(p1, enemies)
        enemy.kill()

