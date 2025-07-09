import pygame

win = pygame.display.set_mode((700, 500))

clock = pygame.time.Clock()

win.fill((0, 220, 255))
#阿拉马兹
is_game = True

while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False

    pygame.display.update()
    clock.tick(40)