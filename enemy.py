import sys
import pygame

class Enemy():

    def __init__(self, gSettings, screen, eType, x, y):
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