import sys
import pygame
from bullet import *
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, gSettings, screen, eType, x, p1):
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
        self.y = float(self.rect.centery)
        self.x = x
        self.goingDown = True
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
                    self.timer = 0
        else:
            if self.goingDown:
                self.y += self.speed
                self.x += self.speed/2
                if self.rect.y >= 200:
                    self.goingDown = False
            else:
                if not self.fired:
                    self.targetx = p1.rect.centerx
                    self.targety = p1.rect.centery
                    new_bullet = EBulletT(self.gSettings, self.screen, self.rect.x, self.rect.y, self.targetx, self.targety)
                    ebullets.add(new_bullet)
                    self.fired = True
                self.y -= self.speed
                self.x += self.speed/1.5
        self.rect.centery = self.y
        self.rect.centerx = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
