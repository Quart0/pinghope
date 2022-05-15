
from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("pinghope")

background = transform.scale(image.load("background.png") , (700,500))

finish = False


clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect  =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.x > 5:
            self.rect.y += self.speed
    
        if keys_pressed[K_UP] and self.rect.x < 600:
            self.rect.y -= self.speed


May1 = player("New Piskel.png",10,10,10,200,200) 
  



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish  !=  True:
        window.blit(background,(0,0))
        May1.update1()
        May1.reset()
    display.update()
    clock.tick(FPS)
