#!/usr/bin/python3
import pygame
from settings import *
from App import App

pygame.init()
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

app = App()
if __name__ == "__main__":
    while app.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.run = False
        keys = pygame.key.get_pressed()
        app.drawWindow()
        app.ask_for_command()
        clock.tick(60)

pygame.quit()