from os import path

# Acessa Pastas
BASE_DIR = path.dirname(__file__)
DIR_IMG = path.join(BASE_DIR, 'assets', 'imagens')
DIR_WAV = path.join(BASE_DIR, 'assets', 'audios')
DIR_FNT = path.join(BASE_DIR, 'assets', 'fonte')

# Declara Constantes
LARGURA = 1200
ALTURA = 600
TITULO = "Penalty Shootout"
FPS = 60

# Declara Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (173, 216, 230)
AZUL_MARINHO = (60, 72, 92)
LARANJA = (255, 100, 0)

#Estados do Jogo
LOAD = 0 # Tela de Carregamento
INIT = 1 # Tela Inicial
CONFIG = 2 # Tela de Configurações
SELECT = 3 # Tela de Seleção de Times
PLAY = 4 # Tela Disputa