from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("pinghope")

background = transform.scale(image.load("background.png") , (700,500))

finish = False

speed_x = 3
speed_y = 3


clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Arial',30)
font2 = font.SysFont('Arial',80)

Chet1 = 0
Chet2 = 0


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

        if keys_pressed[K_s] and self.rect.x > -100:
            self.rect.y += self.speed
    
        if keys_pressed[K_w] and self.rect.x < 600:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.x > 5:
            self.rect.y += self.speed
    
        if keys_pressed[K_UP] and self.rect.x < 700:
            self.rect.y -= self.speed
       



May1 = player("New Piskel.png",50,10,10,30,150) 
May2 = player("New Piskel 2.png",600,10,10,30,150) 
ball = player("ballchime.png",300,0,10,30,30) 




game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish  !=  True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        May1.update1()
        May1.reset()
        May2.update2()
        May2.reset()
        ball.reset()
        if sprite.collide_rect(May1,ball) or sprite.collide_rect(May2,ball):
            speed_x *= -1
        if ball.rect.y > 500 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 5 :
            Chet2 = Chet2 + 1
            ball.rect.x = 300
            ball.rect.y = 100
            speed_x = speed_x + 1
            speed_y = speed_y + 1
        
        if ball.rect.x > 700 :
            Chet1 = Chet1 + 1
            ball.rect.x = 300
            ball.rect.y = 100
            speed_x = speed_x + 1
            speed_y = speed_x + 1
        

        vivod = font1.render(str(Chet1) + ":",True , (255,255,255))
        window.blit(vivod,(0,0))
        vivod2 = font1.render(str(Chet2),True , (255,255,255))
        window.blit(vivod2,(20,0))



    display.update()
    clock.tick(FPS)

