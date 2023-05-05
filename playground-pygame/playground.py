# Import and initialize the pygame library
import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background("./assets/background.png", [0, 0])

hero_png = pygame.image.load("./assets/hero.png").convert_alpha()
hero_png = pygame.transform.scale(hero_png, (125, 125))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = hero_png
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -15)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 15)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-15, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(15, 0)

        # dont let plyer to go off screen
        # handle left screen
        if self.rect.left < 0:
            self.rect.left = 0
        # handle right screen
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        # handle top screen
        if self.rect.top < 0:
            self.rect.top = 0
        # handle bottom screen
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


enemy_png = pygame.image.load("./assets/enemy.png").convert_alpha()
enemy_png = pygame.transform.scale(enemy_png, (125, 125))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = enemy_png
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(20, 35)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


new_player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(new_player)
# Run until the user asks to quit
running = True
# MAIN LOOP
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user pressed any key
        if event.type == KEYDOWN:
            # Is this key ESC?
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

        # add a new enemy
        elif event.type == ADDENEMY:
            # create new enemy and add it on sprite group
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    new_player.update(pressed_keys)
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(new_player, enemies):
        # remove the player and stop the loop
        new_player.kill()
        running = False

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Flip everything to the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)
    # make all enemies move
    enemies.update()
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
