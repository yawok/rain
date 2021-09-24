from pygame.sprite import Sprite
import pygame
from settings import Settings
drops = []
class Raindrop(Sprite):
    """class to manage raindrop properties"""
    
    def __init__(self, display):
        super().__init__()
        self.screen = display.screen
        self.settings = display.settings
        #loading raindrop image and setting rect
        self.image = pygame.image.load(self.settings.img)
        self.rect = self.image.get_rect()
        #setting initial position of raindrop
        self.rect.x = self.rect.width
        self.rect.y = -10
        self.y = float(self.rect.y)
        self.x = float(self.rect.x) 


    def check_ground(self):
        """checks if raindrop has touch ground"""
        if self.rect.bottom >= self.settings.ground_pos:
            return True
    

    def next_set(self, limit):
        """checks if next set of raindrops is ready to fall """
        if self.rect.bottom >= 100 * limit:
            limit += 1
            return True


    def rainfall(self):
        """creates rainfall effect"""
        self.y += self.settings.drop_speed
        self.rect.y = self.y

