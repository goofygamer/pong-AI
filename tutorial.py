import pygame
from pong import Game

#Sizing for the window
width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    game.loop()
    game.draw()
    pygame.display.update()

pygame.quit()