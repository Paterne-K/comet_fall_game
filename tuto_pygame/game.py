from itertools import groupby
import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

# Game Creation
class Game:
    def __init__(self) :

        # Define if the game has started
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.comet_event = CometFallEvent(self)

        # Create a group of monsters
        self.all_monsters = pygame.sprite.Group()


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # Restart the game (remove monsters, set player's health to 100, pause the game)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.add_reset_percent()
        self.is_playing = False


    def update(self, screen):
        
        # Apply player image
        screen.blit(self.player.image, self.player.rect)

        #update player health bar
        self.player.update_health_bar(screen)

        # Update game event bar
        self.comet_event.update_bar(screen)

        # move projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # move projectiles
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # get all comets 
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Apply all projectiles
        self.player.all_projectiles.draw(screen)

        # Apply all monsters
        self.all_monsters.draw(screen)

        # Apply all comets
        self.comet_event.all_comets.draw(screen)

        # Checking pressed keys
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= screen.get_width()-self.player.rect.width:
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x>=0:
            self.player.move_left()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)