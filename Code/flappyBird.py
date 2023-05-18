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
birdGroup.add(fBird) #Adção do passaro criado aou agrupamento

groundGrup = pygame.sprite.Group()
for i in range(2):
    fGround = Ground((const.GROUND_WIDTH)*i )
    groundGrup.add(fGround)

clock = pygame.time.Clock() #chama a função clock, responsavel por determinar o FPS do sistema

def isOffScreen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

while True: #Laço de repetição infinito para manter janela aberta
    clock.tick(30) #Determina a quantidade de FPS do jogo
    for event in pygame.event.get(): #Iteração de evento com Pygame 
        if event.type == QUIT: #evento condicional: caso event.type == quit finalisa o programa
            pygame.quit() #Finaliza o Pygame

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                fBird.bump()

    screen.blit(BACKGROUND,(0,0)) #Excutando imagem de background no display

    if isOffScreen(groundGrup.sprites()[0]):
        groundGrup.remove(groundGrup.sprites()[0])

        newGround = Ground(const.GROUND_WIDTH - 20)
        groundGrup.add(newGround)

    birdGroup.update() #Atualização do birdGrup
    groundGrup.update()

    birdGroup.draw(screen) #Informar o local que deseja que o passaro aparessa (neste caso na tela do jogo)
    groundGrup.draw(screen)

    pygame.display.update() #Atualiza o display