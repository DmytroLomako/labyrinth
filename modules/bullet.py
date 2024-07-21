import pygame
from .settings import Object
from .create_map import list_block

class Bullet(Object):
    def __init__(self, image_name, x, y, width, height, speed, direction):
        super().__init__(image_name, x, y, width, height, speed)
        self.START_X = x
        self.START_Y = y
        self.DIRECTION = direction
    def move_bullet(self, hero):
        self.collision_bullet(hero)
        if self.DIRECTION == 'up':
            self.Y -= self.SPEED
            self.load_image()
        elif self.DIRECTION == 'down':
            self.Y += self.SPEED
            self.load_image(False, True)
    def collision_bullet(self, hero):
        bullet_rect = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        
        hero_rect = pygame.Rect(hero.X, hero.Y, hero.WIDTH, hero.HEIGHT)
        for i in list_block:
            if bullet_rect.colliderect(i):
                self.X = self.START_X
                self.Y = self.START_Y
                break
        if bullet_rect.colliderect(hero_rect):
            hero.X = 70
            hero.Y = 0

