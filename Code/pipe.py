import pygame
from constant import Constant
from pygame.locals import *

class Pipe(pygame.sprite.Sprite): #Criação da classe Pipe
    def __init__(self, inverted, xPos, ySize):
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'
        
        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(Constant().PIPE_WIDTH,Constant().PIPE_HEIGTH))
        
        self.rect = self.image.get_rect()
        self.rect[0] = xPos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3]- ySize)
        else:
            self.rect[1] = Constant().SCREEN_HEIGTH - ySize

        self.mask = pygame.mask.from_surface(self.image)

        
    def update(self):    
        self.rect[0] -= Constant().OBJECT_SPEED