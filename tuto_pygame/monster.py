import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 970 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)


    def damage(self, amount):
        
        # monster taking damages
        self.health -= amount

        # Check if the monster should disappear
        if self.health <= 0:
            
            # The old monster disappear but a new one appear
            self.rect.x = 970 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

            # check if the event bar is fully loaded
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # define a color for our health bar (green)
        bar_color = (111, 210, 46)

        # define a color for our back bar
        back_bar_color = (60, 63, 60)

        # define our health bar position, width and thickness
        bar_position = [self.rect.x+11, self.rect.y-20, self.health, 5]
        back_bar_position = [self.rect.x+11, self.rect.y-20, self.max_health, 5]

        # draw our health bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        
        else: 
            self.game.player.damage(self.attack)