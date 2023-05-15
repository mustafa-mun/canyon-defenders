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
        self.mouse_pressed = False
        self.purchased_tower = None


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self._image = pygame.image.load(image_file)
        self._rect = self._image.get_rect()
        self._rect.left, self._rect.top = location
       

class CoordinateManager:
    def __init__(self):
        self.buy_tower_coords = []
        self.tower_images = [
            "assets/towers/tower-1.png",
            "assets/towers/tower-2.png",
            "assets/towers/tower-3.png",
            "assets/towers/tower-4.png"
        ]
        self.tower_costs = [250, 750, 2000, 5000]
        self._waypoints = [
        {
            "x": -151.666666666667,
            "y": 368.666666666667
        }, 
        {
            "x": 195,
            "y": 362
        }, 
        {
            "x": 199,
            "y": 175.333333333333
        }, 
        {
            "x": 513.666666666667,
            "y": 175.333333333333
        }, 
        {
            "x": 516.333333333333,
            "y": 552.666666666667
        }, 
        {
            "x": 1029.66666666667,
            "y": 554
        }, 
        {
            "x": 1031,
            "y": 368.666666666667
        }, 
        {
            "x": 1296.33333333333,
            "y": 360.666666666667
        }
    ]
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
    def is_coordinate_valid_placement_point(self, x, y, coordinates,win, player):
        pos = pygame.mouse.get_pos()
        for block in coordinates:
            # get maximum coordinates
            max_x = block["x"] + block["width"]
            max_y = block["y"] + block["height"]
            # check if coordinates are in range
            if x >= block["x"] and x <= max_x and y >= block["y"] and y <= max_y:
                # coordinates are in range
                if block["is_placed"]:
                    # there is already a tower
                    # handle tower upgrading
                    for sprite in win.towers:
                        if sprite.rect.collidepoint(pos):
                            # check if player is trying to upgrade tower with same tower on block or trying to downgrade
                            if sprite._image_file != win.purchased_tower["img"] and sprite._price <= win.purchased_tower["price"]:
                                # player is trying to upgrade the tower
                                original_price = win.purchased_tower["price"] # keep track the old price for creating tower with original price
                                # update purchased towers price by substracting the price of old tower
                                win.purchased_tower["price"] -= sprite._price
                                # If player has enough money
                                if player.money >= win.purchased_tower["price"]: 
                                    # remove old tower
                                    win.all_sprites.remove(sprite)
                                    win.towers.remove(sprite)
                                    # return block and original price
                                    return block, original_price
                            else:
                                # player is trying to upgrade tower with same tower or trying to downgrade
                                return False, None
                    # coordinate is valid and there is no tower in the block
                else:
                    # If player has enough money
                    if player.money >= win.purchased_tower["price"]:
                        block["is_placed"] = True
                        return block, win.purchased_tower["price"]
                    # player has not enough money
                    return False, None
        # coordinates are out of range
        return False, None
    
    def show_tower_buy(self, screen, win):
        font = pygame.font.Font('freesansbold.ttf', 21)

        for i in range(len(self.tower_images)):
            image = pygame.image.load(self.tower_images[i]).convert_alpha()
            scaled = pygame.transform.scale(image, (100, 100))
            cost_text = font.render(f'{self.tower_costs[i]}', True, (255, 255, 255))
            scaled_x = win._SCREEN_WIDTH//2 - scaled.get_width()//2 + (i-1.5)*1.5*scaled.get_width()
            scaled_y = 15
            cost_text_x = win._SCREEN_WIDTH//2 - cost_text.get_width()//2 + (i-1.5)*1.5*scaled.get_width()
            cost_text_y = 125
            screen.blit(scaled, (scaled_x, scaled_y))
            screen.blit(cost_text, (cost_text_x, cost_text_y))
            # make sure to send coordinates maximum tower images length
            if len(self.buy_tower_coords) <= len(self.tower_images):
                # send image coordinates to buy tower coordinates
                dict = {}
                dict["tower"] = scaled
                dict["tower_price"] = self.tower_costs[i]
                self.buy_tower_coords.append(dict)


    def determine_tower(self, price, surface):
        tower = {
            "price": price,
            "surface": surface,
            "img": None,
            "range": None,
            "damage": None,
            "shooting_speed": None,
            "shooting_rate": None
        }
        # features of towers
        if price == 250:
            tower["img"] = self.tower_images[0]
            tower["range"] = 220
            tower["damage"] = 50
            tower["shooting_speed"] = 12
            tower["shooting_rate"] = 40
        elif price == 750:
            tower["img"] = self.tower_images[1]
            tower["range"] = 280
            tower["damage"] = 125
            tower["shooting_speed"] = 16
            tower["shooting_rate"] = 30
        elif price == 2000:
            tower["img"] = self.tower_images[2]
            tower["range"] = 350
            tower["damage"] = 250
            tower["shooting_speed"] = 20
            tower["shooting_rate"] = 25
        elif price == 5000:
            tower["img"] = self.tower_images[3]
            tower["range"] = 450
            tower["damage"] = 375
            tower["shooting_speed"] = 25
            tower["shooting_rate"] = 15

        return tower

        

   


