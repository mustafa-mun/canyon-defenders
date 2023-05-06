import pygame

placement_tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0,
            0, 19, 19, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 19, 19, 0, 0, 19, 19, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 19, 19, 0, 0, 19, 19, 0]
two_d_tiles = []

for i in range(12):
    row = []
    for j in range(20):
        row.append(placement_tiles[i*20+j])
    two_d_tiles.append(row)
    
possible_placement_coordinates = []

for i in range(len(two_d_tiles)):
    for j in range(len(two_d_tiles[i])):
        if two_d_tiles[i][j] == 19:
            possible_placement_coordinates.append({ "x": j * 64, "y": i * 64 })

def is_coordinate_valid_placement_point(x, y):
    for pos in possible_placement_coordinates:
        # check if coordinate is between a placement tile
        if x >= pos["x"] and x <= pos["x"] + 64 and y >= pos["y"] and y <= pos["y"] + 64:
            print(pos)
            return True

is_coordinate_valid_placement_point(85, 63)

class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
      super(Tower, self).__init__()
      self._surf = pygame.Surface((25, 25))
      self._surf.fill((0, 0, 0))
      self._rect = self._surf.get_rect(
          center=(pos_x, pos_y)
        )