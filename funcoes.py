import pygame
import random
from config import *
from assets import *

def desenha_barra(window, progresso, posicao=(200, 450), tamanho=(800, 30), cor_borda = PRETO, cor_barra = VERDE, cor_fundo = BRANCO):
    x, y = posicao
    width, height = tamanho

    # Desenha o fundo da barra
    pygame.draw.rect(window, cor_fundo, (x, y, width, height))

    # Desenha o preenchimento baseado no progresso
    fill_width = int(progresso * width)
    pygame.draw.rect(window, cor_barra, (x, y, fill_width, height))

    # Desenha a borda da barra
    pygame.draw.rect(window, cor_borda, (x, y, width, height), 3)

def cria_rect(window, color, largura, altura, largura_r, altura_r, offset_x=0, offset_y=0):
    tamanho = (largura_r, altura_r)  # Tamanho do retângulo
    posicao = (1 / 4 * largura + offset_x, 1 / 5 * altura + offset_y)  # Posição do retângulo
    pygame.draw.rect(window, color, (*posicao, *tamanho))
