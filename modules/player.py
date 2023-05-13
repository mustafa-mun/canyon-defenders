import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
      super(Player, self).__init__()
      self.health = 10
      # default money
      self.money = 250
      self.font = pygame.font.Font('assets/font.ttf', 22)
      self.health_icon = pygame.image.load('assets/heart.png').convert_alpha()
      self.health_icon_scaled = pygame.transform.scale(self.health_icon, (35, 35))
      self.money_icon = pygame.image.load('assets/coin.png').convert_alpha()
      self.money_icon_scaled = pygame.transform.scale(self.money_icon, (35, 35))


    def draw_player_info(self, screen):
      # Draw health
      health = self.font.render(str(self.health), True, (255, 255, 255))
      health_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
      health_surface.blit(health, (50, 7))
      health_surface.blit(self.health_icon_scaled, (0, 0))
      health_surface.set_colorkey((0, 0, 0))  # Make surface transparent

      # Draw money
      money = self.font.render(str(self.money), True, (255, 255, 255))
      money_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
      money_surface.blit(money, (50, 7))
      money_surface.blit(self.money_icon_scaled, (0, 0))
      money_surface.set_colorkey((0, 0, 0))  # Make surface transparent

      # Combine health and money surfaces
      player_info_surface = pygame.Surface((200, 100), pygame.SRCALPHA)
      player_info_surface.blit(health_surface, (0, 0))
      player_info_surface.blit(money_surface, (0, 50))

      screen.blit(player_info_surface, (25, 25))