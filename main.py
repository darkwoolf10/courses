#!/usr/bin/python3
import pygame
from settings import *
from App import App
from Turtle import Turtle
from BestTurtle import BestTurtle

pygame.init()
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

if __name__ == "__main__":
    turtle = input("Select turtle 1 or 2:")
    if turtle == "1":
        app = App(Turtle(x, y, width, height, (0, 255, 0)))
    elif turtle == "2":
        app = App(BestTurtle(x, y, width, height, (0, 255, 0)))
    while app.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.run = False
        keys = pygame.key.get_pressed()
        app.drawWindow()
        app.ask_for_command()
        clock.tick(60)

pygame.quit()
