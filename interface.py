# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *
from assets import *
from funcoes import *
from classes import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)
assets = load_assets()
music_controller = MusicController(assets[MUSICAS])
music_controller.set_global_volume(0.8)
music_controller.set_individual_volume("Feet Don't Fail Me Now", 1)


imagem_seta = assets[SETA_BACK]
imagem_seta_mouse = assets[SETA_BACK2]
imagem_seta_prox = assets[SETA_NEXT]
imagem_seta_prox_cor = assets[SETA_NEXT2]
botao_confirma = assets[BOTAO_CONFIRM]
botao_confirma_cor = assets[BOTAO_CONFIRM2]
logo_sp = pygame.image.load("imagens/logo sao paulo.png").convert_alpha()
logo_flu = pygame.image.load("imagens/logo fluminense png.png").convert_alpha()
logo_borussia = pygame.image.load("imagens/logo borussia png.png").convert_alpha()
logo_inter = pygame.image.load("imagens/logo inter miami png.png").convert_alpha()
imagem_gol = assets[FUNDO_GOL]
bola_chute = assets[BOLA_CHUTE]


game = True
# === tempo de primeira tela (tela de carregamento)
state = LOAD

# def game_screen(window):
clock = pygame.time.Clock()

LOAD = 0 
INIT = 1 
CONFIG = 2 
SELECT = 3 
PLAY = 4
GAMEOVER = 5
QUIT = 6

def muda_estado(novo_estado):
    global state
    state = novo_estado

def reseta_jogo():
    global JogoP, state, rodadas
    JogoP = JogoPLAY()  # Nova instância para resetar placar
    rodadas = 0
    state = SELECT  # Volta ao estado inicial

# Botões INIT
botao_play = Botão((LARGURA/2) - 90, (ALTURA/2) + 15, 200, 100, assets[BOTAO_PLAY], 195, 95, assets[BOTAO_PLAY2], ação = lambda: muda_estado(SELECT))
botao_config = Botão((LARGURA/2) - 90, (ALTURA/2) + 110, 200, 185, assets[BOTAO_CONFIG], 345, 335, assets[BOTAO_CONFIG2], ação = lambda: muda_estado(CONFIG))

# Botões CONFIG
botao_pause = Botão((LARGURA/2) - 35, (ALTURA/2) + 20, 50, 50, assets[MUSICA_STOP], 50, 50, assets[MUSICA_STOP], ação = lambda: music_controller.pause_music())
botao_back = Botão((LARGURA/2) - 100, (ALTURA * 1/2) + 25, 50, 50, assets[MUSICA_BACK], 50, 50, assets[MUSICA_BACK], ação = lambda: music_controller.previous_music())
botao_next = Botão((LARGURA/2) + 35, (ALTURA * 1/2) + 25, 50, 50, assets[MUSICA_NEXT], 50, 50, assets[MUSICA_NEXT], ação = lambda: music_controller.next_music())
botao_volta1 = Botão(0, 0, 65, 65, assets[SETA_BACK], 65, 65, assets[SETA_BACK2], ação = lambda: muda_estado(INIT))

# Botões SELECT
botao_volta2 = Botão(0, 0, 65, 65, assets[SETA_BACK], 65, 65, assets[SETA_BACK2], ação = lambda: muda_estado(INIT))
botao_confirma = Botão(500, 385, 200, 200, assets[BOTAO_CONFIRM], 200, 200, assets[BOTAO_CONFIRM2], ação = lambda: muda_estado(PLAY))
seta_esq = Botão(240, 265, 150, 150, assets[SETA_BACK], 150, 150, assets[SETA_BACK2], ação = lambda: time_selector.navegar(-1))
seta_dir = Botão(810, 265, 150, 150, assets[SETA_NEXT], 150, 150, assets[SETA_NEXT2], ação = lambda: time_selector.navegar(1))

# Botões Play
bola_top1 = Botão(336, 165, 100, 100, assets[BOLA_CHUTE], 100, 100, assets[BOLA2], ação = lambda: JogoP.define_chute("Esquerda Superior"))
bola_top2 = Botão(764, 165, 100, 100, assets[BOLA_CHUTE], 100, 100, assets[BOLA2], ação = lambda: JogoP.define_chute("Direita Superior"))
bola_baixo1 = Botão(336, 392, 100, 100, assets[BOLA_CHUTE], 100, 100, assets[BOLA2], ação = lambda: JogoP.define_chute("Esquerda Inferior"))
bola_baixo2 = Botão(764, 392, 100, 100, assets[BOLA_CHUTE], 100, 100, assets[BOLA2], ação = lambda: JogoP.define_chute("Direita Inferior"))

# Botões GAMEOVER
botao_play_again = Botão(220, (ALTURA/2) - 10, 400, 300, assets[BOTAO_PLAY_AGAIN], 400, 300, assets[BOTAO_PLAY_AGAIN2], ação = lambda: reseta_jogo())
botao_quit = Botão(600, (ALTURA/2) - 50, 400, 385, assets[BOTAO_QUIT], 415, 395, assets[BOTAO_QUIT2], ação = lambda: muda_estado(QUIT))

lista_times = list(assets[TIMES].keys())  # Lista de nomes dos times
tamanho_escudo = (250, 250)  # Define o tamanho global dos escudos
time_selector = TimeSelector(lista_times, assets, tamanho_escudo)
JogoP = JogoPLAY()

LOAD_start = None
LOAD_end = 4000  # Tempo total do carregamento (6 segundos)

msg_start = None
msg_end = 1000

# ========== Parâmetros para o jogo ===========
game_over = False
escolhas_gol = ["Esquerda Superior", "Esquerda Inferior", "Direita Superior", "Direita Inferior"]
rodadas = 0
rodadas_max = 5
msg_gol_duracao = 1000 
msg_gol = ""
pontuacao_jog = 0
pontuacao_gol = 0
rodadas = 0
game_over = ""

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    if state == LOAD:
        if LOAD_start is None:  # Inicializa apenas na primeira vez
            LOAD_start = pygame.time.get_ticks()

        time_spent = pygame.time.get_ticks() - LOAD_start

        # Calcula o progresso (0 a 1)
        progresso = min(time_spent / LOAD_end, 1)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas

        img_fundo = pygame.transform.scale(assets[FUNDO], (LARGURA, ALTURA))
        window.blit(img_fundo, (0, 0))

        desenha_barra(window, progresso)
        # ==== fica 6 segundos na tela de carregamento

        # imprime o logo no tela
        Draw.imagem(window, assets[LOGO], (LARGURA / 2, ALTURA / 2 - 50), (400, 400))

        if progresso >= 1:  # Quando o carregamento está completo
            if msg_start is None:  # Inicializa o início da mensagem
                msg_start = pygame.time.get_ticks()
            
            # Exibe a mensagem
            Draw.texto(window, 'ESTA NA HORA DE FAZER GOL!!!', (200, 500), assets[FONTE_PRINCIPAL], PRETO)

            # Verifica se o tempo de exibição da mensagem passou
            if pygame.time.get_ticks() - msg_start >= msg_end:
                LOAD_start = None  # Reseta para o próximo uso
                msg_start = None   # Reseta a mensagem para o próximo ciclo
                state = INIT

    
    # TELA DE INÍCIO

    if state == INIT:
        imagem_fundo = pygame.transform.scale(assets[FUNDO], (LARGURA, ALTURA))
        window.blit(imagem_fundo, (0, 0))

        # Obtém a posição do mouse para verificar hover
        mouse_pos = pygame.mouse.get_pos()

        # Atualiza hover dos botões
        botao_play.check_hover(mouse_pos)
        botao_config.check_hover(mouse_pos)

        # Desenha os botões
        botao_play.draw(window)
        botao_config.draw(window)

        # coloca o escrito "PENALTY SHOOT OUT" na tela
        Draw.imagem(window, assets[LOGO_2], ((LARGURA/2),(ALTURA/2)-150), (500, 500))

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            
            botao_play.handle_event(event)
            botao_config.handle_event(event)

    # === TELA CONFIGURAÇÃO
    
    if state == CONFIG:
        imagem_fundo_pix = pygame.transform.scale(assets[FUNDO_PIX], (LARGURA, ALTURA))
        window.blit(imagem_fundo_pix, (0, 0))

        musica_info = music_controller.get_current_music_info()
        nome_musica = musica_info["name"]
        artista = musica_info["artist"]

        menuCONFIG = CreateMenu(window, 816, 436)
        menuCONFIG.draw()

        nome_musica_text = assets[FONTE_PRINCIPAL].render(nome_musica, True, PRETO)
        artista_text = assets[FONTE_PRINCIPAL].render(artista, True, PRETO)

        # Centraliza e exibe os textos
        nome_musica_rect = nome_musica_text.get_rect(center=(LARGURA // 2, ALTURA // 2 - 50))
        artista_rect = artista_text.get_rect(center=(LARGURA // 2, ALTURA // 2))
        window.blit(nome_musica_text, nome_musica_rect)
        window.blit(artista_text, artista_rect)

        # Atualiza o estado hover dos botões
        mouse_pos = pygame.mouse.get_pos()
        botao_pause.check_hover(mouse_pos)
        botao_next.check_hover(mouse_pos)
        botao_back.check_hover(mouse_pos)
        botao_volta1.check_hover(mouse_pos)

        # Desenha os botões
        botao_pause.draw(window)
        botao_next.draw(window)
        botao_back.draw(window)
        botao_volta1.draw(window)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                botao_back.handle_event(event)
                botao_next.handle_event(event)
                botao_pause.handle_event(event)
                botao_volta1.handle_event(event)
    
    
    if state == SELECT:
        window.blit(imagem_fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        botao_volta2.check_hover(mouse_pos)
        seta_esq.check_hover(mouse_pos)
        seta_dir.check_hover(mouse_pos)
        botao_confirma.check_hover(mouse_pos)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            
            botao_volta2.handle_event(event)
            botao_confirma.handle_event(event)
            seta_esq.handle_event(event)
            seta_dir.handle_event(event)

        menuSELECT = CreateMenu(window, 836, 506)
        menuSELECT.draw()

        botao_volta2.draw(window)
        seta_esq.draw(window)
        seta_dir.draw(window)
        botao_confirma.draw(window)
        time_selector.draw(window)

        time_select = time_selector.acha_ultimo()

        # Mapeia nomes dos times para suas siglas
        siglas_times = {
            "Sao Paulo FC": "SAO",
            "Fluminense FC": "FLU",
            "Borussia Dortmund": "DOR",
            "Inter Miami": "MIA"
        }

        # Define a sigla com segurança
        sigla = siglas_times.get(time_select, "N/A")

    if state == PLAY:
        fundo_gol = pygame.transform.scale(imagem_gol, (LARGURA, ALTURA))
        window.blit(fundo_gol,(0, 0))

        mouse_pos = pygame.mouse.get_pos()
        bola_top1.check_hover(mouse_pos)
        bola_top2.check_hover(mouse_pos)
        bola_baixo1.check_hover(mouse_pos)
        bola_baixo2.check_hover(mouse_pos)

        # Desenha os botões
        bola_top1.draw(window)
        bola_top2.draw(window)
        bola_baixo1.draw(window)
        bola_baixo2.draw(window)

        Draw.imagem(window, assets[GOLEIRO], (LARGURA/2, ALTURA/2 + 70), (400, 400))
        Draw.imagem(window, assets[BOLA], (LARGURA/2 + 5, ALTURA/2 + 250), (100, 100))

        pos_mouse = pygame.mouse.get_pos()

        tempo = pygame.time.get_ticks()

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if not game_over and not msg_gol and event.type == pygame.MOUSEBUTTONDOWN:
                bola_top1.handle_event(event)
                bola_top2.handle_event(event)
                bola_baixo1.handle_event(event)
                bola_baixo2.handle_event(event)

                canto_gol = random.choice(escolhas_gol)

                msg_gol = JogoP.processar_jogada(canto_gol)

                msg_gol_inicia = tempo

                rodadas += 1

                if rodadas == rodadas_max:
                    game_over = True
        

        Draw.retangulo(window, AZUL, (10, 10), (150, 85), 0)
        Draw.texto(window, f'{sigla}:', (20, 20), assets[FONTE_PEQUENA], BRANCO)
        Draw.texto(window, f'{JogoP.pontuacao_jog}', (125, 20), assets[FONTE_PEQUENA], BRANCO)
        Draw.texto(window, f'GOL:', (20, 60), assets[FONTE_PEQUENA], BRANCO)
        Draw.texto(window, f'{JogoP.pontuacao_gol}', (125, 60), assets[FONTE_PEQUENA], BRANCO)
        
        if msg_gol:
            if msg_gol == "GOOOOOOOOOOOOOOOOL!!":
                    Draw.texto(window, msg_gol, (270, 75), assets[FONTE_PRINCIPAL], PRETO)

                    if tempo - msg_gol_inicia  >= msg_gol_duracao:
                        msg_gol = ""  
                        if game_over:
                            state = GAMEOVER
            else:
                Draw.texto(window, msg_gol, (300, 75), assets[FONTE_PRINCIPAL], PRETO)

                if tempo - msg_gol_inicia  >= msg_gol_duracao:
                    msg_gol = ""  
                    if game_over:
                        state = GAMEOVER

    if state == GAMEOVER:
        imagem_fundo_pix = pygame.transform.scale(assets[FUNDO_PIX], (LARGURA, ALTURA))
        window.blit(imagem_fundo_pix, (0, 0))
        menuGAMEOVER = CreateMenu(window, 836, 506)
        menuGAMEOVER.draw()


        if JogoP.pontuacao_jog > JogoP.pontuacao_gol:
            Draw.texto(window, "Bela Conquista!", (245, 130), assets[FONTE_GRANDE], PRETO)
            Draw.texto(window, (f"Placar Final: {sigla}: {JogoP.pontuacao_jog} | GOL: {JogoP.pontuacao_gol}"), (375, 280), assets[FONTE_PEQUENA], PRETO)

        else:
            Draw.texto(window, "HA, Perninha...", (245, 130), assets[FONTE_GRANDE], PRETO)
            Draw.texto(window, (f"Placar Final: {sigla}: {JogoP.pontuacao_jog} | GOL: {JogoP.pontuacao_gol}"), (375, 280), assets[FONTE_PEQUENA], PRETO)


        # Obtém a posição do mouse para verificar hover
        mouse_pos = pygame.mouse.get_pos()

        # Atualiza hover dos botões
        botao_play_again.check_hover(mouse_pos)
        botao_quit.check_hover(mouse_pos)

        # Desenha os botões
        botao_play_again.draw(window)
        botao_quit.draw(window)


        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            
            botao_play_again.handle_event(event)
            botao_quit.handle_event(event)
    
    if state == QUIT:
        game = False


        
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
