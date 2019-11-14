import sys
import pygame
from bullet import *
from explosion import Explosion

score = 0
highScore = 0

def initGUI(gSettings,screen):
    global overlay
    overlay = pygame.image.load('images/overlay.png').convert_alpha(screen)

    global heart
    heart = pygame.image.load('images/vida.png').convert_alpha(screen)

    global bomb
    bomb = pygame.image.load('images/bomb.png').convert_alpha(screen)

    global font
    font = gSettings.getGUIFont()
    screen_width = gSettings.getWidth()
    screen_Height = gSettings.getHight()

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

def drawGUI(screen,gSettings,p1,enemies):
    screen.blit(overlay,(0,0))

    if p1.getLife()>0:
        for i in range(p1.getLife()):
            screen.blit(heart,(700+(64*i)+(5*(i+1)),100,gSettings.getWidth(),100))

    if p1.getBombs() > 0:
        for i in range(p1.getBombs()):
            screen.blit(bomb,(700+(64*i)+(5*(i+1)),270,gSettings.getWidth(),100))

    scoreText = ("%010d" % (score))
    highScoreText = ("%010d" % (highScore))
    inimigos = ("%d" % (len(enemies)))

    drawText("Score:",gSettings,screen,810,370)
    drawText(scoreText,gSettings,screen,810,410)

    drawText("High Score:",gSettings,screen,810,490)
    drawText(highScoreText,gSettings,screen,810,530)

    drawText("Inimigos:",gSettings,screen,810,610)
    drawText(inimigos,gSettings,screen,805,650)

    drawText("Vida:",gSettings,screen,810,70)
    drawText("Bombas:",gSettings,screen,810,240)

def drawText(texto,gSettings,screen,x,y):
    text_surface = font.render(texto,False,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)

def updateScreen(gSettings, screen, p1, bullets, enemies, ebullets,bg,clouds,explosions,bossGroup,bbullets):
    bg.blitme()

    for cloud in clouds:
        cloud.blitme()

    p1.blitme()
    for bullet in bullets.sprites():
        bullet.drawBullet()
    for enemy in enemies.sprites():
        enemy.blitme()
    for ebullet in ebullets.sprites():
        ebullet.drawEBullet()
    for explosion in explosions.sprites():
        explosion.blitme()
    for boss in bossGroup.sprites():
        boss.blitme()
    for bbullet in bbullets.sprites():
        bbullet.drawBBullet()
    drawGUI(screen,gSettings,p1,enemies)
    # Apresenta a ultima tela
    pygame.display.flip()

def updateBg(bg,clouds):
    for cloud in clouds.sprites():
        cloud.update()

def updateExplosions(explosions):
    for explosion in explosions:
        explosion.update()

def updateBullets(bullets, enemies,soundController,screen, explosions):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 23 or bullet.rect.top >= 675 or bullet.rect.right <= 46 or bullet.rect.left >= 646:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for col in collisions:
            new_explosion = Explosion(screen,col.rect.centerx,col.rect.centery,70,7,0)
            explosions.add(new_explosion)
            addScore()
        soundController.playSound(1)
    '''if pygame.sprite.spritecollideany(bullets, bossGroup):
        boss = pygame.sprite.spritecollideany(bullets, bossGroup)
        boss.hit()
        bullet = pygame.sprite.spritecollideany(bossGroup, bullets)
        bullet.kill()'''

def addScore():
    global score
    score+=100

def updateEBullets(ebullets, p1):
    ebullets.update()

    for ebullet in ebullets.copy():
            if ebullet.rect.bottom <= 23 or ebullet.rect.top >= 675 or ebullet.rect.right <= 46 or ebullet.rect.left >= 646:
                ebullets.remove(ebullet)

    if pygame.sprite.spritecollideany(p1, ebullets) and (not p1.getHit()):
        p1.gotHit()
        bullet = pygame.sprite.spritecollideany(p1, ebullets)
        bullet.kill()

def updateEnemies(enemies, p1, ebullets):
    enemies.update(ebullets, p1)

    for enemy in enemies.copy():
             if enemy.rect.top >= 675:
                enemies.remove(enemy)
             if enemy.eType != 1 and enemy.eType!=2:
                if enemy.fired:
                    if enemy.rect.bottom <= 23:
                        enemies.remove(enemy)

    if pygame.sprite.spritecollideany(p1, enemies) and (not p1.getHit()):
        p1.gotHit()
        enemy = pygame.sprite.spritecollideany(p1, enemies)
        enemy.kill()

def getHighScore():

    f = open("score.txt", "r")
    temp = f.read()
    f.close()
    global highScore
    highScore = int(temp)

def updateScore():
    global highScore
    global score
    if score > highScore:
        highScore = score

def writeHighScore():

    f = open("score.txt", "w")
    f.write(str(highScore))
    f.close()

def updateBBullets(bbullets, p1):
    bbullets.update()

    for bbullet in bbullets.copy():
            if bbullet.rect.bottom <= 23 or bbullet.rect.top >= 675 or bbullet.rect.right <= 46 or bbullet.rect.left >= 646:
                bbullets.remove(bbullet)

    if pygame.sprite.spritecollideany(p1, bbullets) and (not p1.getHit()):
        p1.gotHit()
        bullet = pygame.sprite.spritecollideany(p1, bbullets)
        bullet.kill()

def updateBoss(bossGroup, bbullets, p1):
    for boss in bossGroup.sprites():
        boss.update(bbullets,p1)
