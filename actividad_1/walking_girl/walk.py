import pygame

from walking_girl.config import cfg_item
from walking_girl.bitmapfont import BitmapFont

class Walk:

    def __init__(self, y_init):
        self.__pos = pygame.math.Vector2(cfg_item("screen_size")[0]-120, y_init)
        self.__bitmapfont = BitmapFont()

        self.__direction = "left"


    def update(self, delta_time):
        if self.__direction == "left":
            self.__pos.x -= cfg_item("walk", "speed") * delta_time
            if self.__pos.x <= -cfg_item("girl", "sprite_size")[0]:
                self.__direction = "right"

        if self.__direction == "right":
            self.__pos.x += cfg_item("walk", "speed") * delta_time
            if self.__pos.x >= (cfg_item("screen_size")[0]-120):
                self.__direction = "left"

    def render(self, surface_dst):
        pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
        self.__bitmapfont.render(surface_dst, pos, self.__direction)