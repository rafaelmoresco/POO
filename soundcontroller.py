
import pygame

class Sound:
    def __init__(self):
        shot = pygame.mixer.Sound('sounds/shot.wav')
        death_e = pygame.mixer.Sound('sounds/death_e.wav')
        death_p = pygame.mixer.Sound('sounds/death_p.wav')
        bomb = pygame.mixer.Sound('sounds/bomb.wav')
        damage = pygame.mixer.Sound('sounds/damage.wav')

        self.sounds = [shot,death_e,death_p,bomb,damage]
        for sound in self.sounds:
            sound.set_volume(0.25)

        stage1 = 'music/stage1.ogg'
        self.musics = [stage1]

    def playSound(self,index):
        pygame.mixer.Sound.play(self.sounds[index])

    def playMusic(self,index):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.musics[index])
        pygame.mixer.music.play(-1)

    def stopMusic(self):
        pygame.mixer.music.stop()
