import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Turtle")

x = 200
y = 200
width = 50
height = 50
speed = 5

turtle = pygame.image.load('turtle.png')
background = pygame.image.load('bg.jpg')
# walkRight = pygame.image.load('spites/right.png')
# walkLeft = pygame.image.load('spites/left.png')
# walkUp = pygame.image.load('spites/up.png')
# walkDown = pygame.image.load('spites/down.png')
# background = pygame.image.load('sprites/bg.jpg')

left = False
right = False
Up = False
Down = False

def drawWindow():
    win.blit(background, (0, 0))
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (x, y, width, height))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x-=speed
        left = True
        right = False
        Up = False
        Down = False    
    if keys[pygame.K_RIGHT] and x < 500 - width -5:
        x+=speed
        left = False
        right = True
        Up = False
        Down = False
    if keys[pygame.K_UP] and y > 5:
        y-=speed
        left = False
        right = False
        Up = True
        Down = False
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y+=speed
        left = False
        right = False
        Up = False
        Down = True   

    # drawWindow()
    win.blit(background, (0, 0))
    win.blit(turtle, (x, y))
    pygame.display.update()

pygame.quit()         