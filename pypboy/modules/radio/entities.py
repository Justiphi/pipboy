import os
import game
import config
import pygame
import time
from random import choice


class RadioStation(game.Entity):

    STATES = {
        'stopped': 0,
        'playing': 1,
        'paused': 2
    }

    def __init__(self, *args, **kwargs):
        super(RadioStation, self).__init__((10, 10), *args, **kwargs)
        self.state = self.STATES['stopped']
        self.files = self.load_files()
        pygame.mixer.music.set_endevent(config.EVENTS['SONG_END'])

    def play_random(self):
        start_pos = 0
        f = False
        if config.SOUND_ENABLED:
            if hasattr(self, 'last_filename') and self.last_filename:
                pygame.mixer.music.load(self.last_filename)

                now = time.time()
                curpos = self.last_playpos + (now - self.last_playtime)
                # TODO
            f = choice(self.files)
            self.filename = f
            pygame.mixer.music.load(f)
            pygame.mixer.music.play(0, start_pos)
            self.state = self.STATES['playing']
        
    def play(self):
        if config.SOUND_ENABLED:
            if self.state == self.STATES['paused']:
                pygame.mixer.music.unpause()
                self.state = self.STATES['playing']
            else:
                self.play_random()
        
    def pause(self):
        if config.SOUND_ENABLED:
            self.state = self.STATES['paused']
            pygame.mixer.music.pause()
        
    def stop(self):
        if config.SOUND_ENABLED:
            self.state = self.STATES['stopped']
            if self.filename:
                self.last_filename = self.filename
                self.last_playpos = pygame.mixer.music.get_pos()
                self.last_playtime = time.time()
            pygame.mixer.music.stop()

    def load_files(self):
        files = []
        for f in os.listdir(self.directory):
            if f.endswith(".mp3") or f.endswith(".ogg") or f.endswith(".wav"):
                files.append(self.directory + f)
        print(files)
        return files

    def __le__(self, other):
        if type(other) is not RadioStation:
            return 0
        else:
            return self.label <= other.label
    
    def __ge__(self, other):
        if type(other) is not RadioStation:
            return 0
        else:
            return self.label >= other.label

class ClassicalRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Classical Radio'
        self.directory = 'sounds/radio/Classical/'
        super(ClassicalRadio, self).__init__(self, *args, **kwargs)

class DiamondCityRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Diamond City Radio'
        self.directory = 'sounds/radio/DCR/'
        super(DiamondCityRadio, self).__init__(self, *args, **kwargs)

class R76(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Radio 76'
        self.directory = 'sounds/radio/R76/'
        super(R76, self).__init__(self, *args, **kwargs)

class Playlist(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Radio JustiPhi'
        self.directory = 'sounds/radio/Playlist/'
        super(R76, self).__init__(self, *args, **kwargs)

class EnclaveRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Enclave Radio'
        self.directory = 'sounds/radio/Enclave/'
        super(EnclaveRadio, self).__init__(self, *args, **kwargs)

class InstituteRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Institute Radio'
        self.directory = 'sounds/radio/Institute/'
        super(InstituteRadio, self).__init__(self, *args, **kwargs)

class MinutemenRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Minutemen Radio'
        self.directory = 'sounds/radio/Minutemen/'
        super(MinutemenRadio, self).__init__(self, *args, **kwargs)

class Vault101Radio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Vault 101 Radio'
        self.directory = 'sounds/radio/V101/'
        super(Vault101Radio, self).__init__(self, *args, **kwargs)

class ViolinRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Violin Radio'
        self.directory = 'sounds/radio/Violin/'
        super(ViolinRadio, self).__init__(self, *args, **kwargs)

class F3Radio(RadioStation):
    def __init__(self, *args, **kwargs):
        
        self.label = 'F3 Radio'
        self.directory = 'sounds/radio/F3/'
        super(F3Radio, self).__init__(self, *args, **kwargs)