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
    
class MenuCONFIG:
    def __init__(self, window, largura, altura):
        self.window = window
        self.largura = largura
        self.altura = altura
        self.rectangles = [
            {"color": PRETO, "largura_r": 636, "altura_r": 436, "offset_x": -18, "offset_y": -18},
            {"color": LARANJA, "largura_r": 630, "altura_r": 430, "offset_x": -15, "offset_y": -15},
            {"color": AZUL_MARINHO, "largura_r": 610, "altura_r": 410, "offset_x": -5, "offset_y": -5},
            {"color": AZUL_CLARO, "largura_r": 600, "altura_r": 400, "offset_x": 0, "offset_y": 0},
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