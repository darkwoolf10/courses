import pygame

window = pygame.display.set_mode((400, 400))

FPS = 60
clock = pygame.time.Clock()

x, y = 200, 200

def ask_for_command():
    command = input("Insert new command: ")
    if command in ("left()", "right()"):
        global x
        if command == "left()":
            x -= 5
        if command == "right()":
            x += 5

game_ended = False
while not game_ended:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True

    ask_for_command()

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), (x, y, 50, 50))

    pygame.display.update()
    clock.tick(FPS)