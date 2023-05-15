import pygame
from pygame.locals import *

# dimensões vertical e horizontal da tela em pixels
SCREEN_WIDTH = 288 
SCREEN_HEIGTH = 512


pygame.init() #Inicia o Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH)) #dimensiona o display a partir das dimensões já definidas 

BACKGROUND = pygame.image.load('assets/sprites/background-day.png') #selecionando imagem de background
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGTH)) #redimensionando imagem de backgroud para mesma escala do display

while True: #Laço de repetição infinito para manter janela aberta
    for event in pygame.event.get(): #Iteração de evento com Pygame 
        if event.type == QUIT: #evento condicional: caso event.type == quit finalisa o programa
            pygame.quit() #Finaliza o Pygame

    screen.blit(BACKGROUND,(0,0)) #Excutando imagem de background no display
    pygame.display.update() #Atualiza o display