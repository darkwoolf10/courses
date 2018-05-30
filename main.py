#!/usr/bin/python3
import pygame
from itertools import tee
import Turtle
import math

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Turtle")
clock = pygame.time.Clock()

x = 200
y = 200
width = 5
height = 5
speed = 25

left = False
right = False
Up = False
Down = False

turtleImage = pygame.image.load('legasy.png')
image = turtleImage
background = pygame.image.load('bg.jpg')

lines = []

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def drawWindow():
    win.blit(background, (0, 0))
    hero.draw_turtle(win)
    for start_coords, end_coords in pairwise(lines):
        if start_coords is not None and end_coords is not None:
            hero.draw_line(win, start_coords, end_coords)
    pygame.display.update()

def ask_for_command():
    global command, x, y, left, right, Up, Down, run, speed, pen, turtleImage
    command = input("Insert new command: ")
    if command == "exit()":
        print("Good bye")
        run = False
    if command.startswith("fd "):
        destination = int(command[3:])
        print(math.cos(hero.angle) * destination)
        print(math.sin(hero.angle) * destination)
        hero.y -= math.cos(hero.angle) * destination
        hero.x -= math.sin(hero.angle) * destination
        print(hero.y, hero.x)
        print(lines)
    if command.startswith("bk "):
        pass

    if command == "down()" and x > 5 and x < 500 and y > 5 and y < 500:
        left = False
        right = False
        Up = False
        Down = True
        hero.y += speed
        print(lines)
    if command.startswith("lt "):
        angle = int(command[3:])
        hero.rotate(angle)
        print(hero.angle)
    if command.startswith("rt "):
        angle = int(command[3:])
        hero.rotate(-angle)
        print(hero.angle)
    if command == "pen()":
        lines.append((hero.x + 15, hero.y + 15))
        print(lines)
    else:
        lines.append(None)

run = True
hero = Turtle.Turtle(x, y, width, height, (0, 255, 0), turtleImage)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    drawWindow()
    ask_for_command()
    clock.tick(60)

pygame.quit()