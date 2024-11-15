import pygame

pygame.init()

LARGURA = 1200
ALTURA = 600
TÍTULO = "Penalty Shootout"
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (173, 216, 230)
AZUL_MARINHO = (60, 72, 92)
VERMELHO = (255, 0, 0)
LARANJA = (255, 100, 0)

#Acessa Arquivos

DIR_IMG = "imagens/"
DIR_WAV = "audios/"
DIR_FONT = "fonte/"

#Inicializa Jogo e Clock

window = pygame.display.set_mode(LARGURA, ALTURA)
pygame.display.set_caption(TÍTULO)

clock = pygame.time.Clock()

#Estados do Jogo

LOAD = 0 # Tela de Carregamento
INIT = 1 # Tela Inicial
CONFIG = 2 # Tela de Configurações
SELECT = 3 # Tela de Seleção de Times
PLAY = 4 # Tela Disputa