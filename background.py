import pygame
import random
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self,gSettings,screen,trueScreen,type):
        super().__init__()
        self.gSettings = gSettings
        self.screen = screen
        self.trueScreen = trueScreen
        self.type = type

        if self.type == 0:
            self.image = pygame.image.load('images/bg.png').convert_alpha()
            self.speed = 0
            self.rect = self.image.get_rect()
        else:
            if self.type == 1:
                self.image = pygame.image.load('images/cloud1.png').convert_alpha()
            elif self.type == 2:
                self.image = pygame.image.load('images/cloud2.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(self.trueScreen.left,self.trueScreen.right)

            self.speed = random.randrange(5,10)

    def update(self):
        self.rect.centery += self.speed
        if self.rect.top > self.trueScreen.bottom:
            self.rect.centery = self.trueScreen.top
            if self.type != 0:
                self.rect.centerx = random.randrange(self.trueScreen.left,self.trueScreen.right)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
