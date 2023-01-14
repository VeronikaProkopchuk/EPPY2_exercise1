import pygame

from walking_girl.config import cfg_item
from walking_girl.sprite_walk import SpriteWalk
from walking_girl.sprite_dance import SpriteDance

class Action:

    def __init__(self, x_init, y_init):
        self.__pos = pygame.math.Vector2(x_init, y_init)
        self.__sprite_walk = SpriteWalk()
        self.__sprite_dance = SpriteDance()

        self.__action = "dance"
        self.__dance_timer = cfg_item("indexes_for_animation", "dance_timer")


    def update(self, delta_time):
        if self.__action == "dance":
            self.__dance_timer -= 1
            if self.__dance_timer == 0:
                #stopping the music
                pygame.mixer.music.stop()
                #ending the dance
                self.__action = "right"

        if self.__action == "left":
            self.__pos.x -= cfg_item("movement", "speed") * delta_time
            if self.__pos.x <= -cfg_item("girl", "sprite_size")[0]:
                self.__action = "right"

        if self.__action == "right":
            self.__pos.x += cfg_item("movement", "speed") * delta_time
            if self.__pos.x >= (cfg_item("screen_size")[0]-120):
                self.__action = "left"

    def render(self, surface_dst):
        if self.__action == "dance":
            pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
            self.__sprite_dance.render(surface_dst, pos, self.__action)

        pos = (self.__pos.x + (cfg_item("girl", "sprite_size")[0]), self.__pos.y)
        self.__sprite_walk.render(surface_dst, pos, self.__action)