from modules.window import Window, Background, CoordinateManager
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

# create coordinate manager
coordinate_manager = CoordinateManager()

# Create a custom event for adding a new enemy every second
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

# Create a custom event for shooting projectiles every second
SHOOTPROJECTILE = pygame.USEREVENT + 2
pygame.time.set_timer(SHOOTPROJECTILE, 1000)

   
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
            new_enemy = Enemy(100, coordinate_manager._waypoints)
            win.all_sprites.add(new_enemy)
            win.enemies.add(new_enemy)
        # handle tower placing
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            valid_coordinate = coordinate_manager.is_coordinate_valid_placement_point(pos[0], pos[1], coordinate_manager._placement_blocks)
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
   

# Done! Time to quit.
pygame.quit()
