# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *
from assets import *
from funcoes import *

pygame.init()
pygame.mixer.init()
pygame.font.init()


# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)
assets = load_assets()
musica_atual = 0
musica_atual = musica_manager('start', assets[MUSICAS])

imagem_logo = pygame.image.load("imagens\logo2.png").convert_alpha()
imagem_fundo = pygame.image.load("imagens\Tela.png").convert()
imagem_fundo_pix = pygame.image.load("imagens/Tela pixelada.jpg").convert()
imagem_play = pygame.image.load("imagens\imagem_play.png").convert_alpha()
imagem_escrito = pygame.image.load("imagens\escrito.png").convert_alpha()
imagem_play_mouse = pygame.image.load("imagens\play_cor.png").convert_alpha()
imagem_config = pygame.image.load("imagens\Botao config2.png").convert_alpha()
imagem_config_mouse = pygame.image.load("imagens\Botao config cor.png").convert_alpha()
imagem_seta = pygame.image.load("imagens/seta volta.png").convert_alpha()
imagem_seta_mouse = pygame.image.load("imagens/seta volta cor.png").convert_alpha()
imagem_seta_prox = pygame.image.load("imagens/seta prox.png").convert_alpha()
imagem_seta_prox_cor = pygame.image.load("imagens/seta prox cor.png").convert_alpha()
botao_pause_music = pygame.image.load("imagens/botao pause music.png").convert_alpha()
botao_next_music = pygame.image.load("imagens/botao next music.png").convert_alpha()
botao_previous_music = pygame.image.load("imagens/botao previous music.png").convert_alpha()
botao_confirma = pygame.image.load("imagens/botao confirma.png").convert_alpha()
botao_confirma_cor = pygame.image.load("imagens/botao confirma cor.png").convert_alpha()
logo_sp = pygame.image.load("imagens/logo sao paulo.png").convert_alpha()
logo_flu = pygame.image.load("imagens/logo fluminense png.png").convert_alpha()
logo_borussia = pygame.image.load("imagens/logo borussia png.png").convert_alpha()
logo_inter = pygame.image.load("imagens/logo inter miami png.png").convert_alpha()
imagem_gol = pygame.image.load("imagens/tela fundo gol.jpeg").convert_alpha()


#========= Texto

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

game = True
# === tempo de primeira tela (tela de carregamento)
state = LOAD

# === imagem times de futebol
i = 0
lista_times = [logo_sp, logo_flu, logo_borussia, logo_inter]
dicio_times = {

    "São Paulo FC":lista_times[0], 
    "Fluminense":lista_times[1],
    "Borussia":lista_times[2],
    "Inter Miami":lista_times[3]

    }

# ================= Cria uma lista com as músicas para depois tocar ============= #
lista_musica = ['audios/1.mp3', 'audios/2.mp3', 'audios/3.mp3', 'audios/4.mp3', 'audios/5.mp3']
dicio_musica = {

    "Feet don't fail me now":'audios/1.mp3',
    "Wavin flags":'audios/2.mp3',
    "Miss Alissa":'audios/3.mp3',
    "My type":'audios/4.mp3',
    "We are one":'audios/5.mp3'

}
variavelmusica = random.randint(0,4) 
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

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
botao_pause = Botão((LARGURA/2) - 35, (ALTURA/2) + 20, 50, 50, assets[MUSICA_STOP], 50, 50, assets[MUSICA_STOP], ação = lambda: musica_manager('pause', assets[MUSICAS], musica_atual))
botao_back = Botão((LARGURA/2) - 100, (ALTURA * 1/2) + 25, 50, 50, assets[MUSICA_BACK], 50, 50, assets[MUSICA_BACK], ação = lambda: musica_manager('back', assets[MUSICAS], musica_atual))
botao_next = Botão((LARGURA/2) + 20, (ALTURA * 1/2) + 25, 50, 50, assets[MUSICA_NEXT], 50, 50, assets[MUSICA_NEXT], ação = lambda: musica_manager('next', assets[MUSICAS], musica_atual))
botao_volta = Botão(0, 0, 65, 65, assets[SETA_BACK], 65, 65, assets[SETA_BACK2], ação = lambda: muda_estado(INIT))

LOAD_start = None
LOAD_end = 4000  # Tempo total do carregamento (6 segundos)

msg_start = None
msg_end = 1000

# ========== Parâmetros para o jogo ===========
game_over = False
escolhas_gol = ["Esquerda Superior", "Esquerda Inferior", "Centro", "Direita Superior", "Direita Inferior"]
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

        # ============== Músicas ================= #
        if not pygame.mixer.music.get_busy():       
            pygame.mixer.music.load(lista_musica[variavelmusica])
            pygame.mixer.music.set_volume(0.2)
            if variavelmusica == 1:
                pygame.mixer.music.play(0, start=11)
                variavelmusica += 1
            if variavelmusica != 1 and variavelmusica != 4:
                pygame.mixer.music.play(0, start=0.1)
                variavelmusica += 1
            if variavelmusica == 4:
                variavelmusica = 0

        # Obtém a posição do mouse para verificar hover
        mouse_pos = pygame.mouse.get_pos()

        # Atualiza hover dos botões
        botao_play.check_hover(mouse_pos)
        botao_config.check_hover(mouse_pos)

        # Desenha os botões
        botao_play.draw(window)
        botao_config.draw(window)

        # coloca o escrito "PENALTY SHOOT OUT" na tela
        imagem_escrito = pygame.transform.scale(imagem_escrito, (500, 500))
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

        imagem_fundo_pix = pygame.transform.scale(imagem_fundo_pix, (LARGURA, ALTURA))
        window.blit(imagem_fundo_pix, (0, 0))

        # === Retangulo do menu
            # Retangulo preto (contorno)
        cor = PRETO
        LARGURA_r = (636)
        ALTURA_r = (436)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/4 * LARGURA - 18, 1/5 * ALTURA - 18)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo laranja
        cor = LARANJA
        LARGURA_r = (630)
        ALTURA_r = (430)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/4 * LARGURA - 15, 1/5 * ALTURA - 15)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul marinho
        cor = AZUL_MARINHO
        LARGURA_r = (610)
        ALTURA_r = (410)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/4 * LARGURA - 5, 1/5 * ALTURA - 5)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul claro
        cor = AZUL_CLARO
        LARGURA_r = (ALTURA)
        ALTURA_r = (400)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/4 * LARGURA, 1/5 * ALTURA)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))

        nome_musicas = list(assets[MUSICAS].keys())
        if nome_musicas:
            # Obtém o nome e o artista da música atual
            musica_atual_nome = nome_musicas[musica_atual]
            musica_atual_info = assets[MUSICAS][musica_atual_nome]
            artista = musica_atual_info["artist"]

            # Renderiza textos
            font = assets[FONTE_PRINCIPAL]
            nome_musica_text = font.render(musica_atual_nome, True, PRETO)
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
        botao_volta.check_hover(mouse_pos)

        # Desenha os botões
        botao_pause.draw(window)
        botao_next.draw(window)
        botao_back.draw(window)
        botao_volta.draw(window)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                botao_back.handle_event(event)
                botao_next.handle_event(event)
                botao_pause.handle_event(event)
                botao_volta.handle_event(event)


    if state == SELECT:
        
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_colisao.collidepoint(mouse_pos):
                    state = INIT
                if retangulo_colisao_prox.collidepoint(mouse_pos):
                    if i < 3:
                        i += 1
                    else:
                        i = 0
                if retangulo_colisao_ant.collidepoint(mouse_pos):
                    if i > 0:
                        i -= 1
                    else:
                        i = 3
                if botao_confirma_rect.collidepoint(mouse_pos):
                    state = PLAY
        
        cor = PRETO
        vertices = [(20, 15), (20, 45), (55, 45), (55, 15)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices)

        window.blit(imagem_fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        if retangulo_colisao.collidepoint(mouse_pos):
            imagem_seta_mouse = pygame.transform.scale(imagem_seta_mouse, (65, 65))
            window.blit(imagem_seta_mouse, (0, 0))
        else:
            imagem_seta_1 = pygame.transform.scale(imagem_seta, (65, 65))
            window.blit(imagem_seta_1, (0, 0))


            # Retangulo preto (contorno)
        LARGURA_r = 836
        ALTURA_r = 506

        cor = PRETO
        LARGURA_r = (LARGURA_r)
        ALTURA_r = (ALTURA_r)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/6 * LARGURA - 18, 1/7 * ALTURA - 18)
        pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo laranja
        cor = LARANJA
        LARGURA_r = (LARGURA_r - 6)
        ALTURA_r = (ALTURA_r - 6)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/6 * LARGURA - 15, 1/7 * ALTURA - 15)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul marinho
        cor = AZUL_MARINHO
        LARGURA_r = (LARGURA_r - 20)
        ALTURA_r = (ALTURA_r - 20)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/6 * LARGURA - 5, 1/7 * ALTURA - 5)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul claro
        cor = AZUL_CLARO
        LARGURA_r = (LARGURA_r - 10)
        ALTURA_r = (ALTURA_r - 10)
        tamanho = (LARGURA_r, ALTURA_r)
        posicao = (1/6 * LARGURA, 1/7 * ALTURA)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))

        # === Colocar e escolha dos times
        
        time = pygame.transform.scale(lista_times[i], (250, 250))
        time_rect=time.get_rect()
        time_rect.center = ((LARGURA * 1/2), (ALTURA * 1/2))
        window.blit(time, (time_rect))

        # Passar para o próximo time

        cor = PRETO
        retangulo_colisao_prox = pygame.draw.rect(window, cor, (730, 360, 75, 40))
        #print(mouse_pos)

        if retangulo_colisao_prox.collidepoint(mouse_pos):
            imagem_seta_prox_cor = pygame.transform.scale(imagem_seta_prox_cor, (150, 150))
            window.blit(imagem_seta_prox_cor, (700, 300))
        else:
            imagem_seta_prox = pygame.transform.scale(imagem_seta_prox, (150, 150))
            window.blit(imagem_seta_prox, (700, 300))

        # Voltar o time

        retangulo_colisao_ant = pygame.draw.rect(window, cor, (395, 360, 75, 40))
        if retangulo_colisao_ant.collidepoint(mouse_pos):
            imagem_seta_mouse = pygame.transform.scale(imagem_seta_mouse, (150, 150))
            window.blit(imagem_seta_mouse, (350, 298))
        else:
            imagem_seta_2 = pygame.transform.scale(imagem_seta, (150, 150))
            window.blit(imagem_seta_2, (350, 300))

        # Confirma o time
            # cria o botão de confirmar
        botao_confirma = pygame.transform.scale(botao_confirma, (200, 200))
        botao_confirma_rect = botao_confirma.get_rect()
        botao_confirma_rect.center = ((ALTURA, 500))
        window.blit(botao_confirma, (botao_confirma_rect))
        
        if botao_confirma_rect.collidepoint(mouse_pos):
            botao_confirma_cor = pygame.transform.scale(botao_confirma_cor, (200, 200))
            botao_confirma_cor_rect = botao_confirma_cor.get_rect()
            botao_confirma_cor_rect.center = ((ALTURA, 500))
            window.blit(botao_confirma_cor, (botao_confirma_cor_rect))
        else:
            botao_confirma = pygame.transform.scale(botao_confirma, (200, 200))
            botao_confirma_rect = botao_confirma.get_rect()
            botao_confirma_rect.center = ((ALTURA, 500))
            window.blit(botao_confirma, (botao_confirma_rect))
        
        time_atual = lista_times[i]

        if i == 0:
            sigla = "SAO"
        if i == 1:
            sigla = "FLU"
        if i == 2:
            sigla = "DOR"
        if i == 3:
            sigla = "MIA"


    if state == PLAY:
        fundo_gol = pygame.transform.scale(imagem_gol, (LARGURA, ALTURA))
        window.blit(fundo_gol,(0, 0))
        pos_mouse = pygame.mouse.get_pos()

        larg = 170
        alt = 106

        x_1 = 340
        y_1 = 170
        canto_1 = pygame.Rect(x_1, y_1, larg, alt)

        x_2 = 690
        y_2 = 170
        canto_2 = pygame.Rect(x_2, y_2, larg, alt)

        x_3 = 340
        y_3 = 382
        canto_3 = pygame.Rect(x_3, y_3, larg, alt)

        x_4 = 690
        y_4 = 382
        canto_4 = pygame.Rect(x_4, y_4, larg, alt)

        x_5 = 510
        y_5 = 276
        larg_5 = 180
        canto_5 = pygame.Rect(x_5, y_5, larg_5, alt)

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
                if canto_5.collidepoint(pos_mouse):
                    pos_bola = "Centro"
                
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
