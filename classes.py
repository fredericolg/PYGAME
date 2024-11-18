import pygame
import random
from config import *
from funcoes import *

class Botão:
    def __init__(self, x, y, width_normal, height_normal, img1, width_hover, height_hover, img2, ação=None):
        self.x = x
        self.y = y
        self.width_normal = width_normal
        self.height_normal = height_normal
        self.width_hover = width_hover
        self.height_hover = height_hover

        # Escala as imagens para os tamanhos correspondentes
        self.img1 = pygame.transform.scale(img1, (width_normal, height_normal))  # Estado normal
        self.img2 = pygame.transform.scale(img2, (width_hover, height_hover))    # Estado hover

        self.ação = ação
        self.hover = False

        # Define o retângulo inicial para o estado normal
        self.rect = pygame.Rect(x, y, width_normal, height_normal)

    def draw(self, surface):
        if self.hover:
            # Calcula o retângulo do estado hover (centralizado no retângulo normal)
            hover_rect = self.img2.get_rect(center=self.rect.center)
            surface.blit(self.img2, hover_rect.topleft)
        else:
            # Desenha o botão normal
            surface.blit(self.img1, self.rect.topleft)

    def check_hover(self, mouse_pos):
        # Sempre verifica com base no retângulo do estado normal
        self.hover = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clique com botão esquerdo
            if self.rect.collidepoint(event.pos):
                if self.ação:
                    self.ação()  # Executa a ação associada ao botão

class MusicController:
    def __init__(self, musicas):

        self.musicas = musicas
        self.lista_musicas = list(musicas.keys())  # Lista de nomes das músicas
        self.musica_atual = 0  # Índice da música atual
        self.volume_global = 1.0  # Volume global padrão (1.0 = máximo)

        # Adiciona a chave 'volume' para cada música, com valor inicial igual ao volume global
        for nome in self.lista_musicas:
            self.musicas[nome]["volume"] = self.volume_global

        # Carrega uma música aleatória no início
        self.start_random()

    def start_random(self):
        self.musica_atual = random.randint(0, len(self.lista_musicas) - 1)
        self.play_music()

    def play_music(self):
        nome_musica = self.lista_musicas[self.musica_atual]
        caminho = self.musicas[nome_musica]["path"]
        volume = self.musicas[nome_musica]["volume"]  # Obtém o volume individual da música
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(volume)  # Define o volume
        pygame.mixer.music.play()

    def set_global_volume(self, volume):
        self.volume_global = max(0.0, min(1.0, volume))  # Garante que o volume está entre 0.0 e 1.0
        for nome in self.lista_musicas:
            self.musicas[nome]["volume"] = self.volume_global  # Atualiza o volume de todas as músicas
        pygame.mixer.music.set_volume(self.volume_global)

    def set_individual_volume(self, music_name, volume):
        if music_name in self.musicas:
            self.musicas[music_name]["volume"] = max(0.0, min(1.0, volume))  # Garante que o volume está entre 0.0 e 1.0
            # Atualiza o volume imediatamente se a música atual for a mesma
            if self.lista_musicas[self.musica_atual] == music_name:
                pygame.mixer.music.set_volume(self.musicas[music_name]["volume"])

    def next_music(self):
        self.musica_atual = (self.musica_atual + 1) % len(self.lista_musicas)
        self.play_music()

    def previous_music(self):
        self.musica_atual = (self.musica_atual - 1) % len(self.lista_musicas)
        self.play_music()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def get_current_music_info(self):
        nome_musica = self.lista_musicas[self.musica_atual]
        artista = self.musicas[nome_musica]["artist"]
        volume = self.musicas[nome_musica]["volume"]
        return {"name": nome_musica, "artist": artista, "volume": volume}

class CreateMenu:
    def __init__(self, window, largura, altura):
        self.window = window
        self.largura = largura
        self.altura = altura
        self.rectangles = [
            {"color": PRETO, "largura_r": largura, "altura_r": altura, "offset_x": -18, "offset_y": -18},
            {"color": LARANJA, "largura_r": largura - 6, "altura_r": altura - 6, "offset_x": -15, "offset_y": -15},
            {"color": AZUL_MARINHO, "largura_r": largura - 26, "altura_r": altura - 26, "offset_x": -5, "offset_y": -5},
            {"color": AZUL_CLARO, "largura_r": largura - 36, "altura_r": altura - 36, "offset_x": 0, "offset_y": 0},
        ]

    def draw(self):
        for rect in self.rectangles:
            cria_rect(
                self.window,
                rect["color"],
                self.largura,
                self.altura,
                rect["largura_r"],
                rect["altura_r"],
                rect["offset_x"],
                rect["offset_y"]
            )

class TimeSelector:
    def __init__(self, lista_times, assets, tamanho_escudo):
        self.lista_times = lista_times
        self.assets = assets
        self.tamanho_escudo = tamanho_escudo
        self.indice_time = 0  # Índice inicial do time selecionado
        self.nome_time = self.lista_times[self.indice_time]
        self.escudo_time = self.assets[TIMES][self.nome_time]

    def navegar(self, direcao):
        # Chama a lógica de `atualiza_time` para calcular o novo índice e obter os valores
        self.indice_time, self.nome_time, self.escudo_time = atualiza_time(
            direcao, self.lista_times, self.assets, self.indice_time
        )

    def draw(self, window):
        # Redimensiona o escudo
        escudo_escalado = pygame.transform.scale(self.escudo_time, self.tamanho_escudo)
        escudo_rect = escudo_escalado.get_rect(center=(LARGURA // 2, ALTURA // 2 - 50))
        window.blit(escudo_escalado, escudo_rect)

        # Exibe o nome do time abaixo do escudo
        fonte = self.assets[FONTE_PRINCIPAL]
        texto_nome = fonte.render(self.nome_time, True, PRETO)  # Preto
        texto_rect = texto_nome.get_rect(center=(LARGURA // 2, ALTURA // 2 + 110))
        window.blit(texto_nome, texto_rect)

    def acha_ultimo(self):
        return self.nome_time
    
class JogoPLAY:
    def __init__(self):
        self.pos_bola = None  # Estado do chute
        self.pontuacao_gol = 0
        self.pontuacao_jog = 0

    def define_chute(self, canto):
        self.pos_bola = canto

    def processar_jogada(self, pos_gol):
        if self.pos_bola == pos_gol:
            self.pontuacao_gol += 1
            return "DEFEEEEEEEEEEEEESA!!"
        else:
            self.pontuacao_jog += 1
            return "GOOOOOOOOOOOOOOOOL!!"
        
class Draw:
    
    def imagem(window, imagem, posicao, tamanho=None):
        if tamanho:
            imagem = pygame.transform.scale(imagem, tamanho)  # Redimensiona a imagem
        rect = imagem.get_rect()
        rect.center = posicao
        window.blit(imagem, rect)

    
    def retangulo(window, cor, posicao, tamanho, largura_borda=0):
        rect = pygame.Rect(*posicao, *tamanho)
        pygame.draw.rect(window, cor, rect, width=largura_borda)

    
    def texto(window, texto, posicao, fonte, cor):
        render = fonte.render(texto, True, cor)
        window.blit(render, posicao)
    