import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
      super(Player, self).__init__()
      self.health = 10
      self.money = 0

    def show_health(self):
       font = pygame.font.Font('freesansbold.ttf', 35)
       health = font.render(f"HEALTH: {str(self.health)}", True, (0, 0, 0))
       return health
    
    def show_money(self):
       font = pygame.font.Font('freesansbold.ttf', 35)
       money = font.render(f"MONEY: {str(self.money)}", True, (0, 0, 0))
       return money

