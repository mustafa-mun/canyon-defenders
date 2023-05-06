from modules.background import Background
from modules.window import Window
import pygame

pygame.init()

# Set up the drawing window
win = Window(1286, 768)
screen = win.screen

BackGround = Background("./assets/map.png", [0, 0])

waypoints = [
    {"x": -93.3333333333333, "y": 285.333333333333},
    {"x": 664, "y": 289.333333333333},
    {"x": 669.333333333333, "y": 528},
    {"x": 1360, "y": 534.666666666667},
]

# Create a custom event for adding a new enemy every second
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)


# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(int(waypoints[0]["x"]), int(waypoints[0]["y"]))
        )
        self.target_waypoint = 0
        self.speed = 5

    def update(self):
        # Get the current target waypoint
        pos = waypoints[self.target_waypoint]

        # handle right
        if self.rect.x < pos["x"]:
            self.rect.move_ip(self.speed, 0)
        # handle left
        if self.rect.x > pos["x"]:
            self.rect.move_ip(-self.speed, 0)
        # handle bottom
        if self.rect.y < pos["y"]:
            self.rect.move_ip(0, self.speed)
        # handle top
        if self.rect.y > pos["y"]:
            self.rect.move_ip(0, -self.speed)

        # check if enemy has reached the current waypoint
        if (
            abs(self.rect.x - pos["x"]) <= self.speed
            and abs(self.rect.y - pos["y"]) <= self.speed
        ):
            # increment the target waypoint
            self.target_waypoint += 1
            # check if enemy has reached the end of waypoints list
            if self.target_waypoint >= len(waypoints):
                self.kill()


running = True

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)

    # add background
    screen.blit(BackGround.image, BackGround.rect)

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # make enemies move
    # enemies.update()
    enemies.update()

    # Flip the display
    pygame.display.flip()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Wait for the next frame
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
