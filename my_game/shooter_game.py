#Создай собственный Шутер!
from pygame import *
window = display.set_mode((700,500))
background = transform.scale(image.load("galaxy.jpg"),(700,500))
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()