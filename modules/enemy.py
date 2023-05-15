import pygame

class WaveController:

    def __init__(self):
        self._wave_index = 0
        self._spawn_count = 0
        self._enemy_numbers = []
        self._populate_enemy_numbers()
        self._enemy_speeds = [3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8]
        self._enemy_healths = []
        self._populate_enemy_healths()
        self._enemy_rewards = [50, 50, 45, 45, 45, 45, 45, 45, 45, 35, 35, 35, 30, 30, 25]
        self._enemy_rate = [1000, 1000, 900, 850, 800, 750, 650, 650, 600, 550, 550, 500, 500, 450, 400]
        self.font = pygame.font.Font('assets/font.ttf', 22)
        self.img = pygame.image.load('assets/enemy.png').convert_alpha()
        self.scaled_img = pygame.transform.scale(self.img, (45, 45))

    def _populate_enemy_numbers(self):
        base_number = 10
        for i in range(15):
            self._enemy_numbers.append(base_number)
            base_number += 7
    
    def _populate_enemy_healths(self):
        base_number = 50
        for i in range(15):
            self._enemy_healths.append(base_number)
            base_number += 65
            
    def draw_wave_info(self, screen):
        wave = self.font.render(f"#{str(self._wave_index + 1)}", True, (255, 255, 255))
        wave_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        wave_surface.blit(wave, (50, 15))
        wave_surface.blit(self.scaled_img, (0, 0))
        screen.blit(wave_surface, (25, 125))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, speed, reward, waypoints):
        super(Enemy, self).__init__()
        self.max_health = health
        self.health = health
        self._frame_width = 85
        self._frame_height = 85
        self._num_frames = 7
        self._current_frame = 0
        self._load_sprite_sheet()
        self.rect = self._surf.get_rect(center=(int(waypoints[0]["x"]), int(waypoints[0]["y"])))
        self._reward = reward
        self._waypoints = waypoints
        self._target_waypoint = 0
        self._speed = speed


  

    def draw_health_bar(self, surf, pos, size, borderC, backC, healthC, progress):
        pygame.draw.rect(surf, backC, (*pos, *size))
        pygame.draw.rect(surf, borderC, (*pos, *size), 1)
        innerPos = (pos[0] + 1, pos[1] + 1)
        innerSize = ((size[0] -2) * progress, size[1] -2)
        rect = (
            round(innerPos[0]),
            round(innerPos[1]),
            round(innerSize[0]),
            round(innerSize[1]),
        )
        pygame.draw.rect(surf, healthC, rect)


    def _load_sprite_sheet(self):
        sprite_sheet = pygame.image.load('assets/orc.png').convert_alpha()
        self._sprite_sheet = pygame.transform.scale(sprite_sheet, (self._frame_width * self._num_frames, self._frame_height))
        self._surf = self._sprite_sheet.subsurface(pygame.Rect(0, 0, self._frame_width, self._frame_height))
 
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
         # Animate the enemy
        self._current_frame = (self._current_frame + 1) % self._num_frames
        x = self._current_frame * self._frame_width
        y = 0  # Adjust if the frames are not in the first row
        self._surf = self._sprite_sheet.subsurface(pygame.Rect(x, y, self._frame_width, self._frame_height))

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
