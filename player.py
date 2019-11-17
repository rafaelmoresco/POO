import pygame
import game_functions as gf
from bullet import PBullet
from enemy import Enemy
from explosion import Explosion
from pygame.sprite import Sprite
class Player(Sprite):

    def __init__(self, gSettings, screen,enemies,soundController,trueScreen,explosions,ebullets,bbullets):
        super().__init__()
        #Inicialização basica
        self.screen = screen
        self.trueScreen = trueScreen
        self.soundController = soundController
        self.anim = [pygame.image.load('images/reimu-1.png').convert_alpha(screen), pygame.image.load('images/reimu-2.png').convert_alpha(screen),pygame.image.load('images/reimu-3.png').convert_alpha(screen),pygame.image.load('images/reimu-4.png').convert_alpha(screen),pygame.image.load('images/reimu-5.png').convert_alpha(screen),pygame.image.load('images/reimu-6.png').convert_alpha(screen),pygame.image.load('images/reimu-7.png').convert_alpha(screen),pygame.image.load('images/reimu-8.png').convert_alpha(screen)]
        self.image = self.anim[0]
        self.iRect = self.image.get_rect()
        #self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gSettings = gSettings
        self.fDelay = gSettings.getPFireDelay()
        self.tFDelay = gSettings.getPFireDelay()
        self.enemies = enemies
        self.explosions = explosions
        self.ebullets = ebullets
        self.bbullets = bbullets
        #Controle das animações
        self.spriteNum = 0
        self.spriteNumMax = 8
        self.spriteTimer = 0
        self.spriteTimermMax = 7
        #Inicializa hitbox
        self.hImage = pygame.image.load('images/hitbox3.png').convert_alpha(screen)
        self.rect = self.hImage.get_rect()
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
        self.cf = True #Pode atirar
        self.dead = False #Pode agir
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
        if not self.dead:
            self.life -= 1
            self.hit = True
            self.soundController.playSound(4)
            if self.life <= 0:
                self.explosions.add(Explosion(self.screen,self.rect.centerx,self.rect.centery,100,5,0))
                self.dead = True
                self.speed = 0
                self.speed2 = 0
                self.cf = False
                gf.writeHighScore()
                self.soundController.stopMusic()
                self.soundController.playSound(2)

    def getLife(self):
        return self.life
    
    def addLife(self):
        self.life +=1

    def getBombs(self):
        return self.bombs
    
    def addBombs(self):
        self.bombs +=1

    def update(self, bullets):
        #Normal Speed
        if self.mr and not self.sm and self.rect.right < self.trueScreen.right:
            self.centerx += self.speed
        if self.ml and not self.sm and self.rect.left > self.trueScreen.left:
            self.centerx -= self.speed
        if self.mu and not self.sm and self.rect.top > self.trueScreen.top:
            self.centery -= self.speed
        if self.md and not self.sm and self.rect.bottom < self.trueScreen.bottom:
            self.centery += self.speed
        #Slow Speed
        if self.mr and self.sm and self.rect.right < self.trueScreen.right:
            self.centerx += self.speed2
        if self.ml and self.sm and self.rect.left > self.trueScreen.left:
            self.centerx -= self.speed2
        if self.mu and self.sm and self.rect.top > self.trueScreen.top:
            self.centery -= self.speed2
        if self.md and self.sm and self.rect.bottom < self.trueScreen.bottom:
            self.centery += self.speed2
        #Verifica se o delay de disparo foi atingido, se for dispara e reseta o contador
        if self.fDelay >= self.tFDelay and self.fi:
            if self.cf:
                if not self.sm:
                    new_bullet_right = PBullet(self.gSettings, self.screen, self.centerx+20, self.iRect.top+10,False)
                    new_bullet_left = PBullet(self.gSettings, self.screen, self.centerx-20, self.iRect.top+10,False)
                    bullets.add(new_bullet_right)
                    bullets.add(new_bullet_left)
                    self.soundController.playSound(0)
                else:
                    new_bullet_right = PBullet(self.gSettings, self.screen, self.centerx+5, self.iRect.top,True)
                    new_bullet_left = PBullet(self.gSettings, self.screen, self.centerx-5, self.iRect.top,True)
                    bullets.add(new_bullet_right)
                    bullets.add(new_bullet_left)
                    self.soundController.playSound(0)
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
        self.iRect.centerx = self.centerx
        self.iRect.centery = self.centery
        #Update Animação
        self.spriteTimer+=1

        if self.spriteTimer>=self.spriteTimermMax:
            self.spriteNum+=1
            self.spriteTimer = 0

        if self.spriteNum >= self.spriteNumMax:
            self.spriteNum = 0

        self.image = self.anim[self.spriteNum]

    def getHit(self):
        return self.hit

    def bomb(self,boss):
        if self.bombs > 0 and not self.dead:
            self.explosions.add(Explosion(self.screen,self.trueScreen.centerx,self.trueScreen.centery,self.gSettings.getHight()+100,50,1))
            for i in range(len(self.enemies)):
                gf.addScore()
            self.enemies.empty()
            self.ebullets.empty()
            self.bbullets.empty()
            boss.hitBomb()
            self.bombs -= 1
            self.soundController.playSound(3)

    def blitme(self):
        if not self.dead:
            self.screen.blit(self.image, self.iRect)
            if self.sm:
                self.screen.blit(self.hImage,self.rect)
