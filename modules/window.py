import pygame

class Window:
    def __init__(self, width, height):
        self._SCREEN_WIDTH = width
        self._SCREEN_HEIGHT = height
        self._screen = pygame.display.set_mode(
            [self._SCREEN_WIDTH, self._SCREEN_HEIGHT]
        )
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self._image = pygame.image.load(image_file)
        self._rect = self._image.get_rect()
        self._rect.left, self._rect.top = location
       

class CoordinateManager:
    def __init__(self):
        self._waypoints = [
            {"x": -93.3333333333333, "y": 285.333333333333},
            {"x": 664, "y": 289.333333333333},
            {"x": 669.333333333333, "y": 528},
            {"x": 1360, "y": 534.666666666667},
        ]
        self._placement_blocks = [
   {
        "height":125,
        "width":122,
        "x":68,
        "y":63
    }, 
    {
        "height":125,
        "width":125,
        "x":322,
        "y":65
    }, 
    {
        "height":123,
        "width":128,
        "x":66,
        "y":386
    }, 
    {
        "height":124,
        "width":126,
        "x":321,
        "y":385
    }, 
    {
        "height":122,
        "width":125,
        "x":834,
        "y":195
    }, 
    {
        "height":122,
        "width":124,
        "x":1027,
        "y":323
    }, 
    {
        "height":124,
        "width":124,
        "x":578,
        "y":643
    }, 
    {
        "height":122,
        "width":123,
        "x":836,
        "y":643
    }, 
    {
        "height":126,
        "width":123,
        "x":1093,
        "y":642
    }]
        
    # check if tile coordinate in a placement tile range
    def is_coordinate_valid_placement_point(self, x, y, coordinates):
        for block in coordinates:
            # get maximum coordinates
            max_x = block["x"] + block["width"]
            max_y = block["y"] + block["height"]
            # check if coordinates are in range
            if x >= block["x"] and x <= max_x and y >= block["y"] and y <= max_y:
                # coordinates are in range
                return block
        # coordinates are out of range
        print("Out ouf range")
        return False

