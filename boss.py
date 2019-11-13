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
        self.eType = eType
        self.timer = 0
        self.image = pygame.image.load('images/Comet-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.y = y
        self.x = x
        self.speed = gSettings.getESpeed()