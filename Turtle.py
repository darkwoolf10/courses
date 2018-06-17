import pygame

class Turtle():
    def __init__(self, x, y, width, height, color, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.image.load(image)
        self.angle = 0
        self.pen = False

    def draw_turtle(self, win):
        win.blit(self.image, (self.x, self.y))

    def draw_line(self, win, start_coords, end_coords):
        pygame.draw.line(win, self.color, start_coords, end_coords, 3)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.angle += angle
        self.angle = self.angle % 360