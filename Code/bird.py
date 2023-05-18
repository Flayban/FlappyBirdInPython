import pygame
import constant
from pygame.locals import *

class Bird(pygame.sprite.Sprite): #Criação da classe 'Bird'
    def __init__(self): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'

        self.images = [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()] #Imagens responsaveis pela animação
        
        self.speed = constant.Constant().SPEED

        self.current_image = 0 #Define a imagem atual entre as opções em self.images

        self.image = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha() #Selecionando a imagem do Passaro
        self.rect = self.image.get_rect() #Coletando as coordenadas em que a imagem estara posicionada na exec.
        print(self.rect) #Print das coordenadas
        
        #Posicionamento central do passaro
        self.rect[0] = (constant.Constant().SCREEN_WIDTH-18)/2 
        self.rect[1] = constant.Constant().SCREEN_HEIGTH/2 

    def update(self): #Metodo update da classe
        self.current_image = (self.current_image + 1) % 3 #faz a adição e quando self.current_image = 3 então o resto da divisão é 0, logo o ciclo é repetido 
        self.image = self.images[self.current_image] #Seleciona a imagem correnspondente as opções 

        self.speed += constant.Constant().GRAVITY
        #Atualizar a Vertical
        self.rect[1] += self.speed 
        
    def bump(self):
        self.speed = -constant.Constant().SPEED
       
