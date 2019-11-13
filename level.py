import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player
from enemy import Enemy
import random

class Level:
    def __init__(self,screen,gSettings,enemies,p1,trueScreen):
        self.screen = screen
        self.trueScreen = trueScreen
        self.gSettings = gSettings
        self.screen_rect = screen.get_rect()
        self.enemies = enemies
        self.p1 = p1

    def generateSpawn(self):
        num1 = random.randrange(1,5)
        num2 = random.randrange(2,10)
        qual = random.randrange(1,6)

        if qual == 1:
            self.spawnEasy(num2)
        elif qual == 2:
            self.spawnParabola(num1)
        elif qual == 3:
            self.fillScreen(num1)
        elif qual == 4:
            self.mixed1(num1,num2)
        elif qual == 5:
            self.mixed2(num1,num2)
        elif qual == 6:
            self.mixed3(num1)

    def spawnEasy(self,num):
        self.dist = random.randrange(10,250)
        for i in range(num):
            self.new_enemy = Enemy(self.gSettings, self.screen, 1, self.trueScreen.centerx-self.dist,0-200*i,self.p1,0)
            self.enemies.add(self.new_enemy)
            self.new_enemy = Enemy(self.gSettings, self.screen, 1, self.trueScreen.centerx+self.dist,0-200*i,self.p1,0)
            self.enemies.add(self.new_enemy)

    def spawnParabola(self,num):
        self.dist = random.randrange(10,250)
        for i in range(num):
            self.new_enemy = Enemy(self.gSettings, self.screen, 3, self.trueScreen.centerx-self.dist-200*i,0-200*i,self.p1,0)
            self.enemies.add(self.new_enemy)

    def fillScreen(self,num):
        self.dist = random.randrange(50,200)
        for i in range(num):
            self.new_enemy = Enemy(self.gSettings, self.screen, 2, self.trueScreen.centerx-self.dist,0-200*i,self.p1,100+100*i)
            self.enemies.add(self.new_enemy)
            self.new_enemy = Enemy(self.gSettings, self.screen, 2, self.trueScreen.centerx+self.dist,0-200*i,self.p1,100+100*i)
            self.enemies.add(self.new_enemy)

    def mixed1(self,num1,num2):
        self.dist = random.randrange(10,250)
        self.fillScreen(num1)
        self.spawnEasy(num2)

    def mixed2(self,num1,num2):
        self.spawnParabola(num1)
        self.spawnEasy(num2)

    def mixed3(self,num):
        self.dist = random.randrange(10,250)
        self.fillScreen(num)
        self.spawnParabola(num)
