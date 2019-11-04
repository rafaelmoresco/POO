import pygame
from bullet import PBullet
from enemy import Enemy
from pygame.sprite import Sprite
class Player(Sprite):

    def __init__(self, gSettings, screen,enemies):
        super().__init__()
        #Inicialização basica
        self.screen = screen
        self.image = pygame.image.load('images/Jogador.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.fDelay = gSettings.getPFireDelay()
        self.tFDelay = gSettings.getPFireDelay()
        self.enemies = enemies
        #Inicializa hitbox
        self.hImage = pygame.image.load('images/hitbox.png')
        self.hRect = self.hImage.get_rect()
        #Speed
        self.speed = self.gSettings.getPSpeed()
        self.speed2 = self.gSettings.getPSpeed2()
        #Flags de ação
        self.mr = False #Move Right
        self.ml = False #Move Left
        self.mu = False #Move Up
        self.md = False #Move Down
        self.sm = False #Slow Mode
        self.fi = False #Firing
        self.hit = False #Recentemente atingido
        #Posições
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom -150
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #Infos
        self.life = 3
        self.bombs = 3
        self.score = 0
        self.tInv = gSettings.getTInv()
        self.iTimer = 0

    def gotHit(self):
        self.life -= 1
        self.hit = True
        if self.life <= 0:
            self.speed = 0
            self.speed2 = 0

    def getLife(self):
        return self.life

    def getBombs(self):
        return self.bombs


    def update(self, bullets):
        #Normal Speed
        if self.mr and not self.sm and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.ml and not self.sm and self.rect.left > 0:
            self.centerx -= self.speed
        if self.mu and not self.sm and self.rect.top > 0:
            self.centery -= self.speed
        if self.md and not self.sm and self.rect.bottom < self.screen_rect.bottom-100:
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
        #Verifica se o delay de disparo foi atingido, se for dispara e reseta o contador
        if self.fDelay >= self.tFDelay and self.fi:
            if not self.sm:
                new_bullet_right = PBullet(self.gSettings, self.screen, self.centerx+20, self.rect.top+10,False)
                new_bullet_left = PBullet(self.gSettings, self.screen, self.centerx-20, self.rect.top+10,False)
                bullets.add(new_bullet_right)
                bullets.add(new_bullet_left)
            else:
                new_bullet_right = PBullet(self.gSettings, self.screen, self.centerx+5, self.rect.top,True)
                new_bullet_left = PBullet(self.gSettings, self.screen, self.centerx-5, self.rect.top,True)
                bullets.add(new_bullet_right)
                bullets.add(new_bullet_left)
            self.fDelay = 0
        #Enquanto Fire estiver ativado, contador conta
        if self.fi:
            self.fDelay += 1
        #Se o botão é solto, volta para o valor maximo
        else:
            self.fDelay = self.tFDelay
        #Se atingido recentemente
        if self.hit:
            self.iTimer += 1
            if self.iTimer >= self.tInv:
                self.hit = False
                self.iTimer = 0
        #Update Movemento
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.hRect.centerx = self.centerx
        self.hRect.centery = self.centery

    def getHit(self):
        return self.hit

    def bomb(self):
        if self.bombs > 0:
            self.enemies.empty()
            self.bombs -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        if self.sm:
            self.screen.blit(self.hImage,self.hRect)
