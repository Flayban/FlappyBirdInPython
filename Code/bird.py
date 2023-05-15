import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite): #Criação da classe 'Bird'
    def __init__(self): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'

        self.images = [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()] #Imagens responsaveis pela animação
        
        self.current_image = 0 #Define a imagem atual entre as opções em self.images

        self.image = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() #Selecionando a imagem do Passaro
        self.rect = self.image.get_rect() #Coletando as coordenadas em que a imagem estara posicionada na exec.
        print(self.rect) #Print das coordenadas
        
        #Posicionamento central do passaro
        self.rect[0] = 270/2 
        self.rect[1] = 512/2 
        #Obs.: Deve ser feito ajustes para que o posicionamento seja feito de forma referenciada e numerado

    def update(self): #Metodo update da classe
        self.current_image = (self.current_image + 1) % 3 #faz a adição e quando self.current_image = 3 então o resto da divisão é 0, logo o ciclo é repetido 
        self.image = self.images[self.current_image] #Seleciona a imagem correnspondente as opções 
        