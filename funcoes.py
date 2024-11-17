import pygame
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

def controla_musica(ação, musicas, musica_atual):
    lista_musicas = list(musicas.items())  # Converte para lista de tuplas [(nome, {"path": caminho, "artist": artista})]
    if ação == 'play':
        if not pygame.mixer.music.get_busy():  # Apenas toca se não estiver tocando
            pygame.mixer.music.play()
    elif ação == 'pause':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    elif ação == 'next':
        musica_atual = (musica_atual + 1) % len(lista_musicas)  # Vai para a próxima música
        pygame.mixer.music.load(lista_musicas[musica_atual][1]['path'])  # Carrega o caminho da música
        pygame.mixer.music.play()
    elif ação == 'previous':
        musica_atual = (musica_atual - 1) % len(lista_musicas)  # Volta para a música anterior
        pygame.mixer.music.load(lista_musicas[musica_atual][1]['path'])  # Carrega o caminho da música
        pygame.mixer.music.play()

    return musica_atual
