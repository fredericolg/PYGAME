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


imagem_seta = pygame.image.load("imagens/seta volta.png").convert_alpha()
imagem_seta_mouse = pygame.image.load("imagens/seta volta cor.png").convert_alpha()
imagem_seta_prox = pygame.image.load("imagens/seta prox.png").convert_alpha()
imagem_seta_prox_cor = pygame.image.load("imagens/seta prox cor.png").convert_alpha()
botao_confirma = pygame.image.load("imagens/botao confirma.png").convert_alpha()
botao_confirma_cor = pygame.image.load("imagens/botao confirma cor.png").convert_alpha()
logo_sp = pygame.image.load("imagens/logo sao paulo.png").convert_alpha()
logo_flu = pygame.image.load("imagens/logo fluminense png.png").convert_alpha()
logo_borussia = pygame.image.load("imagens/logo borussia png.png").convert_alpha()
logo_inter = pygame.image.load("imagens/logo inter miami png.png").convert_alpha()
imagem_gol = pygame.image.load("imagens/tela fundo gol.jpeg").convert_alpha()
bola_chute = pygame.image.load("imagens/Bola de futebol p&b.png").convert_alpha()


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

def muda_estado(novo_estado):
    global state
    state = novo_estado

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

lista_times = list(assets[TIMES].keys())  # Lista de nomes dos times
tamanho_escudo = (250, 250)  # Define o tamanho global dos escudos
time_selector = TimeSelector(lista_times, assets, tamanho_escudo)

LOAD_start = None
LOAD_end = 4000  # Tempo total do carregamento (6 segundos)

msg_start = None
msg_end = 1000

# ========== Parâmetros para o jogo ===========
game_over = False
escolhas_gol = ["Esquerda Superior", "Esquerda Inferior", "Direita Superior", "Direita Inferior"]
rodadas = 0
rodadas_max = 5
msg_gol_duracao = 3000 
msg_gol = ""
pontuacao_jog = 0
pontuacao_gol = 0

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
        imagem_logo = pygame.transform.scale(assets[LOGO], (400, 400))
        imagem_logo_rect = imagem_logo.get_rect(center=(LARGURA / 2, ALTURA / 2 - 50))
        window.blit(imagem_logo, imagem_logo_rect)

        if progresso >= 1:  # Quando o carregamento está completo
            if msg_start is None:  # Inicializa o início da mensagem
                msg_start = pygame.time.get_ticks()
            
            # Exibe a mensagem
            hora_do_gol = assets[FONTE_PRINCIPAL].render('ESTA NA HORA DE FAZER GOL!!!', False, PRETO)
            hora_do_gol_rect = hora_do_gol.get_rect(center=(LARGURA / 2, 520))
            window.blit(hora_do_gol, hora_do_gol_rect)

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
        imagem_escrito = pygame.transform.scale(assets[LOGO_2], (500, 500))
        imagem_escrito_rect=imagem_escrito.get_rect()
        imagem_escrito_rect.center=((LARGURA/2),(ALTURA/2)-150)
        window.blit(imagem_escrito, (imagem_escrito_rect))

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

        font = assets[FONTE_PRINCIPAL]
        nome_musica_text = font.render(nome_musica, True, PRETO)
        artista_text = font.render(artista, True, PRETO)

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


    if state == PLAY:
        fundo_gol = pygame.transform.scale(imagem_gol, (LARGURA, ALTURA))
        window.blit(fundo_gol,(0, 0))
        pos_mouse = pygame.mouse.get_pos()

        larg = 170
        alt = 106

        x_1 = 340
        y_1 = 170
        canto_1 = pygame.Rect(x_1, y_1, larg, alt)
        bola_chute = pygame.transform.scale(bola_chute, (100, 100))
        window.blit(bola_chute, (x_1,y_1))

        x_2 = 690
        y_2 = 170
        canto_2 = pygame.Rect(x_2, y_2, larg, alt)
        bola_chute = pygame.transform.scale(bola_chute, (100, 100))
        window.blit(bola_chute, (x_2+70,y_2))

        x_3 = 340
        y_3 = 382
        canto_3 = pygame.Rect(x_3, y_3, larg, alt)
        bola_chute = pygame.transform.scale(bola_chute, (100, 100))
        window.blit(bola_chute, (x_3,y_3))

        x_4 = 690
        y_4 = 382
        canto_4 = pygame.Rect(x_4, y_4, larg, alt)
        bola_chute = pygame.transform.scale(bola_chute, (100, 100))
        window.blit(bola_chute, (x_4+70,y_4))

        # x_5 = 510
        # y_5 = 276
        # larg_5 = 180
        # canto_5 = pygame.Rect(x_5, y_5, larg_5, alt)
        # bola_chute = pygame.transform.scale(bola_chute, (100, 100))
        # window.blit(bola_chute, (x_5,y_5))

        tempo = pygame.time.get_ticks()

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if not game_over and not msg_gol and event.type == pygame.MOUSEBUTTONDOWN:
                pos_bola = None
                if canto_1.collidepoint(pos_mouse):
                    pos_bola = "Esquerda Superior"
                if canto_2.collidepoint(pos_mouse):
                    pos_bola = "Esquerda Inferior"
                if canto_3.collidepoint(pos_mouse):
                    pos_bola = "Direita Superior"
                if canto_4.collidepoint(pos_mouse):
                    pos_bola = "Direita Inferior"
                # if canto_5.collidepoint(pos_mouse):
                #     pos_bola = "Centro"

                if pos_bola:
                    pos_gol = random.choice(escolhas_gol)

                    if pos_bola != pos_gol:
                        pontuacao_jog += 1
                        msg_gol = "GOOOOOOOOOOOOOOOOL!!"

                    else:
                        pontuacao_gol += 1
                        msg_gol = "DEFEEEEEEEEEEEEESA!!"
                    
                    msg_gol_inicia = tempo

                    rodadas += 1

                    if rodadas == rodadas_max:
                        game_over = True
        


        cor = AZUL
        LARGURA_pla = (150)
        ALTURA_pla = (85)
        tamanho_pla = (LARGURA_pla, ALTURA_pla)
        posicao_pla = (10, 10)
        placar = pygame.draw.rect(window, cor, (posicao_pla, tamanho_pla))
        font = pygame.font.Font("fonte/Minecraft.ttf", 36)
        render_pont_jog = font.render(f'{sigla}: {pontuacao_jog}', True, (255,255,255))
        render_pont_gol = font.render(f'GOL: {pontuacao_gol}', True, (255,255,255) )
        window.blit(render_pont_jog, (20, 20))
        window.blit(render_pont_gol, (20, 60))




        if msg_gol:
            if msg_gol == "GOOOOOOOOOOOOOOOOL!!":
                font = pygame.font.Font("fonte/Minecraft.ttf", 48)
                render_msg_gol = font.render(msg_gol, True, (0,0,0))
                window.blit(render_msg_gol, (270, 75))

                if tempo - msg_gol_inicia  >= msg_gol_duracao:
                    msg_gol = ""  
                    if game_over:
                        state = "game_over"
            else:
                font = pygame.font.Font("fonte/Minecraft.ttf", 48)
                render_msg_gol = font.render(msg_gol, True, (0,0,0))
                window.blit(render_msg_gol, (300, 75))

                if tempo - msg_gol_inicia  >= msg_gol_duracao:
                    msg_gol = ""  
                    if game_over:
                        state = "game_over"

    if state == "game_over":
        aaa = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
        window.blit(aaa,(0, 0))
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
        
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
