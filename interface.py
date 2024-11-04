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
imagem_play = pygame.image.load("imagens\imagem_play.png").convert_alpha()
imagem_escrito = pygame.image.load("imagens\escrito.png").convert_alpha()
imagem_play_mouse = pygame.image.load("imagens\play_cor.png").convert_alpha()
imagem_config = pygame.image.load("imagens\Botao config2.png").convert_alpha()
imagem_config_mouse = pygame.image.load("imagens\Botao config cor.png").convert_alpha()
imagem_seta = pygame.image.load("imagens/seta volta.png").convert_alpha()
imagem_seta_mouse = pygame.image.load("imagens/seta volta cor.png").convert_alpha()

#========= Texto


# ----- colocar as outras musicas e como trocar 
lista_musica = ['audios/1.mp3', 'audios/2.mp3', 'audios/3.mp3', 'audios/4.mp3', 'audios/5.mp3']
s = random.randint(0,4)
variavelmusica = 0
pygame.mixer.music.load(lista_musica[s])
pygame.mixer.music.set_volume(0.2)

game = True

barra_carregamento = 0
frames=0
tela_atual='Tela de carregamento'
# === variavel para ajuste de tempo da tela
clock = pygame.time.Clock()
FPS = 60


# ===== Loop principal =====
while game:
    frames+=1
    clock.tick(FPS)
    if tela_atual == 'Tela de carregamento':
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas

        imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 600))
        window.blit(imagem_fundo, (0, 0))

        if frames<=360:
            cor = (0, 0, 0)
            vertices = [(200, 450), (200, 480), (1000, 480), (1000, 450)]

            pygame.draw.polygon(window, cor, vertices, width=3)

            cor = (255, 255, 255)
            vertices = [(201, 451), (201, 479), (999, 479), (999, 451)]
            pygame.draw.polygon(window, cor, vertices)

            cor = (0, 255, 0)
            vertices = [(203, 453), (203, 477), (203 + barra_carregamento, 477), (203 + barra_carregamento, 453)]

            pygame.draw.polygon(window, cor, vertices)
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




        # ======= colocar a imagem do logo do jogo na tela de carregamento


        
        else:
            tela_atual = 'Tela de início'

    
    if tela_atual == 'Tela de início':
        window.blit(imagem_fundo, (0, 0))

        if variavelmusica == 0:
            pygame.mixer.music.play(-1, 2)
            variavelmusica += 1

        cor = (255, 255, 255)
        vertices = [(525, 330), (525, 395), (690, 395), (690, 330)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices, width = 1)

        cor = (255, 255, 255)
        vertices = [(550, 450), (550, 550), (670, 550), (670, 450)]
        retangulo_colisao2 = pygame.draw.polygon(window, cor, vertices, width = 1)

        imagem_escrito = pygame.transform.scale(imagem_escrito, (500, 500))
        imagem_escrito_rect=imagem_escrito.get_rect()
        imagem_escrito_rect.center=((largura/2),(altura/2)-150)
        window.blit(imagem_escrito, (imagem_escrito_rect))

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
                    mouse_pos=event.pos
                    if retangulo_colisao.collidepoint(mouse_pos):
                        tela_atual = "Tela play"
                    if retangulo_colisao2.collidepoint(mouse_pos):
                        tela_atual = "Tela config"
    
    if tela_atual == "Tela config":
        cor = (0, 0, 0)
        vertices = [(20, 15), (20, 45), (55, 45), (55, 15)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices)

        window.blit(imagem_fundo, (0, 0))

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
        cor = (0, 0, 0)
        vertices = [(20, 15), (20, 45), (55, 45), (55, 15)]
        retangulo_colisao = pygame.draw.polygon(window, cor, vertices)

        window.blit(imagem_fundo, (0, 0))

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

        
            



    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
