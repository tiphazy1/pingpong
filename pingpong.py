from pygame import *
from random import *
window = display.set_mode((700, 500))
background = transform.scale(image.load("123.jpg"), (700, 500))
display.set_caption("Pingpong")
FPS = 144
game = True
finish = False
clock = time.Clock()
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, palyer_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = palyer_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed() 
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed() 
        if key_pressed[K_e] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_d] and self.rect.y < 495:
            self.rect.y += self.speed
# class Enemy(GameSprite):
    # def __init__(self, player_image, player_x, palyer_y, size_x, size_y, speed_x, speed_y):
    #     self.image = transform.scale(image.load(player_image), (size_x, size_y))
    #     self.rect = self.image.get_rect()
    #     self.rect.x = player_x
    #     self.rect.y = palyer_y
    #     self.speed_y = speed_y
    #     self.speed_x = speed_x
    # def reset(self):
    #     window.blit(self.image, (self.rect.x, self.rect.y))
pl1 = Player("133.jpg", 15, 340, 40, 80, 3)
pl2 = Player("133.jpg", 650, 340, 40, 80, 3)
ball = GameSprite("ball.png", 65, 240, 30, 30,0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))

        pl1.update()
        pl2.update2()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(pl1, ball) or sprite.collide_rect(pl2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            pass
        pl1.reset()
        pl2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS) 









    
