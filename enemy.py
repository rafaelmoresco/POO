import sys
import pygame
import math
from bullet import *
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, gSettings, screen, eType, x, y, p1):
        super().__init__()
        #Inicialização basica
        self.screen = screen
        self.eType = eType
        self.timer = 0
        self.fired = False
        self.fDelay = gSettings.getEFDelay()
        self.targetx = p1.rect.centerx
        self.targety = p1.rect.centery
        if self.eType == 1:
            self.image = pygame.image.load('images/M1.png')
        elif self.eType == 2:
            self.image = pygame.image.load('images/M2.png')
        else:
            self.image = pygame.image.load('images/M3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.y = y
        self.x = x
        #controle movimento parabólico inimigo 3
        self.goingDown = True
        self.pxi = x
        self.px = -300
        self.py = 0
        #Speed
        self.speed = gSettings.getESpeed()

    def update(self, ebullets, p1):
        if self.eType == 1:
            self.y += self.speed

        elif self.eType == 2:
            if self.rect.y < 100:
                self.y += self.speed
            else:
                self.timer +=1
                if self.timer >= self.fDelay:
                    #fire

                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx, 0)
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, 0, self.rect.centery)
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.gSettings.getWidth(), self.rect.centery)
                    ebullets.add(new_bullet)

                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+200, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-200, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+200, 0)
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-200, 0)
                    ebullets.add(new_bullet)

                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+400, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-400, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+400, 0)
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-400, 0)
                    ebullets.add(new_bullet)

                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+600, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-600, self.gSettings.getHight())
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+600, 0)
                    ebullets.add(new_bullet)
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-600, 0)
                    ebullets.add(new_bullet)


                    self.timer = 0
        else:
            if self.goingDown:
                self.x = self.pxi + (300 + self.px)
                self.py = math.sqrt(90000 - (self.px**2))
                self.y = self.py
                if self.px >= 0:
                    self.goingDown = False
                
                if self.px > -250:
                    self.px += 2
                else:
                    self.px += 1

            else:
                if not self.fired:
                    self.targetx = p1.rect.centerx
                    self.targety = p1.rect.centery
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.targetx, self.targety)
                    ebullets.add(new_bullet)
                    self.fired = True
                if not(self.px >= 300):
                    self.x = self.pxi + 300 + self.px
                    self.py = math.sqrt(90000 - (self.px**2))
                    self.y = self.py
                    if self.px < 250:
                        self.px += 2
                    else:
                        self.px += 1
                else:
                    self.y -= self.speed
                
        self.rect.centery = self.y
        self.rect.centerx = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
