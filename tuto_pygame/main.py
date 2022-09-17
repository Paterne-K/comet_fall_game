import pygame
import math
from game import Game
pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 90


# Loading the window
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("assets/bg.jpg")

# Import the banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# Import Play Button
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.7)

game = Game()
running = True

while running:

    # Apply Game background
    screen.blit(background, (0,-200))

    # Check if the game has started or not
    if game.is_playing:

        # Start the game
        game.update(screen)
    else:
        # Add Welcome Screen
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # Update the window
    pygame.display.flip()


    # In case player close the window
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing Game window")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Check if space is pressed
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()

                else:
                    # Run the game
                    game.start()

                    # Play sound
                    game.sound_manager.play("click")

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checking if the mouse collides the play button
            if play_button_rect.collidepoint(event.pos):

                # Run the game
                game.start()

                # Play sound
                game.sound_manager.play("click")

    # Fix the number of FPS of the clock
    clock.tick(FPS)