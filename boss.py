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
        self.image = pygame.image.load('images/Comet-1.png').convert_alpha(screen)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.gSettings = gSettings
        self.y = y
        self.x = x
        self.speed = gSettings.getESpeed()/2
        self.direction = 0 #0Centro-Direita 1Direita-Centro 2Centro-Esquerda 3Esquerda-Centro
        self.counter = 0
        self.alive = True
        self.hp = 100

    def count(self):
        self.counter += 1
        return self.counter

    def update(self):
        #Durante o counter, atira em circulo, fora atira 3 projeteis na direção do jogador
        if self.direction == 0:
            if self.rect.centerx < 497:
                self.x += self.speed
            else:
                if self.counter <= 120:
                    self.counter += 1
                else:
                    self.counter = 0
                    self.direction = 1
        elif self.direction == 1:
            if self.rect.centerx > 347:
                self.x -= self.speed
            else:
                if self.counter <= 120:
                    self.counter += 1
                else:
                    self.counter = 0
                    self.direction = 2
        elif self.direction == 2:
            if self.rect.centerx > 197:
                self.x -= self.speed
            else:
                if self.counter <= 120:
                    self.counter += 1
                else:
                    self.counter = 0
                    self.direction = 3
        else:
            if self.rect.centerx < 347:
                self.x += self.speed
            else:
                if self.counter <= 120:
                    self.counter += 1
                else:
                    self.counter = 0
                    self.direction = 0
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
