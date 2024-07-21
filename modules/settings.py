import pygame
import os


screen = pygame.display.set_mode((600, 600))
class Object():
    def __init__(self, image_name, x, y, width, height, speed):
        self.IMAGE_NAME = image_name
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = speed
        self.image = None
        self.direction = 'r'
        self.load_image()
    def load_image(self, flip_x = False, flip_y = False):
        path_folder = os.path.abspath(__file__ + '/../../images')
        path_image = os.path.join(path_folder, self.IMAGE_NAME)
        self.image = pygame.image.load(path_image)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = pygame.transform.flip(self.image, flip_x, flip_y)
    def show_sprite(self):
        screen.blit(self.image, (self.X, self.Y))



