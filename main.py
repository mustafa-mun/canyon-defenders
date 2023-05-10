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

# handle framerate
clock = pygame.time.Clock()

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
            # create new enemy 
            new_enemy = Enemy(100, 2, 50, coordinate_manager._waypoints)
            win.all_sprites.add(new_enemy)
            win.enemies.add(new_enemy)
        # handle tower buy 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            pos = pygame.mouse.get_pos()

            for i in range(len(coordinate_manager.buy_tower_coords)):
                x = win._SCREEN_WIDTH//2 - coordinate_manager.buy_tower_coords[i]["tower"].get_width()//2 + (i-1.5)*1.5*coordinate_manager.buy_tower_coords[i]["tower"].get_width()
                y = 15
                # check if user clicked a tower buy image
                if x < pos[0] < x + coordinate_manager.buy_tower_coords[i]["tower"].get_width() and y < pos[1] < y + coordinate_manager.buy_tower_coords[i]["tower"].get_height():
            
                    win.mouse_pressed = True
                    print(f"Tower price => {coordinate_manager.buy_tower_coords[i]['tower_price']}")
                    win.purchased_tower = coordinate_manager.determine_tower(coordinate_manager.buy_tower_coords[i]['tower_price'], coordinate_manager.buy_tower_coords[i]["tower"])

        # handle drop 
        elif event.type == pygame.MOUSEBUTTONUP:
            win.mouse_pressed = False
            # get mouse position
            pos = pygame.mouse.get_pos()

            # check if mouse coordinate is valid
            valid_coordinate = coordinate_manager.is_coordinate_valid_placement_point(pos[0], pos[1], coordinate_manager._placement_blocks)
            if valid_coordinate:
                # if player purchased a tower
                if win.purchased_tower:
                    # if player has enough money
                    if player.money >= win.purchased_tower["price"]:
                        player.money -= win.purchased_tower["price"]
                        # player have money
                        # coordinate is valid, create new tower 
                        x = valid_coordinate["x"] + (valid_coordinate["width"] / 2)
                        y = valid_coordinate["y"] + (valid_coordinate["height"] / 2)
                        # create new tower with purchased tower 
                        new_tower = Tower(win.purchased_tower["range"], win.purchased_tower["damage"], win.purchased_tower["img"], win.purchased_tower["shooting_speed"], win.purchased_tower["shooting_rate"], valid_coordinate["width"], valid_coordinate["height"], x, y)
                        win.all_sprites.add(new_tower)
                        win.towers.add(new_tower)
                    else:
                        print("you don't have enough money")

    # handle dragging purchased tower 
    if win.mouse_pressed:
        # get mouse position
        pos = pygame.mouse.get_pos()
        # calculate the position of the top-left corner of the tower image
        x = pos[0] - win.purchased_tower["surface"].get_width() // 2
        y = pos[1] - win.purchased_tower["surface"].get_height() // 2
        # blit the tower image to the screen at the new position
        screen.blit(win.purchased_tower["surface"], (x, y))
        pygame.display.update()

    # handle when player out of health
    if player.health <= 0:
        pass
   

    # add background
    screen.blit(background._image, background._rect)

    # draw all sprites
    for entity in win.all_sprites:
        screen.blit(entity._surf, entity.rect)
        
    # add projectiles to enemies in range
    for tower in win.towers:
        tower.draw_range_box(screen)
        # find the enemies in towers range
        range_enemies = [enemy for enemy in win.enemies if tower.range_box.colliderect(enemy.rect)]
        # set towers shooting rate delay
        if tower.shoot_timer >= tower._shooting_rate:
            tower.shoot_timer = 0
            if range_enemies:
                # shoot projectile to first locked out enemy
                new_projectile = Projectile(tower, range_enemies[0])
                win.all_sprites.add(new_projectile)
                win.projectiles.add(new_projectile)
        else:
            tower.shoot_timer += 1
    
    # shoot all projectiles
    for projectile in win.projectiles:
        if projectile._enemy.rect.x > 0:
            # projectile folllows the enemy
            projectile.update()
            if projectile.rect.colliderect(projectile._enemy.rect):
                # when projectile hits the enemy, reflect the damage to enemy and kill the projectile
                projectile._enemy.health -= projectile._tower._damage
                projectile.kill()

    # draw players health
    screen.blit(player.show_health(), (25, 25))
    # draw players money
    screen.blit(player.show_money(), (25, 75))
    # draw towers to buy
    coordinate_manager.show_tower_buy(screen, win)
    # make enemies move and draw their health
    for enemy in win.enemies:
        enemy.draw_health(screen, win)
        enemy.update(player)
    
   # set framerate to 60 
    clock.tick(60)
    # Flip the display
    pygame.display.flip()
   

# Done! Time to quit.
pygame.quit()
