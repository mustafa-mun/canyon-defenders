from modules.background import Background
from modules.window import Window
from modules.enemy import Enemy
import pygame
import math

pygame.init()

# Set up the drawing window
win = Window(1286, 768)
screen = win._screen

pygame.display.set_caption("Canyon Defenders")

# create background
background = Background("./assets/map.png", [0, 0])

# Create a custom event for adding a new enemy every second
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)


placement_tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 19, 19, 0, 0, 19, 19, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 19, 19, 0, 0, 19, 19, 0]

two_d_placement_tiles = []

list = []
for i in range(len(placement_tiles)):
    if len(list) == 20:
        two_d_placement_tiles.append(list)
        list = []
    else:
        list.append(placement_tiles[i])
    


print(two_d_placement_tiles)

# main game loop
running = True
while running:
    # get events
    for event in pygame.event.get():
        # handle quit
        if event.type == pygame.QUIT:
            running = False
        # handle enemy spawn
        elif event.type == ADDENEMY:
            new_enemy = Enemy(100, background._waypoints)
            win.all_sprites.add(new_enemy)
            win.enemies.add(new_enemy)

    # add background
    screen.blit(background._image, background._rect)

    # draw all sprites
    for entity in win.all_sprites:
        screen.blit(entity._surf, entity._rect)

    # make enemies move
    win.enemies.update()

    for enemy in win.enemies:
        enemy.draw_health(screen, win)

    # Flip the display
    pygame.display.flip()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Wait for the next frame
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
