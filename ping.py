
from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("pinghope")

background = transform.scale(image.load("background.png") , (700,500))

finish = False


clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish  !=  True:
        window.blit(background,(0,0))
    display.update()
    clock.tick(FPS)
