import pygame
from comet import Comet

# Class to handle comet event
class CometFallEvent:

    def __init__(self, game) -> None:
        self.percent = 0
        self.percent_speed  = 5
        self.game = game
        self.fall_mode = False

        # Define a group of sprites to store comets
        self.all_comets = pygame.sprite.Group()


    def add_reset_percent(self):
        self.percent = 0

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent>=100

    def meteor_fall(self):
        #iterating between 1 and 10
        for i in range(1,10):
            # display a fireball
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters)==0:
            print("Comet Rain")
            self.meteor_fall()
            #self.add_reset_percent()
            self.fall_mode = True # Activate the event

    def update_bar(self, surface):

        # Add percent to the bar
        self.add_percent()

        # Calling the method to attempt fall
        #self.attempt_fall()

        # Black Background bar
        pygame.draw.rect(surface, (0,0,0), [
            0, 
            surface.get_height() - 20,
            surface.get_width(),
            10
            ])

        # Red Event bar
        pygame.draw.rect(surface, (187,11,11), [
            0, 
            surface.get_height() - 20,
            (surface.get_width()/100)*self.percent,
            10
            ])