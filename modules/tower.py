import pygame

class Tower(pygame.sprite.Sprite):
  def __init__(self, range, width, height, pos_x, pos_y):
    super(Tower, self).__init__()
    self._pos_x = pos_x
    self._pos_y = pos_y
    self._surf = pygame.Surface((width, height))
    self._surf.fill((0, 0, 0))
    self.rect = self._surf.get_rect(
        center=(pos_x, pos_y)
    )    
    self.range_box = pygame.Rect(pos_x - (width // 2) - (range // 2),
                                     pos_y - (height // 2) - (range // 2),
                                     width + range,
                                     height + range)

  def draw_range_box(self, screen):
    # this method will be removed after tests
    pygame.draw.rect(screen, (255, 255, 255), self.range_box, 1)




      
class Projectile(pygame.sprite.Sprite):
  def __init__(self,tower):
    super(Projectile, self).__init__()
    self._tower = tower
    self._surf = pygame.Surface((10, 10))
    self._surf.fill((0, 0, 0))
    self.rect = self._surf.get_rect(
       center =(self._tower._pos_x, self._tower._pos_y)
    )
    self._speed = 5

  def update(self, screen):

    self.rect.move_ip(self._speed,0)

    if self.rect.x < 0 or self.rect.x > screen._SCREEN_WIDTH:
      self.kill()

    if self.rect.y < 0 or self.rect.y > screen._SCREEN_HEIGHT:
      self.kill()  