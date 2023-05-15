import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite): #Criação da classe 'Bird'
    def __init__(self): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'

        self.image = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() #Selecionando a imagem do Passaro
        self.rect = self.image.get_rect() #Coletando as coordenadas em que a imagem estara posicionada na exec.
        print(self.rect) #Print das coordenadas

    def update(self): #Metodo update da classe
        pass
