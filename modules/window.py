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
        self.buy_tower_coords = []
        self.purchased_tower = None

    def show_tower_buy(self, screen):
        tower_images = [
            "assets/towers/tower-1.png",
            "assets/towers/tower-2.png",
            "assets/towers/tower-3.png",
            "assets/towers/tower-4.png"
        ]
        tower_costs = [250, 500, 1000, 2500]
        font = pygame.font.Font('freesansbold.ttf', 21)

        for i in range(len(tower_images)):
            image = pygame.image.load(tower_images[i]).convert_alpha()
            scaled = pygame.transform.scale(image, (100, 100))
            cost_text = font.render(f'${tower_costs[i]}', True, (255, 255, 255))
            scaled_x = self._SCREEN_WIDTH//2 - scaled.get_width()//2 + (i-1.5)*1.5*scaled.get_width()
            scaled_y = 15
            cost_text_x = self._SCREEN_WIDTH//2 - cost_text.get_width()//2 + (i-1.5)*1.5*scaled.get_width()
            cost_text_y = 125
            screen.blit(scaled, (scaled_x, scaled_y))
            screen.blit(cost_text, (cost_text_x, cost_text_y))
            # make sure to send coordinates maximum tower images length
            if len(self.buy_tower_coords) <= len(tower_images):
                # send image coordinates to buy tower coordinates
                dict = {}
                dict["tower"] = scaled
                dict["tower_price"] = tower_costs[i]
                self.buy_tower_coords.append(dict)
   

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
                 "height":64,
                 "id":40,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":128,
                 "x":320,
                 "y":320
                }, 
                {
                 "height":63,
                 "id":41,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":127,
                 "x":322,
                 "y":449
                }, 
                {
                 "height":63,
                 "id":42,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":126,
                 "x":320,
                 "y":577
                }, 
                {
                 "height":63,
                 "id":43,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":126,
                 "x":642,
                 "y":447
                }, 
                {
                 "height":65,
                 "id":44,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":129,
                 "x":640,
                 "y":256
                }, 
                {
                 "height":64,
                 "id":45,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":127,
                 "x":1025,
                 "y":255
                }, 
                {
                 "height":62,
                 "id":46,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":125,
                 "x":1154,
                 "y":514
                }, 
                {
                 "height":63,
                 "id":47,
                 "name":"",
                 "rotation":0,
                 "type":"",
                 "is_placed":False,
                 "width":129,
                 "x":832,
                 "y":448
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


