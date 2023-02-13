import pygame
from pong import Game

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(Left = True, up = True)
    if keys[pygame.K_s]:
        game.move_paddle(Left = True, up = False)

    game_info = game.loop()
    print(game_info.left_score, game_info.right_score)
    game.draw(False, True)
    pygame.display.update()

pygame.quit()