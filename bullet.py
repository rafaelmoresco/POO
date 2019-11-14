import pygame
import math
from pygame.sprite import Sprite

class PBullet(Sprite):

    def __init__(self, gSettings, screen, pCenterx, pTop, isSlow):
        super().__init__()
        #init size
        self.bulletHeight = 15
        self.bulletWidth = 3

        self.screen = screen
        self.gSettings = gSettings
        self.rect = pygame.Rect(0,0, self.bulletWidth, self.bulletHeight)
        self.colour = 60,60,60

        if not isSlow:
            self.speed = self.gSettings.getPBulletS()
        else:
            self.speed = self.gSettings.getPBulletS_Slow()

        self.rect.centerx = pCenterx
        self.rect.top = pTop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen,self.colour,self.rect)

class EBulletT(Sprite):

    def __init__(self, gSettings, screen, x, y, tx, ty):
        super().__init__()
        #init size
        self.image = pygame.image.load('images/MonsterTiro.png')
        self.rect = self.image.get_rect()

        self.screen = screen
        self.gSettings = gSettings
        
        self.rect.centerx = x
        self.rect.centery = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.xd = abs(x - tx)
        self.yd = abs(y - ty)
        self.hipotenusa = math.sqrt(pow(self.xd,2) + pow(self.yd,2))
        if x < tx:
            self.leftRight = 1
        else:
            self.leftRight = 0
        if y < ty:
            self.upDown = 1
        else:
            self.upDown = 0

        #speed
        self.speedx = gSettings.getEBSpeed() * (self.xd/self.hipotenusa)
        self.speedy = gSettings.getEBSpeed() * (self.yd/self.hipotenusa)

        self.screen = screen
        self.gSettings = gSettings

    def update(self):

        if self.upDown == 1:
            self.y += self.speedy
        else:
            self.y -= self.speedy
        if self.leftRight == 1:
            self.x += self.speedx
        else:
            self.x -= self.speedx

        self.rect.y = self.y
        self.rect.x = self.x

    def drawEBullet(self):
        self.screen.blit(self.image, self.rect)

class BBulletT(Sprite):

    def __init__(self, gSettings, screen, x, y, tx, ty):
        super().__init__()
        #init size
        self.image = pygame.image.load('images/BossTiro.png')
        self.rect = self.image.get_rect()

        self.screen = screen
        self.gSettings = gSettings
        
        self.rect.centerx = x
        self.rect.centery = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.xd = abs(x - tx)
        self.yd = abs(y - ty)
        self.hipotenusa = math.sqrt(pow(self.xd,2) + pow(self.yd,2))
        if x < tx:
            self.leftRight = 1
        else:
            self.leftRight = 0
        if y < ty:
            self.upDown = 1
        else:
            self.upDown = 0

        #speed
        self.speedx = gSettings.getEBSpeed() * (self.xd/self.hipotenusa)
        self.speedy = gSettings.getEBSpeed() * (self.yd/self.hipotenusa)

        self.screen = screen
        self.gSettings = gSettings

    def update(self):

        if self.upDown == 1:
            self.y += self.speedy
        else:
            self.y -= self.speedy
        if self.leftRight == 1:
            self.x += self.speedx
        else:
            self.x -= self.speedx

        self.rect.y = self.y
        self.rect.x = self.x

    def drawEBullet(self):
        self.screen.blit(self.image, self.rect)