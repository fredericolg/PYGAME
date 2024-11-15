import pygame
import os
from config import DIR_IMG, DIR_WAV, DIR_FNT, LARGURA, ALTURA

LOGO = 'logo'
FUNDO = 'fundo'
FUNDO_PIX = 'fundo_pixe'
BOTAO_PLAY = 'botao_play'
BOTAO_CONFIG = 'botao_config'
FUNDO_GOL = 'fundo_gol'
TIMES = 'times'
LISTA_MUSICAS = 'lista_musicas'
FONTE_PRINCIPAL = 'fonte_principal'

def load_assets():
    assets = {}
    assets[LOGO] = pygame.image.load(os.path.join(DIR_IMG, 'logo2.png')).convert_alpha()
    assets[FUNDO] = pygame.image.load(os.path.join(DIR_IMG, 'Tela.png')).convert()
    assets[FUNDO_PIX] = pygame.image.load(os.path.join(DIR_IMG, 'Tela pixelada.jpg')).convert()
    assets[BOTAO_PLAY] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_play.png')).convert_alpha()

    imagem_play = pygame.image.load("imagens\imagem_play.png").convert_alpha()
    imagem_escrito = pygame.image.load("imagens\escrito.png").convert_alpha()
    imagem_play_mouse = pygame.image.load("imagens\play_cor.png").convert_alpha()
    imagem_config = pygame.image.load("imagens\Botao config2.png").convert_alpha()
    imagem_config_mouse = pygame.image.load("imagens\Botao config cor.png").convert_alpha()
    imagem_seta = pygame.image.load("imagens/seta volta.png").convert_alpha()
    imagem_seta_mouse = pygame.image.load("imagens/seta volta cor.png").convert_alpha()
    imagem_seta_prox = pygame.image.load("imagens/seta prox.png").convert_alpha()
    imagem_seta_prox_cor = pygame.image.load("imagens/seta prox cor.png").convert_alpha()
    imagem_menu_config = pygame.image.load("imagens/menu config2.png").convert_alpha()