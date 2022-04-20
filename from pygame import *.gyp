from pygame import *

back = (255, 182, 193) #фон
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player('pngegg.png', 20, 100, 30, 300, 15)
racket2 = Player('pngegg.png', 550, 100, 30, 300, 15)

ball = GameSprite('ball.png', 280, 200, 40, 40, 4) #мяч
dx = 3
dy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += dx #движение мяча
        ball.rect.y += dy #движение мяча
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball): #столкновение с ракетками
            dx *= -1     #изменение направления по х
        if ball.rect.y < 0 or ball.rect.y > win_height-40: #столкновение со стенками
            dy *= -1     #изменение направления по у

        racket1.reset()
        racket2.reset()

        ball.reset() #мяч

    display.update()
    clock.tick(FPS)
