from .map import game_matrix, list_block, list_bullet
from .bullet import Bullet
import pygame

x = 0
y = 0
for i in game_matrix:
    for j in i:
        if j == 1:
            block = pygame.Rect(x, y, 30, 30)
            list_block.append(block)
        elif j == 2:
            finish = pygame.Rect(x, y, 30, 30)
        elif j == 'u':
            bullet = Bullet('bullet.png', x + 13, y + 9, 4, 20, 4, 'up')
            list_bullet.append(bullet)
        elif j == 'd':
            bullet = Bullet('bullet.png', x + 13, y - 4, 4, 20, 4, 'down')
            list_bullet.append(bullet)
        x += 30
    y += 30
    x = 0
    