
from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("Синяя бибра Люся 228")

clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
clock.tick(FPS)
