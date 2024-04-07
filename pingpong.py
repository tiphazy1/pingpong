from pygame import *
from random import *
window = display.set_mode((700, 500))
background = transform.scale(image.load("123.jpg"), (700, 500))
display.set_caption("Pingpong")
FPS = 144
game = True
finish = False
clock = time.Clock()

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
            self.rect.x -= self.speed
        if key_pressed[K_s] and self.rect.y < 495:
            self.rect.x += self.speed
pl1 = Player("133.jpg", 15, 340, 40, 80, 10)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    pl1.reset()
    display.update()
    clock.tick(FPS) 









    
