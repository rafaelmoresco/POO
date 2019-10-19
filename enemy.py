import sys
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, gSettings, screen, eType, x):
        super().__init__()
        #Basic Init
        self.screen = screen
        self.eType = eType
        if self.eType == 1:
            self.image = pygame.image.load('images/M1.png')
        elif self.eType == 2:
            self.image = pygame.image.load('images/M2.png')
        else:
            self.image = pygame.image.load('images/M3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.y = float(self.rect.y)
        self.x = x
        self.goingDown = True
        #Speed
        self.speed = gSettings.getESpeed()

    def update(self):
        if self.eType == 1:
            self.y += self.speed

        elif self.eType == 2:
            if self.rect.y < 100:
                self.y += self.speed
        else:
            if self.goingDown:
                self.y += self.speed
                self.x += self.speed/2
                if self.rect.y >= 200:
                    self.goingDown = False
            else:
                self.y -= self.speed
                self.x += self.speed/1.5
        self.rect.y = self.y
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
