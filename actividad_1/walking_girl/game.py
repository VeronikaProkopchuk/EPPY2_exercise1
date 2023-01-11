import pygame
import os

from walking_girl.config import cfg_item
from walking_girl.movement import Movement

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(cfg_item("screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("title"))

        self.__running = False
        self.__fps_clock = pygame.time.Clock()
        self.__walk = [Movement(cfg_item("movement", "spawn_position")[0], cfg_item("movement", "spawn_position")[1])]

    def run(self):
        self.__running = True
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(*cfg_item("music", "music_path")))
        pygame.mixer.music.play(loops=0, start=cfg_item("music", "music_start"), fade_ms=2)

        while self.__running:
            delta_time = self.__fps_clock.tick(cfg_item("fps"))
            self.__process_events()
            self.__update(delta_time)
            self.__render()

        self.__quit()

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

    def __update(self, delta_time):
        for step in self.__walk:
            step.update(delta_time)

    def __render(self):
        self.__screen.fill(cfg_item("background_color"))

        for step in self.__walk:
            step.render(self.__screen)

        pygame.display.update()

    def __quit(self):
        pygame.quit()