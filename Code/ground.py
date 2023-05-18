import pygame
from constant import Constant
from pygame.locals import *

class Ground(pygame.sprite.Sprite): #Criação da classe Ground
    def __init__(self, xpos): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'

        self.image = pygame.image.load('assets/sprites/base.png').convert_alpha() #Selecionando a imagem do ground
        self.image = pygame.transform.scale(self.image, (Constant().GROUND_WIDTH, Constant().GROUND_HEIGTH)) #Ajustando a imagem selecionada para a escala correta
        self.mask = pygame.mask.from_surface(self.image) #Cria uma mascara para realizar a colisão
        self.rect = self.image.get_rect()  #Coletando as coordenadas em que a imagem estara posicionada na exec.
        self.rect[0] = xpos #posição horizontal inicial
        self.rect[1] = Constant().SCREEN_HEIGTH - Constant().GROUND_HEIGTH #posição vertical inicial

    def update(self): #Metodo update da classe
        self.rect[0] -= Constant().OBJECT_SPEED #Cria a ilusão de movimento a uma deterninada velocidade
 
