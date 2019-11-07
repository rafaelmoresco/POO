import sys
import pygame
import game_functions as gf
import threading
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy

class Level:
    def __init__(self,screen,gSettings,enemies,p1,trueScreen):
        self.screen = screen
        self.trueScreen = trueScreen
        self.gSettings = gSettings
        self.screen_rect = screen.get_rect()
        self.enemies = enemies
        self.p1 = p1


    def decodeSpawn(self,lista):
        self.code = lista[0]
        self.quantos = lista[1]
        self.tipo = lista[2]
        self.dist = lista[3]
        self.tempo = lista[4]

        if self.code == 0:
            self.spawnLados()
        elif self.code == 1:
            self.spawnMeio()

    def spawnLados(self):
        for i in range(0,self.quantos):
            if self.tipo!=1 and self.tipo!=2:
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx-self.dist-self.tempo*i,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx+self.dist-self.tempo*i,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)
            else:
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx-self.dist,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx+self.dist,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)

    def spawnMeio(self):
        for i in range(0,self.quantos):
            if self.tipo!=1 and self.tipo!=2:
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx-self.tempo*i,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)
            else:
                self.new_enemy = Enemy(self.gSettings, self.screen, self.tipo, self.trueScreen.centerx,0-self.tempo*i,self.p1)
                self.enemies.add(self.new_enemy)
