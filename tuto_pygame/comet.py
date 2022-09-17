import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event) -> None:
        super().__init__()

        # Define the image 
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(30, 800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
         self.comet_event.all_comets.remove(self)


         # verify if the number of comets if 0
         if len(self.comet_event.all_comets) == 0:
             self.comet_event.add_reset_percent()

             # display monsters
             self.comet_event.game.spawn_monster()
             self.comet_event.game.spawn_monster()
             self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # Check if the comet it the ground
        if self.rect.y >= 510:
           self.remove()

           # if there is no more comet
           if len(self.comet_event.all_comets) == 0:
               # reset comet bar
               self.comet_event.add_reset_percent()
               self.comet_event.fall_mode = False


        # check if comet touches the player
        if self.comet_event.game.check_collision(
            self,
            self.comet_event.game.all_players
            ):
            print("player touched")
            self.remove()

            # damages to player
            self.comet_event.game.player.damage(20)