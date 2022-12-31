import pygame
import os

from walking_girl.config import cfg_item

class BitmapFont:

    def __init__(self):
        self.__image = pygame.image.load(os.path.join(*cfg_item("girl", "path"))).convert_alpha()

        self.__font = dict()

        self.__index_right = 1
        self.__index_left = 11
        self.__index_right_max = 9
        self.__index_left_max = 19
        self.__timer = 10

        columns = cfg_item("girl", "columns")
        letter_size = cfg_item("girl", "sprite_size")

        for i in range(cfg_item("girl", "total_sprites")):
            left = letter_size[0] * (i % columns)
            top = letter_size[1] * int(i / columns)
            self.__font[i] = pygame.Rect(left, top, letter_size[0], letter_size[1])

    def render(self, surface_dst, pos, direction):
        if direction == "right":
            self.__timer -= 1
            if self.__timer < 0:
                self.__timer = 10
                self.__index_right += 1
                if self.__index_right > self.__index_right_max:
                    self.__index_right = 1
            surface_dst.blit(self.__image, pos, self.__font[self.__index_right])

        if direction == "left":
            self.__timer -= 1
            if self.__timer < 0:
                self.__timer = 10
                self.__index_left += 1
                if self.__index_left > self.__index_left_max:
                    self.__index_left = 11
            surface_dst.blit(self.__image, pos, self.__font[self.__index_left])

        
