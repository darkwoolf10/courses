from Turtle import Turtle
import pygame

class BestTurtle(Turtle):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = pygame.image.load("legasy.png")
        self.color = (255, 255, 0)

    def draw_line(self, win, start_coords, end_coords):
        pygame.draw.line(win, self.color, start_coords, end_coords, 1)