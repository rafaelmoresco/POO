import sys
import pygame
import math
from bullet import *
from pygame.sprite import Sprite

class Boss(Sprite):

    def __init__(self,  gSettings, screen, x, y, p1):
        super().__init__()
        #Inicialização basica
        self.screen = screen
        self.timer = 0
        self.timerM = gSettings.getBDelay()
        self.pattern = True
        self.image = pygame.image.load('images/Comet-1.png').convert_alpha(screen)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.gSettings = gSettings
        self.y = y
        self.x = x
        self.speed = gSettings.getEBSpeed()/2
        self.direction = -1 #0Centro-Direita 1Direita-Centro 2Centro-Esquerda 3Esquerda-Centro
        self.counter = 0
        self.alive = True
        self.hp = gSettings.getBHP()

    def count(self):
        self.counter += 1
        return self.counter

    def update(self, bbullets, p1):
        #Durante o counter, atira em circulo, fora atira 3 projeteis na direção do jogador
        if self.alive:    
            if self.direction == -1:
                if self.counter <= 120:
                        self.counter += 1
                        self.timer += 1
                        if self.timer >= self.timerM:
                            self.fireC(bbullets,p1)
                            self.timer = 0
                else:
                    self.counter = 0
                    self.direction = 0
            elif self.direction == 0:
                if self.rect.centerx < 497:
                    self.x += self.speed
                    self.timer += 1
                    if self.timer >= self.timerM*2:
                        self.fireL(bbullets,p1)
                        self.timer = 0
                else:
                    if self.counter <= 120:
                        self.counter += 1
                        self.timer += 1
                        if self.timer >= self.timerM:
                            self.fireC(bbullets,p1)
                            self.timer = 0
                    else:
                        self.counter = 0
                        self.direction = 1
            elif self.direction == 1:
                if self.rect.centerx > 347:
                    self.x -= self.speed
                    self.timer += 1
                    if self.timer >= self.timerM*2:
                        self.fireL(bbullets,p1)
                        self.timer = 0
                else:
                    if self.counter <= 120:
                        self.counter += 1
                        self.timer += 1
                        if self.timer >= self.timerM:
                            self.fireC(bbullets,p1)
                            self.timer = 0
                    else:
                        self.counter = 0
                        self.direction = 2
            elif self.direction == 2:
                if self.rect.centerx > 197:
                    self.x -= self.speed
                    self.timer += 1
                    if self.timer >= self.timerM*2:
                        self.fireL(bbullets,p1)
                        self.timer = 0
                else:
                    if self.counter <= 120:
                        self.counter += 1
                        self.timer += 1
                        if self.timer >= self.timerM:
                            self.fireC(bbullets,p1)
                            self.timer = 0
                    else:
                        self.counter = 0
                        self.direction = 3
            else:
                if self.rect.centerx < 347:
                    self.x += self.speed
                    self.timer += 1
                    if self.timer >= self.timerM*2:
                        self.fireL(bbullets,p1)
                        self.timer = 0
                else:
                    if self.counter <= 120:
                        self.counter += 1
                        self.timer += 1
                        if self.timer >= self.timerM:
                            self.fireC(bbullets,p1)
                            self.timer = 0
                    else:
                        self.counter = 0
                        self.direction = 0
            self.rect.centerx = self.x
            self.rect.centery = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def fireC(self, bbullets, p1):
        if self.pattern:
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 75)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 175)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 275)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 375)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 475)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 575)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-200, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-100, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+100, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+200, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 575)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 475)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 375)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 275)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 175)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 75)
            bbullets.add(new_bullet)
            self.pattern = False
        else:
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 25)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 125)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 225)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 325)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 425)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 525)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-300, 625)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-250, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-150, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx-50, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+50, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+150, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+250, 675)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 25)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 125)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 225)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 325)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 425)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 525)
            bbullets.add(new_bullet)
            new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, self.rect.centerx+300, 625)
            bbullets.add(new_bullet)
            self.pattern = True

    def fireL(self, bbullets, p1):
        
        new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, p1.rect.centerx-100, p1.rect.centery)
        bbullets.add(new_bullet)
        new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, p1.rect.centerx, p1.rect.centery)
        bbullets.add(new_bullet)
        new_bullet = BBulletT(self.gSettings, self.screen, self.rect.centerx, self.rect.centery, p1.rect.centerx+100, p1.rect.centery)
        bbullets.add(new_bullet)

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.alive = False
            