import pygame
import os
from config import DIR_IMG, DIR_WAV, DIR_FNT

LOGO = 'logo'
LOGO_2 = 'logo_escrito'
FUNDO = 'fundo'
FUNDO_PIX = 'fundo_pixelado'
FUNDO_GOL = 'fundo_gol'

BOTAO_PLAY = 'botao_play'
BOTAO_PLAY2 = 'botao_play_mouse'
BOTAO_CONFIG = 'botao_config'
BOTAO_CONFIG2 = 'botao_config_mouse'
BOTAO_CONFIRM = 'botao_confirma'
BOTAO_CONFIRM2 = 'botao_confirma_mouse'

SETA_BACK = 'seta_voltar'
SETA_BACK2 = 'seta_voltar_mouse'
SETA_NEXT = 'seta_prox'
SETA_NEXT2 = 'seta_prox_mouse'

MUSICA_STOP = 'pausa_musica'
MUSICA_NEXT = 'prox_musica'
MUSICA_BACK = 'volta_musica'


TIMES = 'times'
MUSICAS = 'lista_musicas'
FONTE_PRINCIPAL = 'fonte_principal'

def load_assets():
    assets = {}

    assets[LOGO] = pygame.image.load(os.path.join(DIR_IMG, 'logo2.png')).convert_alpha()
    assets[LOGO_2] = pygame.image.load(os.path.join(DIR_IMG, 'escrito.png')).convert_alpha()
    assets[FUNDO] = pygame.image.load(os.path.join(DIR_IMG, 'Tela.png')).convert()
    assets[FUNDO_PIX] = pygame.image.load(os.path.join(DIR_IMG, 'Tela pixelada.jpg')).convert()
    assets[FUNDO_GOL] = pygame.image.load(os.path.join(DIR_IMG, 'tela fundo gol.jpeg.png')).convert_alpha()

    assets[BOTAO_PLAY] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_play.png')).convert_alpha()
    assets[BOTAO_PLAY2] = pygame.image.load(os.path.join(DIR_IMG, 'play_cor.png')).convert_alpha()
    assets[BOTAO_CONFIG] = pygame.image.load(os.path.join(DIR_IMG, 'Botao config2.png')).convert_alpha()
    assets[BOTAO_CONFIG2] = pygame.image.load(os.path.join(DIR_IMG, 'Botao config cor.png')).convert_alpha()
    assets[BOTAO_CONFIRM] = pygame.image.load(os.path.join(DIR_IMG, 'botao confirma.png')).convert_alpha()
    assets[BOTAO_CONFIRM2] = pygame.image.load(os.path.join(DIR_IMG, 'botao confirma cor.png')).convert_alpha()

    assets[SETA_BACK] = pygame.image.load(os.path.join(DIR_IMG, 'seta volta.png')).convert_alpha()
    assets[SETA_BACK2] = pygame.image.load(os.path.join(DIR_IMG, 'seta volta cor.png')).convert_alpha()
    assets[SETA_NEXT] = pygame.image.load(os.path.join(DIR_IMG, 'seta prox.png')).convert_alpha()
    assets[SETA_NEXT2] = pygame.image.load(os.path.join(DIR_IMG, 'seta prox cor.png')).convert_alpha()

    assets[MUSICA_STOP] = pygame.image.load(os.path.join(DIR_IMG, 'botao pause music.png')).convert_alpha()
    assets[MUSICA_NEXT] = pygame.image.load(os.path.join(DIR_IMG, 'botao next music.png')).convert_alpha()
    assets[MUSICA_BACK] = pygame.image.load(os.path.join(DIR_IMG, 'botao previous music.png')).convert_alpha()
    

    assets[TIMES] = {
        "São Paulo FC": pygame.image.load(os.path.join(DIR_IMG, 'logo sao paulo.png')).convert_alpha(),
        "Fluminense": pygame.image.load(os.path.join(DIR_IMG, 'logo fluminense png.png')).convert_alpha(),
        "Borussia Dortmund": pygame.image.load(os.path.join(DIR_IMG, 'logo borussia png.png')).convert_alpha(),
        "Inter Miami": pygame.image.load(os.path.join(DIR_IMG, 'logo inter miami png.png')).convert_alpha(),
    }

    assets[FONTE_PRINCIPAL] = pygame.font.Font(os.path.join(DIR_FNT, 'Minecraft.ttf'), 48)

    assets[MUSICAS] = {
        "Feet Don't Fail Me Now": os.path.join(DIR_WAV, '1.mp3'),
        "Wavin Flags": os.path.join(DIR_WAV, '2.mp3'),
        "Miss Alissa": os.path.join(DIR_WAV, '3.mp3'),
        "My Type": os.path.join(DIR_WAV, '4.mp3'),
        "We Are One": os.path.join(DIR_WAV, '5.mp3'),
    }

    return assets