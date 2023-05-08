import pygame
from pygame.locals import *

# dimensões vertical e horizontal da tela em pixels
SCREEN_WIDTH = 400 
SCREEN_HEIGTH = 600

pygame.init() #Inicia o Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH)) #dimensiona o display a partir das dimensões já definidas 

while True: #Laço de repetição infinito para manter janela aberta
    for event in pygame.event.get(): #Iteração de evento com Pygame 
        if event.type == QUIT: #evento condicional: caso event.type == quit finalisa o programa
            pygame.quit() #Finaliza o Pygame
    pygame.display.update() #Atualiza o display