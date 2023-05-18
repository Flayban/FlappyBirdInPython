import pygame, constant
from bird import Bird
from ground import Ground
from pygame.locals import *

pygame.init() #Inicia o Pygame
const = constant.Constant()
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGTH)) #dimensiona o display a partir das dimensões já definidas 

BACKGROUND = pygame.image.load('assets/sprites/background-day.png') #selecionando imagem de background
BACKGROUND = pygame.transform.scale(BACKGROUND,(const.SCREEN_WIDTH,const.SCREEN_HEIGTH)) #redimensionando imagem de backgroud para mesma escala do display

birdGroup = pygame.sprite.Group() #Criação do agrupamento da Classe 'Bird'
fBird = Bird() #Chamada da Classe 'Bird'
birdGroup.add(fBird) #Adção do passaro criado ao agrupamento

groundGrup = pygame.sprite.Group() #Criação do agrupamento da Classe 'Ground'
for i in range(2): #Realiza a duplicação da chanada da Classe 'Ground'
    fGround = Ground((const.GROUND_WIDTH)*i ) #Chamada da Classe 'Ground'
    groundGrup.add(fGround) #Adção do ground criado ao agrupamento

clock = pygame.time.Clock() #chama a função clock, responsavel por determinar o FPS do sistema

def isOffScreen(sprite): #Metodo para verificar se algum sprite saiu completamente da tela
    return sprite.rect[0] < -(sprite.rect[2])

while True: #Laço de repetição infinito para manter janela aberta
    clock.tick(30) #Determina a quantidade de FPS do jogo

    for event in pygame.event.get(): #Iteração de evento com Pygame 
        if event.type == QUIT: #evento condicional: caso event.type == QUIT finalisa o programa
            pygame.quit() #Finaliza o Pygame

        if event.type == KEYDOWN: #evento condicional: caso event.type == KEYDOWN entra na proxima condição 
            if event.key == K_SPACE: #evento condicional: caso event.key == K_SPACE, então realiza a ação de "pulo" do passaro
                fBird.bump() #Chama a ação de pulo do passaro  

    screen.blit(BACKGROUND,(0,0)) #Excutando imagem de background no display

    if isOffScreen(groundGrup.sprites()[0]): #Verifica se o ground esta fora da tela, caso esteja realiza a remoção do grund atual e cria um novo
        groundGrup.remove(groundGrup.sprites()[0]) #Remoção do ground atual

        newGround = Ground(const.GROUND_WIDTH - 20) #Criação de um novo ground
        groundGrup.add(newGround) #Adção do ground criado ao agrupamento

    birdGroup.update() #Atualização do birdGrup
    groundGrup.update() #Atualização do groundGrup

    birdGroup.draw(screen) #Informar o local que deseja que o passaro aparessa (neste caso na tela do jogo)
    groundGrup.draw(screen) #Informar o local que deseja que o ground aparessa (neste caso na tela do jogo)

    pygame.display.update() #Atualiza o display