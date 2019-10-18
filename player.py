import pygame
from bullet import PBullet
class Player():

    def __init__(self, gSettings, screen):
        #Basic init
        self.screen = screen
        self.image = pygame.image.load('images/Jogador.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.fDelay = 50 #Fire Delay
        #Speed
        self.speed = self.gSettings.getPSpeed()
        self.speed2 = self.gSettings.getPSpeed2()
        #Action flags
        self.mr = False #Move Right
        self.ml = False #Move Left
        self.mu = False #Move Up
        self.md = False #Move Down
        self.sm = False #Slow Mode
        self.fi = False #Firing
        #Positions
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom -80
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    def update(self, bullets):
        #Normal Speed
        if self.mr and not self.sm and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.ml and not self.sm and self.rect.left > 0:
            self.centerx -= self.speed
        if self.mu and not self.sm and self.rect.top > 0:
            self.centery -= self.speed
        if self.md and not self.sm and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        #Slow Speed
        if self.mr and self.sm and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed2
        if self.ml and self.sm and self.rect.left > 0:
            self.centerx -= self.speed2
        if self.mu and self.sm and self.rect.top > 0:
            self.centery -= self.speed2
        if self.md and self.sm and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed2
        #Verifies if the delay timer is equal to 50, if it is fires one bullet and resets it
        if self.fDelay >= 50 and self.fi:
            new_bullet = PBullet(self.gSettings, self.screen, self.centerx, self.rect.top)
            bullets.add(new_bullet)
            self.fDelay = 0
        #While fire button is presse, it counts
        if self.fi:
            self.fDelay += 1
        #If the button is released, the counter goes back to 50
        else:
            self.fDelay = 50

        #Update Movement
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    def blitme(self):
        self.screen.blit(self.image, self.rect)