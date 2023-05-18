import pygame
from constant import Constant
from pygame.locals import *

class Pipe(pygame.sprite.Sprite): #Criação da classe Pipe
    def __init__(self, inverted, xPos, ySize): #Metodo de inicialização da classe
        pygame.sprite.Sprite.__init__(self) #inicializando a classe 'Sprite'
        
        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha() #Selecionando a imagem do pipe
        self.image = pygame.transform.scale(self.image,(Constant().PIPE_WIDTH,Constant().PIPE_HEIGTH)) #Ajustando a imagem selecionada para a escala correta
        
        self.rect = self.image.get_rect() #Coletando as coordenadas em que a imagem estara posicionada na exec.
        self.rect[0] = xPos #posição horizontal inicial

        if inverted: #Caso inverted == True, realiza a inversão do pipe para que tenha um pipe normal e outro invertido
            self.image = pygame.transform.flip(self.image, False, True) #Responsavel por realziar a inversão vertical do pipe
            self.rect[1] = -(self.rect[3]- ySize) # Posição vertical do pipe invertido
        else:
            self.rect[1] = Constant().SCREEN_HEIGTH - ySize #Caso o pipe não seja invertido (inverted == False) essa sera a posição vertical do pipe

        self.mask = pygame.mask.from_surface(self.image) #Cria uma mascara para realizar a colisão

        
    def update(self): #Metodo update da classe    
        self.rect[0] -= Constant().OBJECT_SPEED #Cria a ilusão de movimento a uma deterninada velocidade