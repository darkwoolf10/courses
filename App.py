from BestTurtle import BestTurtle
from Turtle import Turtle
import math
from settings import *
import pygame
from itertools import tee

class App():
    def __init__(self, hero):
        self.background = pygame.image.load(BACKGROUND)
        self.lines = []
        self.hero = hero
        self.win = pygame.display.set_mode((500, 500))
        self.run = True

    def pairwise(self, iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def ask_for_command(self):
        global command, x, y, run, pen, turtleImage
        command = input("Insert new command: ")
        if command == "exit":
            print("\033[1;44mGood bye\033[1;m")
            self.run = False
        if command.startswith("fd "):
            destination = int(command[3:])
            self.hero.x += -destination * math.sin(math.radians(self.hero.angle))
            self.hero.y += -destination * math.cos(math.radians(self.hero.angle))
        if command.startswith("bk "):
            destination = int(command[3:])
            # self.hero.rotate(180)
            self.hero.x -= -destination * math.sin(math.radians(self.hero.angle))
            self.hero.y -= -destination * math.cos(math.radians(self.hero.angle))
        if command.startswith("lt "):
            angle = int(command[3:])
            self.hero.rotate(angle)
        if command.startswith("rt "):
            angle = int(command[3:])
            self.hero.rotate(-angle)
        if command == "help":
            print("\033[1;32mfd n\033[1;m  - Вперед на n пікселів.")
            print("\033[1;32mbk n\033[1;m  - Назад на n пікселів.")
            print("\033[1;32mlt n\033[1;m  - Поворот вліво на n пікселів.")
            print("\033[1;32mrt n\033[1;m  - Поворот вправо на n пікселів.")
            print("\033[1;32mpen()\033[1;m - Почати/припинити малювати лінію.")
            print("\033[1;32mexit\033[1;m  - Вихід з гри.\n")
        if command == "pen()":
            if self.hero.pen == False:
                self.hero.pen = True
            else:
                self.hero.pen = False
                self.lines.append(None)


    def drawWindow(self):
        self.win.blit(self.background, (0, 0))
        self.hero.draw_turtle(self.win)
        if self.hero.pen:
            self.lines.append((self.hero.x + 15, self.hero.y + 15))
        for start_coords, end_coords in self.pairwise(self.lines):
            if start_coords is not None and end_coords is not None:
                self.hero.draw_line(self.win, start_coords, end_coords)
        pygame.display.update()
