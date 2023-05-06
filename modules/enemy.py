import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints):
        super(Enemy, self).__init__()
        self._surf = pygame.Surface((25, 25))
        self._surf.fill((0, 0, 0))
        self._rect = self._surf.get_rect(
            center=(int(waypoints[0]["x"]), int(waypoints[0]["y"]))
        )
        self._waypoints = waypoints
        self._target_waypoint = 0
        self._speed = 5

    def update(self):
        # Get the current target waypoint
        pos = self._waypoints[self._target_waypoint]

        # handle right
        if self._rect.x < pos["x"]:
            self._rect.move_ip(self._speed, 0)
        # handle left
        if self._rect.x > pos["x"]:
            self._rect.move_ip(-self._speed, 0)
        # handle bottom
        if self._rect.y < pos["y"]:
            self._rect.move_ip(0, self._speed)
        # handle top
        if self._rect.y > pos["y"]:
            self._rect.move_ip(0, -self._speed)

        # check if enemy has reached the current waypoint
        if (
            abs(self._rect.x - pos["x"]) <= self._speed
            and abs(self._rect.y - pos["y"]) <= self._speed
        ):
            # increment the target waypoint
            self._target_waypoint += 1
            # check if enemy has reached the end of waypoints list
            if self._target_waypoint >= len(self._waypoints):
                self.kill()
