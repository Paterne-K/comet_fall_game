import pygame
from projectile import Projectile
import animation


# Player Creation
class Player(animation.AnimateSprite):
    
    def  __init__(self, game) :
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        self.health -= amount

        if self.health <=0:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # define a color for our health bar (green)
        bar_color = (111, 210, 46)

        # define a color for our back bar
        back_bar_color = (60, 63, 60)

        # define our health bar position, width and thickness
        bar_position = [self.rect.x+50, self.rect.y+20, self.health, 7]
        back_bar_position = [self.rect.x+50, self.rect.y+20, self.max_health, 7]

        # draw our health bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        # instantiate projectile class
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        # Start animation
        self.start_animation()

        # Play sound
        self.game.sound_manager.play("tir")

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity