import sys
import pygame
import random
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy
from level import Level
from boss import Boss
from soundcontroller import Sound
from background import Background
from explosion import Explosion

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("Touhou C")
gSettings = Settings()
soundController = Sound()
screen = pygame.display.set_mode((gSettings.getWidth(), gSettings.getHight()))
trueScreen = pygame.Rect(46,23,gSettings.getTrueWidth(),gSettings.getTrueHight())
clock = pygame.time.Clock()
fps = gSettings.getFPS()

titleFont = gSettings.getTitleFont()
buttonFont = gSettings.getButtonFont()
titleText = gSettings.getTitleText()
titleColor = gSettings.getIntroTitleColor()
buttonColor = gSettings.getButtonColor()
buttonHover = gSettings.getButtonHoverColor()
buttonTextColor = gSettings.getButtonTextColor()

def quit_game():
    pygame.quit()
    quit()

def button(texto,buttonCords,color,colorHover,textColor, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    buttonFont = gSettings.getButtonFont()

    if buttonCords[0] + buttonCords[2] > mouse[0] > buttonCords[0] and buttonCords[1] + buttonCords[3] > mouse[1] > buttonCords[1]:
        pygame.draw.rect(screen, colorHover,buttonCords)
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(screen, color,buttonCords)

    TextSurf,TextRect = text_objects(texto,buttonFont,textColor)
    TextRect.center = ( int(buttonCords[0]+(buttonCords[2]/2)) , int(buttonCords[1]+(buttonCords[3]/2)) )
    screen.blit(TextSurf, TextRect)

def telaBotoes(texto,textoBotao1,textoBotao2):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(gSettings.getIntroBgColor())

        TextSurf, TextRect = text_objects(texto,titleFont,titleColor)
        TextRect.center = (int(gSettings.getWidth()/2),int(gSettings.getHight()/6))
        screen.blit(TextSurf, TextRect)

        button1Cords = (int(gSettings.getWidth()/2-100),300,200,75)
        button2Cords = (int(gSettings.getWidth()/2-100),450,200,75)
        button3Cords = (int(gSettings.getWidth()/2-100),600,200,75)

        button(textoBotao1, button1Cords, buttonColor,buttonHover,buttonTextColor,telaInstruc)
        button(textoBotao2, button2Cords, buttonColor,buttonHover,buttonTextColor,quit_game)

        pygame.display.flip()
        clock.tick(fps)

def telaInstruc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(gSettings.getIntroBgColor())

    def drawText(texto,font,gSettings,screen,x,y,cor):
        text_surface = font.render(texto,True,cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (int(x),int(y))
        screen.blit(text_surface,text_rect)

    font1 = gSettings.getButtonFont()
    font2 = gSettings.getTitleFont()
    branco = (255,255,255)
    vermelho = gSettings.getIntroTitleColor()

    drawText("SETAS = Mover",font1,gSettings,screen,gSettings.getWidth()/2,100,branco)
    drawText("Z = Atirar",font1,gSettings,screen,gSettings.getWidth()/2,150,branco)
    drawText("X = Bomba",font1,gSettings,screen,gSettings.getWidth()/2,200,branco)
    drawText("SHIFT = Modo precisão",font1,gSettings,screen,gSettings.getWidth()/2,250,branco)
    drawText("Prepare se...",font2,gSettings,screen,gSettings.getWidth()/2,600,vermelho)

    pygame.display.flip()
    pygame.time.wait(5000)
    run_game()



def text_objects(texto,fonte,cor):
    textSurface = fonte.render(texto, True, cor)
    return textSurface, textSurface.get_rect()

def run_game():
    #Cria bullet group
    bullets = Group()
    #Cria enemy group
    enemies = Group()
    #Cira enemy bullet group
    ebullets = Group()
    bbullets = Group()
    explosions = Group()
    gSettings.resetDificulty()

    gf.clearScore()

    bg = Background(gSettings,screen,trueScreen,0)
    clouds = Group()
    for i in range(3):
        new_cloud = Background(gSettings,screen,trueScreen,1)
        clouds.add(new_cloud)
        new_cloud = Background(gSettings,screen,trueScreen,2)
        clouds.add(new_cloud)


    #Cria jogador
    p1 = Player(gSettings, screen,enemies,soundController,trueScreen,explosions,ebullets,bbullets)

    level = Level(screen,gSettings,enemies,p1,trueScreen)

    gf.initGUI(gSettings,screen)
    gf.getHighScore()
    soundController.playMusic(0)

    #Inicia o loop principal do jogo.
    level.generateSpawn()
    boss = Boss(gSettings,screen,347,100,p1,soundController)
    bossCount = 0
    bossSpawned = False
    first = 0

    while True:

        clock.tick(fps)

        gf.checkEvents(p1, gSettings, screen, bullets, boss, bossSpawned)
        gf.updateScreen(gSettings, screen, p1, bullets, enemies, ebullets,bg,clouds,explosions,boss,bbullets, bossSpawned)
        gf.updateBg(bg,clouds)
        p1.update(bullets)
        gf.updateBullets(bullets,enemies,soundController,screen, explosions, boss)
        gf.updateExplosions(explosions)
        gf.updateEBullets(ebullets, p1)
        gf.updateBBullets(bbullets, p1)
        gf.updateEnemies(enemies, p1, ebullets)
        gf.updateBoss(boss, bbullets, p1, bossSpawned)
        gf.updateScore()

        if len(enemies) == 0:
            if bossCount >= 20:
                bossCount = 0
                if first == 1:
                    gSettings.bossIncrease()
                    boss = Boss(gSettings,screen,347,100,p1,soundController)
                bossSpawned = True
                soundController.stopMusic()
                soundController.playMusic(1)
            else:
                if not bossSpawned:
                    gSettings.difficultyIncrease()
                    level.generateSpawn()
                    bossCount += 1
                else:
                    if boss.hp <= 0:
                        bossSpawned = False
                        boss.alive = False
                        soundController.stopMusic()
                        soundController.playMusic(0)
                        gf.addBScore(p1)
                        first = 1
                        soundController.playSound(6)
                        new_explosion = new_explosion = Explosion(screen,boss.rect.centerx,boss.rect.centery,200,10,0)
                        explosions.add(new_explosion)

        if p1.dead and not pygame.mixer.get_busy():
            telaBotoes("Game Over", "Novamente", "Sair")

telaBotoes("Touhou C", "Iniciar", "Sair")
