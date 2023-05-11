import pygame

class Tower(pygame.sprite.Sprite):
  def __init__(self, price, range, damage, image_file, shooting_speed, shooting_rate, width, height, pos_x, pos_y):
    super(Tower, self).__init__()
    self._image_file = image_file
    self._pos_x = pos_x
    self._pos_y = pos_y
    self._surf = pygame.image.load(image_file).convert_alpha() # Load image file
    self._surf = pygame.transform.scale(self._surf, (width, height * 2)) # Resize image to match original surface
    self.rect = self._surf.get_rect(
        center=(pos_x, pos_y - (height // 2))
    )
    self.shoot_timer = 0
    self._shooting_rate = shooting_rate
    self._shooting_speed = shooting_speed
    self._damage = damage
    self._price = price    
    self.range_box = pygame.Rect(pos_x - (width // 2) - (range // 2),
                                     pos_y - (height // 2) - (range // 2),
                                     width + range,
                                     height + range)

  def draw_range_box(self, screen):
      # detect mouse hover over tower
      mouse_pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(mouse_pos):
          # set flag to draw range box
          draw_range = True
      else:
          # clear flag to not draw range box
          draw_range = False

      # draw range box if flag is set
      if draw_range:
          pygame.draw.rect(screen, (255, 255, 255), self.range_box, 1)




      
class Projectile(pygame.sprite.Sprite):
  def __init__(self,tower, enemy):
    super(Projectile, self).__init__()
    self._tower = tower
    self._enemy = enemy
    self._surf = pygame.image.load('assets/shoot.png').convert_alpha() # Load image file
    self._surf = pygame.transform.scale(self._surf, (25, 25)) # Resize image to match original surface
    self.rect = self._surf.get_rect(
       center =(self._tower._pos_x, self._tower._pos_y)
    )
    self._speed = self._tower._shooting_speed

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
        
        