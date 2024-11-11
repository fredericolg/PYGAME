# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
largura = 1200
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Penalty shoot out')
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
imagem_menu_config = pygame.image.load("imagens/menu config2.png").convert_alpha()
botao_play_music = pygame.image.load("imagens/botao play music.png").convert_alpha()
botao_pause_music = pygame.image.load("imagens/botao pause music.png").convert_alpha()
botao_mute_music = pygame.image.load("imagens/botao mute music.png").convert_alpha()
botao_desmute_music = pygame.image.load("imagens/botao desmute music.png").convert_alpha()
botao_next_music = pygame.image.load("imagens/botao next music.png").convert_alpha()
botao_previous_music = pygame.image.load("imagens/botao previous music.png").convert_alpha()
botao_pix = pygame.image.load("imagens/botao faz o pix.png").convert_alpha()
logo_sp = pygame.image.load("imagens/logo sao paulo.png").convert_alpha()
logo_flu = pygame.image.load("imagens/logo fluminense png.png").convert_alpha()
logo_borussia = pygame.image.load("imagens/logo borussia png.png").convert_alpha()
logo_inter = pygame.image.load("imagens/logo inter miami png.png").convert_alpha()

#========= Texto


game = True
# === tempo de primeira tela (tela de carregamento)
barra_carregamento = 0
frames=0
tela_atual='Tela de carregamento'

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

    "nome1":'audios/1.mp3',
    "nome2":'audios/2.mp3',
    "nome3":'audios/3.mp3',
    "nome4":'audios/4.mp3',
    "nome5":'audios/5.mp3'

}
variavelmusica = random.randint(0,4) 
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

# === variavel para ajuste de tempo da tela
clock = pygame.time.Clock()
FPS = 60


# ===== Loop principal =====
while game:
    frames+=1
    clock.tick(FPS)

    # === TELA DE CARREGAMENTO

    if tela_atual == 'Tela de carregamento':
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas

        imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 600))
        window.blit(imagem_fundo, (0, 0))

        # ==== fica 6 segundos na tela de carregamento
        if frames<=360:
            # cria a barra de carregamento
            cor = (0, 0, 0)
            vertices = [(200, 450), (200, 480), (1000, 480), (1000, 450)]

            pygame.draw.polygon(window, cor, vertices, width=3)

            cor = (255, 255, 255)
            vertices = [(201, 451), (201, 479), (999, 479), (999, 451)]
            pygame.draw.polygon(window, cor, vertices)

            cor = (0, 255, 0)
            vertices = [(203, 453), (203, 477), (203 + barra_carregamento, 477), (203 + barra_carregamento, 453)]

            pygame.draw.polygon(window, cor, vertices)

            # imprime o logo no tela
            imagem_logo = pygame.transform.scale(imagem_logo, (400, 400))
            imagem_logo_rect=imagem_logo.get_rect()
            imagem_logo_rect.center=((largura/2),(altura/2)-50)
            window.blit(imagem_logo, (imagem_logo_rect))

            if barra_carregamento + 205 <= 997:
                barra_carregamento += 3

            else:
                font = pygame.font.SysFont(None, 48)
                hora_do_gol = font.render('ESTÁ NA HORA DE FAZER GOL!!!', False, (0, 0, 0))
                window.blit(hora_do_gol, (330, 490))

        else:
            tela_atual = 'Tela de início'

    
    # TELA DE INÍCIO

    if tela_atual == 'Tela de início':
        window.blit(imagem_fundo, (0, 0))

        # ============== Músicas ================= #
        if not pygame.mixer.music.get_busy():       
            pygame.mixer.music.load(lista_musica[variavelmusica])
            pygame.mixer.music.set_volume(0.2)
            if variavelmusica == 1:
                pygame.mixer.music.play(0, start=11)
                variavelmusica += 1
            if variavelmusica != 1:
                pygame.mixer.music.play(0, start=0.1)
                variavelmusica += 1
            if variavelmusica == 4:
                variavelmusica = 0

        # === Cria retangulo para a placa "PLAY" e "CONFIG" mudarem de cor com o mouse
        cor = (255, 255, 255)
        vertices = [(525, 330), (525, 395), (690, 395), (690, 330)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices, width = 1)

        cor = (255, 255, 255)
        vertices = [(550, 450), (550, 550), (670, 550), (670, 450)]
        retangulo_colisao2 = pygame.draw.polygon(window, cor, vertices, width = 1)

        # coloca o escrito "PENALTY SHOOT OUT" na tela
        imagem_escrito = pygame.transform.scale(imagem_escrito, (500, 500))
        imagem_escrito_rect=imagem_escrito.get_rect()
        imagem_escrito_rect.center=((largura/2),(altura/2)-150)
        window.blit(imagem_escrito, (imagem_escrito_rect))

        # === Muda a cor das placas quando o mouse passa por cima
        mouse_pos = pygame.mouse.get_pos()
        if retangulo_colisao.collidepoint(mouse_pos):
            imagem_play_mouse = pygame.transform.scale(imagem_play_mouse, (345, 485))
            imagem_play_mouse_rect=imagem_play_mouse.get_rect()
            imagem_play_mouse_rect.center=((largura/2)+11,(altura/2 + 80))
            window.blit(imagem_play_mouse, (imagem_play_mouse_rect))
        else:
            imagem_play = pygame.transform.scale(imagem_play, (200, 100))
            imagem_play_rect=imagem_play.get_rect()
            imagem_play_rect.center=((largura/2)+10,(altura/2 + 65))
            window.blit(imagem_play, (imagem_play_rect))

        if retangulo_colisao2.collidepoint(mouse_pos):
            imagem_config_mouse = pygame.transform.scale(imagem_config_mouse, (345, 335))
            imagem_config_mouse_rect=imagem_config_mouse.get_rect()
            imagem_config_mouse_rect.center=((largura/2)+10,(altura/2 + 200))
            window.blit(imagem_config_mouse, (imagem_config_mouse_rect))
        else:
            imagem_config = pygame.transform.scale(imagem_config, (200, 185))
            imagem_config_rect=imagem_config.get_rect()
            imagem_config_rect.center=((largura/2)+10,(altura/2 + 200))
            window.blit(imagem_config, (imagem_config_rect))

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos # ao clicar com o botao esquerdo, muda de tela
                    if retangulo_colisao.collidepoint(mouse_pos):
                        tela_atual = "Tela play"
                    if retangulo_colisao2.collidepoint(mouse_pos):
                        tela_atual = "Tela config"


    # === TELA CONFIGURAÇÃO
    
    if tela_atual == "Tela config":
        cor = (0, 0, 0)
        vertices = [(20, 15), (20, 45), (55, 45), (55, 15)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices)

        imagem_fundo_pix = pygame.transform.scale(imagem_fundo_pix, (largura, altura))
        window.blit(imagem_fundo_pix, (0, 0))

        # === Retangulo do menu
            # Retangulo preto (contorno)
        cor = (0, 0, 0)
        largura_r = (636)
        altura_r = (436)
        tamanho = (largura_r, altura_r)
        posicao = (1/4 * largura - 18, 1/5 * altura - 18)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo laranja
        cor = (255, 100, 0)
        largura_r = (630)
        altura_r = (430)
        tamanho = (largura_r, altura_r)
        posicao = (1/4 * largura - 15, 1/5 * altura - 15)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul marinho
        cor = (60, 72, 92)
        largura_r = (610)
        altura_r = (410)
        tamanho = (largura_r, altura_r)
        posicao = (1/4 * largura - 5, 1/5 * altura - 5)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul claro
        cor = (173, 216, 230)
        largura_r = (600)
        altura_r = (400)
        tamanho = (largura_r, altura_r)
        posicao = (1/4 * largura, 1/5 * altura)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))


        # === Botoes musica
            # botao pause
        botao_pause_music = pygame.transform.scale(botao_pause_music, (50, 50))
        botao_pause_music_rect=botao_pause_music.get_rect()
        botao_pause_music_rect.center = ((largura * 1/2), (altura * 1/2))
        window.blit(botao_pause_music, (botao_pause_music_rect))
            # botao next
        botao_next_music = pygame.transform.scale(botao_next_music, (50, 50))
        botao_next_music_rect=botao_next_music.get_rect()
        botao_next_music_rect.center = ((largura * 1/2) + 65, (altura * 1/2) + 5)
        window.blit(botao_next_music, (botao_next_music_rect))
            # botao previous
        botao_previous_music = pygame.transform.scale(botao_previous_music, (50, 50))
        botao_previous_music_rect=botao_previous_music.get_rect()
        botao_previous_music_rect.center = ((largura * 1/2) - 65, (altura * 1/2) + 5)
        window.blit(botao_previous_music, (botao_previous_music_rect))
        


        for nome, musica in dicio_musica.items():
            if lista_musica[variavelmusica] == musica:
                font = pygame.font.SysFont(None, 46)
                nome_musica = font.render(nome, False, (0, 0, 0))
                window.blit(nome_musica, (550, 250))


        mouse_pos = pygame.mouse.get_pos()
        if retangulo_colisao.collidepoint(mouse_pos):
            imagem_seta_mouse = pygame.transform.scale(imagem_seta_mouse, (65, 65))
            window.blit(imagem_seta_mouse, (0, 0))
        else:
            imagem_seta = pygame.transform.scale(imagem_seta, (65, 65))
            window.blit(imagem_seta, (0, 0))

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_colisao.collidepoint(mouse_pos):
                    tela_atual = "Tela de início"


    if tela_atual == "Tela play":
        
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_colisao.collidepoint(mouse_pos):
                    tela_atual = "Tela de início"
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
        
        cor = (0, 0, 0)
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
        largura_r = 836
        altura_r = 506

        cor = (0, 0, 0)
        largura_r = (largura_r)
        altura_r = (altura_r)
        tamanho = (largura_r, altura_r)
        posicao = (1/6 * largura - 18, 1/7 * altura - 18)
        pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo laranja
        cor = (255, 100, 0)
        largura_r = (largura_r - 6)
        altura_r = (altura_r - 6)
        tamanho = (largura_r, altura_r)
        posicao = (1/6 * largura - 15, 1/7 * altura - 15)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul marinho
        cor = (60, 72, 92)
        largura_r = (largura_r - 20)
        altura_r = (altura_r - 20)
        tamanho = (largura_r, altura_r)
        posicao = (1/6 * largura - 5, 1/7 * altura - 5)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))
            # Retangulo azul claro
        cor = (173, 216, 230)
        largura_r = (largura_r - 10)
        altura_r = (altura_r - 10)
        tamanho = (largura_r, altura_r)
        posicao = (1/6 * largura, 1/7 * altura)
        retangulo_menu = pygame.draw.rect(window, cor, (posicao, tamanho))

        # === Colocar e escolha dos times
        
        time = pygame.transform.scale(lista_times[i], (500, 282))
        time_rect=time.get_rect()
        time_rect.center = ((largura * 1/2), (altura * 1/2))
        window.blit(time, (time_rect))

        # Passar para o próximo time

        cor = (0, 0, 0)
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

        
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
