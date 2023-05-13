import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
      super(Player, self).__init__()
      self.health = 10
      # default money
      self.money = 250

    def show_health(self):
       font = pygame.font.Font('freesansbold.ttf', 32)
       img = pygame.image.load('assets/heart.png').convert_alpha()
       scaled_img = pygame.transform.scale(img, (35, 35))
       health = font.render(f"{str(self.health)}", True, (255, 255, 255))
       return health, scaled_img
    
    def show_money(self):
       font = pygame.font.Font('freesansbold.ttf', 32)
       img = pygame.image.load('assets/coin.png').convert_alpha()
       scaled_img = pygame.transform.scale(img, (35, 35))
       money = font.render(f"{str(self.money)}", True, (255, 255, 255))
       return money, scaled_img

