import pygame

class Tower(pygame.sprite.Sprite):
  def __init__(self, range, damage, width, height, pos_x, pos_y):
    super(Tower, self).__init__()
    self._pos_x = pos_x
    self._pos_y = pos_y
    self._surf = pygame.Surface((width, height))
    self._surf.fill((0, 0, 0))
    self.rect = self._surf.get_rect(
        center=(pos_x, pos_y)
    )
    self._damage = damage    
    self.range_box = pygame.Rect(pos_x - (width // 2) - (range // 2),
                                     pos_y - (height // 2) - (range // 2),
                                     width + range,
                                     height + range)

  def draw_range_box(self, screen):
    # this method will be removed after tests
    pygame.draw.rect(screen, (255, 255, 255), self.range_box, 1)




      
class Projectile(pygame.sprite.Sprite):
  def __init__(self,tower, enemy):
    super(Projectile, self).__init__()
    self._tower = tower
    self._enemy = enemy
    self._surf = pygame.Surface((10, 10))
    self._surf.fill((0, 0, 0))
    self.rect = self._surf.get_rect(
       center =(self._tower._pos_x, self._tower._pos_y)
    )
    self._speed = 5

  def update(self):
        # move only if enemy is in tower range
        if self._enemy.rect.x <= self._tower.range_box.right:
           # handle right
          if self.rect.x < self._enemy.rect.x:
              self.rect.move_ip(self._speed, 0)
          # handle left
          if self.rect.x > self._enemy.rect.x:
              self.rect.move_ip(-self._speed, 0)
          # handle bottom
          if self.rect.y < self._enemy.rect.y:
              self.rect.move_ip(0, self._speed)
          # handle top
          if self.rect.y > self._enemy.rect.y:
              self.rect.move_ip(0, -self._speed)
        else:
           self.kill()
        
        