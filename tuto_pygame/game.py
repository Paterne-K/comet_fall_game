from itertools import groupby
import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager

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
        self.score = 0
        self.sound_manager = SoundManager()

        # Create a group of monsters
        self.all_monsters = pygame.sprite.Group()


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score (self, points=10):
        self.score += points


    def game_over(self):
        # Restart the game (remove monsters, set player's health to 100, pause the game)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.add_reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play("game_over")


    def update(self, screen):
        # Display score on screen
        font = pygame.font.SysFont("monospace", 25)
        score_text = font.render(f"Score: {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20, 20))

        # Apply player image
        screen.blit(self.player.image, self.player.rect)

        #update player health bar
        self.player.update_health_bar(screen)

        # Update game event bar
        self.comet_event.update_bar(screen)

        # update player animation
        self.player.update_animation()

        # move projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # move monsters
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

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

    def spawn_monster(self, monster_class_name):
        #monster = Mummy(self)
        self.all_monsters.add(monster_class_name.__call__(self))