import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
      super(Player, self).__init__()
      self.health = 10
      self.money = 0

    def show_health(self):
       font = pygame.font.Font('freesansbold.ttf', 40)
       health = font.render(str(self.health), True, (255, 0, 0))
       return health
