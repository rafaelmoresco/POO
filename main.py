import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from player import Player

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    #Create settings
    gSettings = Settings()
    #Create screen
    screen = pygame.display.set_mode((gSettings.getWidth(), gSettings.getHight()))
    #Set Screen title
    pygame.display.set_caption("Touhou Clone")
    #Create player
    p1 = Player(gSettings, screen)
    #Create buller group
    bullets = Group()
    # Start the main loop for the game.
    while True:
        gf.checkEvents(p1, gSettings, screen, bullets)
        gf.updateScreen(gSettings, screen, p1, bullets)
        p1.update(bullets)
        bullets.update()

run_game()
