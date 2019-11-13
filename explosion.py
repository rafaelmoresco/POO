import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):

    def __init__(self,screen,x,y,limit,increase,cor):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.cor = cor
        if self.cor == 0:
            self.image = pygame.image.load('images/exp_1.png').convert_alpha(screen)
        else:
            self.image = pygame.image.load('images/exp_2.png').convert_alpha(screen)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.size = 0
        self.limit = limit
        self.increase = increase

        self.scaled = self.image
        self.new_rect = self.rect

    def update(self):
        self.scaled = pygame.transform.scale(self.image,(self.size,self.size))  
        self.new_rect = self.scaled.get_rect()
        self.new_rect.centerx = self.x
        self.new_rect.centery = self.y

        if self.size >= self.limit:
            self.kill()

        self.size+=self.increase

    def blitme(self):
        self.screen.blit(self.scaled,self.new_rect)
