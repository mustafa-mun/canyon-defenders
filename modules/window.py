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
                        {
                         "x":-126.666666666667,
                         "y":418.666666666667
                        }, 
                        {
                         "x":220,
                         "y":412
                        }, 
                        {
                         "x":224,
                         "y":225.333333333333
                        }, 
                        {
                         "x":538.666666666667,
                         "y":225.333333333333
                        }, 
                        {
                         "x":541.333333333333,
                         "y":602.666666666667
                        }, 
                        {
                         "x":1054.66666666667,
                         "y":604
                        }, 
                        {
                         "x":1056,
                         "y":418.666666666667
                        }, 
                        {
                         "x":1321.33333333333,
                         "y":410.666666666667
                        }]
        self._placement_blocks = [
                {
                 "height":63,
                 "width":128,
                 "x":321,
                 "y":321,
                 "is_placed": False
                }, 
                {
                 "height":63,
                 "width":128,
                 "x":320,
                 "y":449,
                 "is_placed": False
                }, 
                {
                 "height":64,
                 "width":129,
                 "x":320,
                 "y":577,
                 "is_placed": False
                }, 
                {
                 "height":61,
                 "width":125,
                 "x":642,
                 "y":258,
                 "is_placed": False
                }, 
                {
                 "height":63,
                 "width":127,
                 "x":641,
                 "y":449,
                 "is_placed": False
                }, 
                {
                 "height":64,
                 "width":127,
                 "x":833,
                 "y":447,
                 "is_placed": False
                }, 
                {
                 "height":63,
                 "width":124,
                 "x":1025,
                 "y":256,
                 "is_placed": False
                }, 
                {
                 "height":64,
                 "width":126,
                 "x":1153,
                 "y":512,
                 "is_placed": False
                }, 
                {
                 "height":64,
                 "width":128,
                 "x":449,
                 "y":64,
                 "is_placed": False
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
                if block["is_placed"]:
                    # there is already a tower placed
                    print("already placed")
                    return False
                else:
                 block["is_placed"] = True
                 return block
        # coordinates are out of range
        print("out of range")
        return False

