import sys
import pygame
import random
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy
from level import Level
from soundcontroller import Sound
from background import Background

pygame.init()
pygame.display.set_caption("Touhou Clone")
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

gf.getHighScore()

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

        button1Cords = (int(gSettings.getWidth()/2-100),350,200,75)
        button2Cords = (int(gSettings.getWidth()/2-100),500,200,75)

        button(textoBotao1, button1Cords, buttonColor,buttonHover,buttonTextColor,run_game)
        button(textoBotao2, button2Cords, buttonColor,buttonHover,buttonTextColor,quit_game)


        pygame.display.flip()
        clock.tick(fps)


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

    bg = Background(gSettings,screen,trueScreen,0)
    clouds = Group()
    for i in range(5):
        new_cloud = Background(gSettings,screen,trueScreen,random.randrange(1,2))
        clouds.add(new_cloud)

    #Cria jogador
    p1 = Player(gSettings, screen,enemies,soundController,trueScreen)

    level = Level(screen,gSettings,enemies,p1,trueScreen)

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

    gf.importFont(gSettings)
    gf.convertImages()
    soundController.playMusic(0)

    #Inicia o loop principal do jogo.
    while True:

        clock.tick(fps)

        gf.checkEvents(p1, gSettings, screen, bullets)
        gf.updateScreen(gSettings, screen, p1, bullets, enemies, ebullets,bg,clouds)
        gf.updateBg(bg,clouds)
        p1.update(bullets)
        gf.updateBullets(bullets,enemies,soundController)
        gf.updateEBullets(ebullets, p1)
        gf.updateEnemies(enemies, p1, ebullets)
        gf.updateScore()
        

        if len(enemies) == 0 and cont < len(spawnQueue):
                level.decodeSpawn(spawnQueue[cont])
                cont+=1

        if p1.dead and not pygame.mixer.get_busy():
            telaBotoes("Game Over", "Novamente", "Sair")

telaBotoes("Touhou Clone", "Iniciar", "Sair")
