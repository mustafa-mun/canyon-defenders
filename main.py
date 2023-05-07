from modules.background import Background
from modules.window import Window
from modules.enemy import Enemy
from modules.tower import Tower, Projectile
from modules.player import Player
import pygame

pygame.init()

# Set up the drawing window
win = Window(1286, 768)
screen = win._screen

pygame.display.set_caption("Canyon Defenders")

# create background
background = Background("./assets/map.png", [0, 0])

# create player
player = Player()

# Create a custom event for adding a new enemy every second
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

# Create a custom event for shooting projectiles every second
SHOOTPROJECTILE = pygame.USEREVENT + 2
pygame.time.set_timer(SHOOTPROJECTILE, 1000)

# this will go into relative class or module
# check if tile coordinate in a placement tile range
def is_coordinate_valid_placement_point(x, y, coordinates):
    for block in coordinates:
        # get maximum coordinates
        max_x = block["x"] + block["width"]
        max_y = block["y"] + block["height"]
        # check if coordinates are in range
        if x >= block["x"] and x <= max_x and y >= block["y"] and y <= max_y:
            # coordinates are in range
            return block
    # coordinates are out of range
    print("Out ouf range")
    return False
   
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
        # handle tower placing
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            valid_coordinate = is_coordinate_valid_placement_point(pos[0], pos[1], background._placement_blocks)
            if valid_coordinate:
                x = valid_coordinate["x"] + (valid_coordinate["width"] / 2)
                y = valid_coordinate["y"] + (valid_coordinate["height"] / 2)
                new_tower = Tower(250,valid_coordinate["width"], valid_coordinate["height"], x, y)
                win.all_sprites.add(new_tower)
                win.towers.add(new_tower)

        # handle projectile shooting
        elif event.type == SHOOTPROJECTILE:
            for tower in win.towers:
                new_projectile = Projectile(tower)
                win.all_sprites.add(new_projectile)
                win.projectiles.add(new_projectile)
        
   
    # handle when player out of health
    if player.health <= 0:
        pass
        #running = False
    

    # add background
    screen.blit(background._image, background._rect)

    # draw all sprites
    for entity in win.all_sprites:
        screen.blit(entity._surf, entity.rect)
        
    # draw towers range
    for tower in win.towers:
        tower.draw_range_box(screen)
        for enemy in win.enemies:
            if tower.range_box.colliderect(enemy.rect):
                # handle shooting enemies
                pass
    # draw players health
    screen.blit(player.show_health(), (win._SCREEN_WIDTH - 75, 50))

    # make enemies move and draw their health
    for enemy in win.enemies:
        enemy.draw_health(screen, win)
        enemy.update(player)

    # make projectiles move
    for projectile in win.projectiles:
        projectile.update(win)
    
    # Flip the display
    pygame.display.flip()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Wait for the next frame
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
