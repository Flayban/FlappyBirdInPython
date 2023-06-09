#Classe responsavel por passar dados constantes para as demais classes
class Constant():
    # dimensões vertical e horizontal da tela em pixels
    SCREEN_WIDTH = 288 
    SCREEN_HEIGTH = 600

    SPEED = 10 #Velocidade do Passaro
    GRAVITY = 1 #Gravidade do Passaro

    OBJECT_SPEED = 10 # Velocidade dos objetos

    # dimensões vertical e horizontal do 'ground' em pixels
    GROUND_WIDTH = SCREEN_WIDTH * 2
    GROUND_HEIGTH = 100

    # dimensões vertical e horizontal do 'pipe' em pixels
    PIPE_WIDTH = 80
    PIPE_HEIGTH = 500

    PIPE_GAP = 200 #distancia entre os 'pipes' em pixels