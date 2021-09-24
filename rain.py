import sys
import pygame
from settings import Settings
from raindrop import Raindrop
from random import randint

class Rain:
    """class to drive the program"""

    def __init__(self):
        """program variables"""
        pygame.init()
        #triggers to maintain drop deletion point
        self.trigger  = 0
        self.limit = 2
        #settings instance
        self.settings  = Settings()
        #window properties
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg = pygame.image.load(self.settings.bg)
        self.screen.get_rect()
        pygame.display.set_caption(self.settings.caption)
        #sprite group
        self.drops = pygame.sprite.Group()
        #creating initial row of raindrops
        self._create_row()
        #key press and release triggers
        self.increasing_speed = False
        self.decreasing_speed = False 
        
           
    def run_app(self):
        """main program loop"""
        while True:
            self._check_events()
            self._fall()
            self._drop_speed_update()
            self._update_screen()          
            

    def _check_events(self):
        """check for keyboard events"""
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """checking for key presses"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.increasing_speed = True
        if event.key == pygame.K_DOWN:
            self.decreasing_speed = True
        

    def _check_keyup_events(self, event):
        """checking for key releases"""
        if event.key == pygame.K_UP:
            self.increasing_speed = False
        if event.key == pygame.K_DOWN:
            self.decreasing_speed = False


    def _create_drop(self, drop_no):
        """raindrop producer"""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = (drop_width + 15)  * drop_no
        self.drops.add(drop)
         

    def _create_row(self):
        """creates the right number of raindrops on screen"""
        #calcutating number of drops
        drop = Raindrop(self)
        drop_width = drop.rect.width
        available_x_space = self.screen.get_rect().width - (32 * drop_width)
        possible_drops =int((available_x_space - 10 * drop.rect.x))
        #creating drops in rows at random positions
        for drop_no in range(possible_drops):
            if (drop_width + 15)  * drop_no  <= self.screen.get_rect().width and randint(0, 1) and randint(0, 1):
                self._create_drop(drop_no)
        

    def _remove_drop(self):
        """removing drop when it touches the ground"""
        for drop in self.drops.copy():
            if drop.check_ground():
                self.drops.remove(drop)
                self.trigger = 1
        #maintains last raindrop deletion point at the ground     
        if self.trigger:
            self.limit -= 1
            self.trigger = 0 
 

    def _fall(self):
        """creates rainfall and deletes drops when necessary"""
        self._remove_drop()
        for drop in self.drops.copy():
            drop.rainfall()
            if drop.next_set(self.limit):
                self.limit += 1
                self._create_row()


    def _drop_speed_update(self):
        """increasing the speed of each drop in sprite group"""
        if  self.increasing_speed and self.settings.drop_speed < 50:
            for drop in self.drops.sprites():
                self.settings.drop_speed += 0.01
        if self.decreasing_speed and self.settings.drop_speed > 2:
            for drop in self.drops.sprites():
                self.settings.drop_speed -= 0.01
            

    def _update_screen(self):
        """draw background and objects"""
        self.screen.fill(self.settings.bg_colour)
        self.screen.blit(self.bg, (0,0))
        self.drops.draw(self.screen)
        pygame.display.flip()



if __name__ == "__main__":
    rain = Rain()
    rain.run_app() 