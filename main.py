import pygame

win = pygame.display.set_mode((600, 500))

back = ((0, 220, 255))

clock = pygame.time.Clock()

win.fill(back)
#阿拉马兹
is_game = True

class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed

    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 345:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 4, 50, 250)
racket2 = Player('racket.png', 520, 200, 4, 50, 250)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x = 5
speed_y = 5

while is_game:
    win.fill(back)
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 50:
        speed_y *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False

    racket1.update_l()

    racket2.update_r()
    
    racket1.reset()
    racket2.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(40)