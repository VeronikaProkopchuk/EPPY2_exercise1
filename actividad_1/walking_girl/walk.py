import pygame

from walking_girl.config import cfg_item
from walking_girl.bitmapfont import BitmapFont
from walking_girl.bitmapfont_dance import BitmapFontDance

class Walk:

    def __init__(self, y_init):
        self.__pos = pygame.math.Vector2(cfg_item("screen_size")[0]-420, y_init)
        self.__bitmapfont = BitmapFont()
        self.__bitmapfont_dance = BitmapFontDance()

        self.__direction = "dance"
        self.__dance_timer = cfg_item("indexes_for_animation", "dance_timer")


    def update(self, delta_time):
        if self.__direction == "dance":
            self.__dance_timer -= 1
            if self.__dance_timer == 0:
                pygame.mixer.music.stop()
                self.__direction = "right"

        if self.__direction == "left":
            self.__pos.x -= cfg_item("walk", "speed") * delta_time
            if self.__pos.x <= -cfg_item("girl", "sprite_size")[0]:
                self.__direction = "right"

        if self.__direction == "right":
            self.__pos.x += cfg_item("walk", "speed") * delta_time
            if self.__pos.x >= (cfg_item("screen_size")[0]-120):
                self.__direction = "left"

    def render(self, surface_dst):
        if self.__direction == "dance":
            pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
            self.__bitmapfont_dance.render(surface_dst, pos, self.__direction)

        pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
        self.__bitmapfont.render(surface_dst, pos, self.__direction)