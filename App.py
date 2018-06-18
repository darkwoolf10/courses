from BestTurtle import BestTurtle
from Turtle import Turtle
import math
from settings import *
import pygame
from itertools import tee

class App():
    def __init__(self):
        self.background = pygame.image.load(BACKGROUND)
        self.hero = Turtle(x, y, width, height, (0, 255, 0))
        self.lines = []
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
            print("Good bye")
            self.run = False
        if command.startswith("fd "):
            destination = int(command[3:])
            self.hero.x += -destination * math.sin(math.radians(self.hero.angle))
            self.hero.y += -destination * math.cos(math.radians(self.hero.angle))
        if command.startswith("bk "):
            destination = int(command[3:])
            self.hero.rotate(180)
            self.hero.x += -destination * math.sin(math.radians(self.hero.angle))
            self.hero.y += -destination * math.cos(math.radians(self.hero.angle))
        if command.startswith("lt "):
            angle = int(command[3:])
            self.hero.rotate(angle)
        if command.startswith("rt "):
            angle = int(command[3:])
            self.hero.rotate(-angle)
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