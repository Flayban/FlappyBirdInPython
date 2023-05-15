import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite): #Criação da classe 'Bird'
    def __init__(self): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'

        self.images = [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()]
        
        self.current_image = 0

        self.image = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() #Selecionando a imagem do Passaro
        self.rect = self.image.get_rect() #Coletando as coordenadas em que a imagem estara posicionada na exec.
        print(self.rect) #Print das coordenadas
        
        self.rect[0] = 270/2
        self.rect[1] = 512/2 

    def update(self): #Metodo update da classe
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        
