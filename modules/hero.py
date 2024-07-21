import pygame
from .settings import Object
from .map import list_block
from .create_map import finish

class Hero(Object):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__(image_name, x, y, width, height, speed)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'l'
            self.load_image()
            self.X -= self.SPEED
            self.collision()
        elif keys[pygame.K_RIGHT]:
            self.direction = 'r'
            self.load_image(True, False)
            self.X += self.SPEED
            self.collision()
        elif keys[pygame.K_UP]:
            self.Y -= self.SPEED
            self.collision()
            if self.Y < 0:
                self.Y = 0
        elif keys[pygame.K_DOWN]:
            self.Y += self.SPEED
            self.collision()
    def collision(self):
        global scene
        hero_rect = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        for i in list_block:
            if hero_rect.colliderect(i):
                self.X = 70
                self.Y = 0
                break
        if hero_rect.colliderect(finish):
            scene = 'finish'

hero = Hero('hero2.png', 70, 0, 12, 20, 3)