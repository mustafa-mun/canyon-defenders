import pygame

class WaveController:
    # this numbers will be changed
    def __init__(self):
        self._wave_index = 0
        self._spawn_count = 0
        self._enemy_numbers = []
        self._populate_enemy_numbers()
        self._enemy_speeds = [2, 2, 3, 3, 4, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15]
        self._enemy_healths = [50, 75]
        self._populate_enemy_healths()
        self._enemy_rewards = [50, 50, 50, 60, 60, 70, 70, 70, 80, 80, 90, 90, 100, 100, 100]
        self._enemy_rate = [1000, 1000, 900, 850, 800, 650, 500, 400, 300, 300, 300, 200, 200, 200, 200]

    def _populate_enemy_numbers(self):
        base_number = 10
        for i in range(15):
            self._enemy_numbers.append(base_number)
            base_number += 5
    
    def _populate_enemy_healths(self):
        base_number = 100
        for i in range(15 - len(self._enemy_healths)):
            self._enemy_healths.append(base_number)
            base_number += 50
            
        print(self._enemy_healths)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, speed, reward, waypoints):
        super(Enemy, self).__init__()
        self.max_health = health
        self.health = health
        self._surf = pygame.Surface((25, 25))
        self._surf.fill((0, 0, 0))
        self.rect = self._surf.get_rect(
            center=(int(waypoints[0]["x"]), int(waypoints[0]["y"]))
        )
        self._reward = reward
        self._waypoints = waypoints
        self._target_waypoint = 0
        self._speed = speed

    def draw_health_bar(self, surf, pos, size, borderC, backC, healthC, progress):
        pygame.draw.rect(surf, backC, (*pos, *size))
        pygame.draw.rect(surf, borderC, (*pos, *size), 1)
        innerPos = (pos[0] + 1, pos[1] + 1)
        innerSize = ((size[0] - 2) * progress, size[1] - 2)
        rect = (
            round(innerPos[0]),
            round(innerPos[1]),
            round(innerSize[0]),
            round(innerSize[1]),
        )
        pygame.draw.rect(surf, healthC, rect)

    def draw_health(self, surf, win):
        # Check if sprite is still within the screen boundaries
        if self.rect.right < win._SCREEN_WIDTH - 3:
            healthrect = pygame.Rect(0, 0, self._surf.get_width(), 7)
            healthrect.midbottom = self.rect.centerx, self.rect.top
            self.draw_health_bar(
                surf,
                healthrect.topleft,
                healthrect.size,
                (0, 0, 0),
                (255, 0, 0),
                (0, 255, 0),
                self.health / self.max_health,
            )

    def update(self, player):
        # If health is 0 or less, kill enemy
        if self.health <= 0:
            # Increase players money
            player.money += self._reward
            self.kill()

        # Get the current target waypoint
        pos = self._waypoints[self._target_waypoint]

        # handle right
        if self.rect.x < pos["x"]:
            self.rect.move_ip(self._speed, 0)
        # handle left
        if self.rect.x > pos["x"]:
            self.rect.move_ip(-self._speed, 0)
        # handle bottom
        if self.rect.y < pos["y"]:
            self.rect.move_ip(0, self._speed)
        # handle top
        if self.rect.y > pos["y"]:
            self.rect.move_ip(0, -self._speed)

        # check if enemy has reached the current waypoint
        if (
            abs(self.rect.x - pos["x"]) <= self._speed
            and abs(self.rect.y - pos["y"]) <= self._speed
        ):
            # increment the target waypoint
            self._target_waypoint += 1
            # check if enemy has reached the end of waypoints list
            if self._target_waypoint >= len(self._waypoints):
                player.health -=1
                self.kill()
