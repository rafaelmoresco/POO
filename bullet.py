import pygame
from pygame.sprite import Sprite

class PBullet(Sprite):

    def __init__(self, gSettings, screen, pCenterx, pTop,isSlow):
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
