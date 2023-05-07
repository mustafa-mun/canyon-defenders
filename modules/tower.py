import pygame

class Tower(pygame.sprite.Sprite):
    # add price data member 
    def __init__(self, range, width, height, pos_x, pos_y):
      super(Tower, self).__init__()
      self._range = range
      self._surf = pygame.Surface((width, height))
      self._surf.fill((0, 0, 0))
      self._rect = self._surf.get_rect(
          center=(pos_x, pos_y)
        )