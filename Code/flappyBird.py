import pygame, random
from constant import Constant
from bird import Bird
from ground import Ground
from pipe import Pipe
from pygame.locals import *

def isOffScreen(sprite): #Metodo para verificar se algum sprite saiu completamente da tela
    return sprite.rect[0] < -(sprite.rect[2])

def getRandomPipes(xPos): #Metodo para criar de forma randomica os pipes com alturas diferentes
    size = random.randint(100, 300) #Seleciona randomicamente a altura
    pipe = Pipe(False, xPos, size) #Cria o pipe
    pipeInverted = Pipe(True, xPos, Constant().SCREEN_HEIGTH - size - Constant().PIPE_GAP) #Cria o pipe invertido

    return (pipe, pipeInverted) #Retorna o par de pipes

pygame.init() #Inicia o Pygame
const = Constant()
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGTH)) #dimensiona o display a partir das dimensões já definidas 

BACKGROUND = pygame.image.load('assets/sprites/background-day.png') #selecionando imagem de background
BACKGROUND = pygame.transform.scale(BACKGROUND,(const.SCREEN_WIDTH,const.SCREEN_HEIGTH)) #redimensionando imagem de backgroud para mesma escala do display

birdGroup = pygame.sprite.Group() #Criação do agrupamento da Classe 'Bird'
fBird = Bird() #Chamada da Classe 'Bird'
birdGroup.add(fBird) #Adição do passaro criado ao agrupamento

groundGrup = pygame.sprite.Group() #Criação do agrupamento da Classe 'Ground'
for i in range(2): #Realiza a duplicação da chanada da Classe 'Ground'
    fGround = Ground((const.GROUND_WIDTH)* i ) #Chamada da Classe 'Ground'
    groundGrup.add(fGround) #Adição do ground criado ao agrupamento

pipeGroup = pygame.sprite.Group() #Criação do agrupamento da Classe 'Pipe'
for i in range(2):#Realiza a duplicação da chanada da Classe 'Pipe'
    pipes = getRandomPipes(const.SCREEN_WIDTH* i + 800) #Gera os pipes de forma randomica 
    pipeGroup.add(pipes[0]) #Aidção do pipe criado ao agrupamento
    pipeGroup.add(pipes[1]) #Aidção do pipe invertido criado ao agrupamento

clock = pygame.time.Clock() #chama a função clock, responsavel por determinar o FPS do sistema

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
        groundGrup.add(newGround) #Adição do ground criado ao agrupamento

    if isOffScreen(pipeGroup.sprites()[0]): #Verifica se os pipes estão fora da tela, caso estejam realiza a remoção dos pipes atuais e cria novos
        pipeGroup.remove(pipeGroup.sprites()[0]) #Remoção do pipe atual
        pipeGroup.remove(pipeGroup.sprites()[0]) #Remoção do pipe invertido atual

        newPipe = getRandomPipes(const.SCREEN_WIDTH * 2) #Gera os pipes de forma randomica 
        pipeGroup.add(newPipe[0]) #Adição do pipe criado ao agrupamento
        pipeGroup.add(newPipe[1]) #Adição do pipe invertido criado ao agrupamento

    birdGroup.update() #Atualização do birdGrup
    groundGrup.update() #Atualização do groundGrup
    pipeGroup.update() #Atualização do pipeGrup

    birdGroup.draw(screen) #Informar o local que deseja que o bird aparece (neste caso na tela do jogo)
    groundGrup.draw(screen) #Informar o local que deseja que o ground aparece (neste caso na tela do jogo)
    pipeGroup.draw(screen) #Informar o local que deseja que o pipe aparece(neste caso na tela do jogo)

    pygame.display.update() #Atualiza o display

    if (pygame.sprite.groupcollide(birdGroup, groundGrup, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False, pygame.sprite.collide_mask)): #Verifica se o Bird colodio com o Ground ou Bird colodio com o Pipe , se sim finaliza a aplicação
        break #Finaliza a aplição

           