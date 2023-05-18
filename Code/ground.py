import pygame
from constant import Constant
from pygame.locals import *

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/sprites/base.png')
        self.image = pygame.transform.scale(self.image, (Constant().GROUND_WIDTH, Constant().GROUND_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = Constant().SCREEN_HEIGTH - Constant().GROUND_HEIGTH

    def update(self):
        self.rect[0] -= Constant().OBJECT_SPEED

