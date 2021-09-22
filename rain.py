import sys
import pygame
from settings import Settings

class Rain:
    """main class to drive the program"""

    def __init__(self):
        """program variables"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg = pygame.image.load("bg_img.png")
        self.screen.get_rect()
        pygame.display.set_caption("Rain")
        self.settings = Settings()

    def run_app(self):
        """main program loop"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """check for keyboard events"""
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                pass


    def _check_keydown_events(self, event):
        """check for key presses"""
        if event.key == pygame.K_q:
            sys.exit()


    def _update_screen(self):
        """draw background and objects"""
        self.screen.blit(self.bg, (0,0))
        #self.screen.fill(self.settings.bg_colour)
        pygame.display.flip()



if __name__ == "__main__":
    rain = Rain()
    rain.run_app() 