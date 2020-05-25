import pygame
import random
from math import sin, cos, floor, pi

screenWidth = 800
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Asteroid Field")

img = pygame.image.load("universe.jpeg")
#img = pygame.transform.scale(img, (screenWidth, screenHeight))

speed = 3

class Asteroid :
    def __init__(self) :
        self.x = random.randint(-screenWidth // 2, screenWidth // 2)
        self.y = random.randint(-screenHeight // 2, screenHeight // 2)
        self.z = random.randint(1, screenWidth)

WHITE = (255,255,255)

def update(a) :
    if a.z > speed :
        a.z -= speed
    else : 
        a.z = screenWidth
        a.x = random.randint(-screenWidth // 2, screenWidth // 2)
        a.y = random.randint(-screenHeight // 2, screenHeight // 2)

    a.x -= speed * (mouseX - screenWidth // 2) / screenWidth
    a.y -= speed * (mouseY - screenHeight // 2) / screenHeight

def draw(a) :
    x = a.x 
    y = a.y
    z = a.z

    x = (x / z) * screenWidth + screenWidth // 2
    y = (y / z) * screenHeight + screenHeight // 2

    r = screenWidth / z
    pygame.draw.circle(win, WHITE, (floor(x), floor(y)), floor(r))

asteroid = []
for i in range(200) :
    asteroid.append(Asteroid())

run = True
while run :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    mouseX, mouseY = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] :
        pygame.time.delay(10)
        speed += 0.25
    elif keys[pygame.K_DOWN] :
        pygame.time.delay(10)
        speed -= 0.25

    win.fill(0)
    win.blit(img, (0, 0))
    
    for a in asteroid :
        update(a)
        draw(a)

    pygame.display.update()
pygame.quit()