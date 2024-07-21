import pygame
import os
from modules.settings import screen
from modules.hero import hero
from modules.create_map import *

pygame.init()
pygame.display.set_caption("Game")
font = pygame.font.Font(None, 100)
finish_text = font.render('Finish', True, (120, 210, 100))
clock = pygame.time.Clock()
scene = 'game'
start = True
while start:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    if scene == 'game':
        screen.fill((166, 191, 225))
        hero.show_sprite()
        hero.move()
        pygame.draw.rect(screen, (225, 0, 0), finish)
        for i in list_block:
            pygame.draw.rect(screen, (0, 0, 0), i)
        for i in list_bullet:
            i.show_sprite()
            i.move_bullet(hero)
    elif scene == 'finish':
        screen.fill((227, 229, 183))
        screen.blit(finish_text, (200, 250))
    pygame.display.flip()