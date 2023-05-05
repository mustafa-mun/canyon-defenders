import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background("./assets/game-map.png", [0, 0])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # add background
    screen.blit(BackGround.image, BackGround.rect)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
