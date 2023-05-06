import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self._image = pygame.image.load(image_file)
        self._rect = self._image.get_rect()
        self._rect.left, self._rect.top = location
        self._waypoints = [
            {"x": -93.3333333333333, "y": 285.333333333333},
            {"x": 664, "y": 289.333333333333},
            {"x": 669.333333333333, "y": 528},
            {"x": 1360, "y": 534.666666666667},
        ]
