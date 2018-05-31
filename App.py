import Turtle
import math
from settings import *
import pygame
from itertools import tee

class App():
    def __init__(self):
        self.turtleImage = pygame.image.load(HERO_IMAGE)
        self.background = pygame.image.load(BACKGROUND)
        self.hero = Turtle.Turtle(x, y, width, height, (0, 255, 0), self.turtleImage)
        self.lines = []
        self.win = pygame.display.set_mode((500, 500))
        self.run = True

    def pairwise(self, iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def ask_for_command(self):
        global command, x, y, left, right, Up, Down, run, speed, pen, turtleImage
        command = input("Insert new command: ")
        if command == "exit":
            print("Good bye")
            self.run = False
        if command.startswith("fd "):
            destination = int(command[3:])
            # print(math.cos(self.hero.angle) * destination)
            # print(math.sin(self.hero.angle) * destination)
            # self.hero.y -= math.cos(self.hero.angle) * destination
            # self.hero.x -= math.sin(self.hero.angle) * destination
            # print(self.hero.y, self.hero.x)
            # print(self.lines)
        if command.startswith("bk "):
            destination = int(command[3:])
            pass
        if command == "down()" and x > 5 and x < 500 and y > 5 and y < 500:
            left = False
            right = False
            Up = False
            Down = True
            self.hero.y += speed
            print(self.lines)
        if command.startswith("lt "):
            angle = int(command[3:])
            self.hero.rotate(angle)
            print(self.hero.angle)
        if command.startswith("rt "):
            angle = int(command[3:])
            self.hero.rotate(-angle)
            print(self.hero.angle)
        if command == "pen()":
            self.lines.append((self.hero.x + 15, self.hero.y + 15))
            print(self.lines)
        else:
            self.lines.append(None)

    def drawWindow(self):
        self.win.blit(self.background, (0, 0))
        self.hero.draw_turtle(self.win)
        for start_coords, end_coords in self.pairwise(self.lines):
            if start_coords is not None and end_coords is not None:
                self.hero.draw_line(self.win, start_coords, end_coords)
        pygame.display.update()