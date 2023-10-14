#Створи власний Шутер!
from random import *
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            if check is False:            
                check=True
                bulletX=spaceshipX+16

        
class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:       
            self.side = "left"
            

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space Shuter")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

rocket = Player("rocket.png", 5, 420, 4)

bullet = ("bullet.png", 3 )
check=False
bulletX=386
bulletY=490

spaceshipX=370
spaceshipY=480

enemy=[]
image_enemy = Enemy("ufo.png", 5, 15, 1)  


game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        rocket.update()
        image_enemy.update()        
        rocket.reset()
        image_enemy.reset()


    display.update()
    clock.tick(FPS)  