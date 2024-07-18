import pygame
import os

pygame.init()
class Hero:
    def __init__(self, image_name, x, y, width, height, speed):
        self.IMAGE_NAME = image_name
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = speed
        self.image = None
        self.load_image()
    def load_image(self, flip_y = False):
        path_folder = os.path.abspath(__file__ + '/..')
        path_image = os.path.join(path_folder, self.IMAGE_NAME)
        self.image = pygame.image.load(path_image)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = pygame.transform.flip(self.image, False, flip_y)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.X -= self.SPEED
            self.collision()
        elif keys[pygame.K_RIGHT]:
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
    def show_sprite(self):
        screen.blit(self.image, (self.X, self.Y))
hero = Hero('hero2.png', 70, 0, 12, 20, 3)
class Bullet(Hero):
    def __init__(self, image_name, x, y, width, height, speed, direction):
        super().__init__(image_name, x, y, width, height, speed)
        self.START_X = x
        self.START_Y = y
        self.DIRECTION = direction
    def move_bullet(self):
        self.collision_bullet()
        if self.DIRECTION == 'up':
            self.Y -= self.SPEED
            self.load_image()
        elif self.DIRECTION == 'down':
            self.Y += self.SPEED
            self.load_image(True)
    def collision_bullet(self):
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
game_matrix = [
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 'u', 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 'd', 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
list_block = []
list_bullet = []
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Game")

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
            i.move_bullet()
    elif scene == 'finish':
        screen.fill((227, 229, 183))
        screen.blit(finish_text, (200, 250))
    pygame.display.flip()