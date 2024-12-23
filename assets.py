import pygame
import os
from config import DIR_IMG, DIR_WAV, DIR_FNT

LOGO = 'logo'
LOGO_2 = 'logo_escrito'
FUNDO = 'fundo'
FUNDO_PIX = 'fundo_pixelado'
FUNDO_GOL = 'fundo_gol'

BOLA_CHUTE = 'bola_chute'
BOTAO_PLAY = 'botao_play'
BOTAO_PLAY2 = 'botao_play_mouse'
BOTAO_CONFIG = 'botao_config'
BOTAO_CONFIG2 = 'botao_config_mouse'
BOTAO_CONFIRM = 'botao_confirma'
BOTAO_CONFIRM2 = 'botao_confirma_mouse'
GOLEIRO = "imagem_goleiro"
BOLA = "imagem_bola"
BOLA2 = "imagem_bola2"

BOTAO_PLAY_AGAIN = 'botao_play_again'
BOTAO_PLAY_AGAIN2 = 'botao_play_again_mouse'
BOTAO_QUIT = 'botao_quit'
BOTAO_QUIT2 = 'botao_quit_mouse'

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
FONTE_PEQUENA = "Fsmall"
FONTE_GRANDE = "Fbig"

def load_assets():
    assets = {}

    assets[LOGO] = pygame.image.load(os.path.join(DIR_IMG, 'logo2.png')).convert_alpha()
    assets[LOGO_2] = pygame.image.load(os.path.join(DIR_IMG, 'escrito.png')).convert_alpha()
    assets[FUNDO] = pygame.image.load(os.path.join(DIR_IMG, 'Tela.png')).convert()
    assets[FUNDO_PIX] = pygame.image.load(os.path.join(DIR_IMG, 'Tela pixelada.jpg')).convert()
    assets[FUNDO_GOL] = pygame.image.load(os.path.join(DIR_IMG, 'tela fundo gol.jpeg')).convert_alpha()

    assets[BOTAO_PLAY] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_play.png')).convert_alpha()
    assets[BOTAO_PLAY2] = pygame.image.load(os.path.join(DIR_IMG, 'play_hover.png')).convert_alpha()
    assets[BOTAO_CONFIG] = pygame.image.load(os.path.join(DIR_IMG, 'Botao config2.png')).convert_alpha()
    assets[BOTAO_CONFIG2] = pygame.image.load(os.path.join(DIR_IMG, 'Botao config cor.png')).convert_alpha()
    assets[BOTAO_CONFIRM] = pygame.image.load(os.path.join(DIR_IMG, 'botao confirma.png')).convert_alpha()
    assets[BOTAO_CONFIRM2] = pygame.image.load(os.path.join(DIR_IMG, 'botao confirma cor.png')).convert_alpha()
    assets[BOLA_CHUTE] = pygame.image.load(os.path.join(DIR_IMG, 'Bola de futebol p&b.png')).convert_alpha()
    assets[GOLEIRO] = pygame.image.load(os.path.join(DIR_IMG, 'goleiro pixelado.png')).convert_alpha()

    assets[BOLA] = pygame.image.load(os.path.join(DIR_IMG, 'bola fut.png')).convert_alpha()
    assets[BOLA2] = pygame.image.load(os.path.join(DIR_IMG, 'Football_White_Filled.png')).convert_alpha()

    assets[BOTAO_PLAY_AGAIN] = pygame.image.load(os.path.join(DIR_IMG, 'botao play again.png')).convert_alpha()
    assets[BOTAO_PLAY_AGAIN2] = pygame.image.load(os.path.join(DIR_IMG, 'botao play again cor.png')).convert_alpha()
    assets[BOTAO_QUIT] = pygame.image.load(os.path.join(DIR_IMG, 'botao quit.png')).convert_alpha()
    assets[BOTAO_QUIT2] = pygame.image.load(os.path.join(DIR_IMG, 'botao quit cor.png')).convert_alpha()    

    assets[SETA_BACK] = pygame.image.load(os.path.join(DIR_IMG, 'seta volta.png')).convert_alpha()
    assets[SETA_BACK2] = pygame.image.load(os.path.join(DIR_IMG, 'seta volta cor.png')).convert_alpha()
    assets[SETA_NEXT] = pygame.image.load(os.path.join(DIR_IMG, 'seta prox.png')).convert_alpha()
    assets[SETA_NEXT2] = pygame.image.load(os.path.join(DIR_IMG, 'seta prox cor.png')).convert_alpha()

    assets[MUSICA_STOP] = pygame.image.load(os.path.join(DIR_IMG, 'botao pause music.png')).convert_alpha()
    assets[MUSICA_NEXT] = pygame.image.load(os.path.join(DIR_IMG, 'botao next music.png')).convert_alpha()
    assets[MUSICA_BACK] = pygame.image.load(os.path.join(DIR_IMG, 'botao previous music.png')).convert_alpha()
    

    assets[TIMES] = {
        "Sao Paulo FC": pygame.image.load(os.path.join(DIR_IMG, 'logo sao paulo.png')).convert_alpha(),
        "Fluminense FC": pygame.image.load(os.path.join(DIR_IMG, 'logo fluminense png.png')).convert_alpha(),
        "Borussia Dortmund": pygame.image.load(os.path.join(DIR_IMG, 'logo borussia png.png')).convert_alpha(),
        "Inter Miami": pygame.image.load(os.path.join(DIR_IMG, 'logo inter miami png.png')).convert_alpha(),
    }

    assets[FONTE_PRINCIPAL] = pygame.font.Font(os.path.join(DIR_FNT, 'Minecraft.ttf'), 48)
    assets[FONTE_PEQUENA] = pygame.font.Font(os.path.join(DIR_FNT, 'Minecraft.ttf'), 36)
    assets[FONTE_GRANDE] = pygame.font.Font(os.path.join(DIR_FNT, 'Minecraft.ttf'), 100)

    assets[MUSICAS] = {
    "Feet Don't Fail Me Now": {"path": os.path.join(DIR_WAV, '1.mp3'), "artist": "Joy Crookes"},
    "Wavin Flags": {"path": os.path.join(DIR_WAV, '2.mp3'), "artist": "K'naan"},
    "Miss Alissa": {"path": os.path.join(DIR_WAV, '3.mp3'), "artist": "Eagles of Death Metal"},
    "My Type": {"path": os.path.join(DIR_WAV, '4.mp3'), "artist": "SAINT MOTEL"},
    "We Are One": {"path": os.path.join(DIR_WAV, '5.mp3'), "artist": "Pitbull, J-Lo, Claudia Leitte"},
}

    return assets