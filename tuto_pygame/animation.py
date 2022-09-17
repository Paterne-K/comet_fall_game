import pygame

# Class to handle animations
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size = (200, 200)) -> None:
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # Begin animation with the first image
        self.images = animations.get(sprite_name)
        self.animation = False

    # Define a method to start animation
    def start_animation(self):
        self.animation = True


    # Define a method to animate the sprite
    def animate(self, loop=False):

        # Check if animation is active
        if not self.animation:
            return

        # Go to the next image
        self.current_image += 1

        # Check if we reached the end of the animation, restart
        if self.current_image >= len(self.images):
            self.current_image = 0

            if loop is False:
                # disable animation
                self.animation = False

        # Modify the previous image by the next one
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, self.size)


# Define a function to load image of a sprite
def load_animation_images(sprite_name):
    # load 24 images of this sprite from the corresponding folder
    images = []

    # Get the folder path of this sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # Iterate all the images in the folder and add them to the list
    for num in range(1,24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # Return the content of the image list
    return images


# Define a dict that will contains loaded images of each sprite
animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
    }