import pygame
import os

from walking_girl.config import cfg_item

class SpriteWalk:

    def __init__(self):
        self.__image = pygame.image.load(os.path.join(*cfg_item("girl", "path"))).convert_alpha()

        self.__sprites = dict()

        self.__index_right = cfg_item("indexes_for_animation", "first_sprite_moving_right")
        self.__index_left = cfg_item("indexes_for_animation", "first_sprite_moving_left")

        #creating delay timer to match animation and movement of the sprite
        self.__timer = cfg_item("indexes_for_animation", "animation_delay")

        columns = cfg_item("girl", "columns")
        sprite_size = cfg_item("girl", "sprite_size")

        for i in range(cfg_item("girl", "total_sprites")):
            left = sprite_size[0] * (i % columns)
            top = sprite_size[1] * int(i / columns)
            self.__sprites[i] = pygame.Rect(left, top, sprite_size[0], sprite_size[1])

    def render(self, surface_dst, pos, direction):
        if direction == "right":
            self.__timer -= 1
            if self.__timer < 0:
                self.__timer = cfg_item("indexes_for_animation", "animation_delay")
                self.__index_right += 1
                if self.__index_right > cfg_item("indexes_for_animation", "last_sprite_moving_right"):
                    self.__index_right = cfg_item("indexes_for_animation", "first_sprite_moving_right")
            surface_dst.blit(self.__image, pos, self.__sprites[self.__index_right])

        if direction == "left":
            self.__timer -= 1
            if self.__timer < 0:
                self.__timer = cfg_item("indexes_for_animation", "animation_delay")
                self.__index_left += 1
                if self.__index_left > cfg_item("indexes_for_animation", "last_sprite_moving_left"):
                    self.__index_left = cfg_item("indexes_for_animation", "first_sprite_moving_left")
            surface_dst.blit(self.__image, pos, self.__sprites[self.__index_left])
