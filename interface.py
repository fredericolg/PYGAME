# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
largura = 1200
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Penalty shoot out')
imagem_logo = pygame.image.load("imagens\logo_v2.png").convert_alpha()
imagem_goal = pygame.image.load("imagens\GOAL!.png").convert_alpha()


#========= Texto


# ----- Inicia estruturas de dados
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
        window.fill((0, 0, 0))  # Preenche com a cor branca

        if frames<=360:
            cor = (255, 255, 255)
            vertices = [(200, 450), (200, 480), (1000, 480), (1000, 450)]
            pygame.draw.polygon(window, cor, vertices, width=3)

            cor = (0, 255, 0)
            vertices = [(203, 453), (203, 477), (203 + barra_carregamento, 477), (203 + barra_carregamento, 453)]

            pygame.draw.polygon(window, cor, vertices)
            imagem_logo = pygame.transform.scale(imagem_logo, (600, 600))
            imagem_logo_rect=imagem_logo.get_rect()
            imagem_logo_rect.center=((largura/2),(altura/2)-50)
            window.blit(imagem_logo, (imagem_logo_rect))

            if barra_carregamento + 205 <= 997:
                barra_carregamento += 3

            else:
                font = pygame.font.SysFont(None, 48)
                hora_do_gol = font.render('ESTÁ NA HORA DE FAZER GOL!!!', False, (255, 255, 255))
                window.blit(hora_do_gol, (330, 490))




        # ======= colocar a imagem do logo do jogo na tela de carregamento


        
        else:
            tela_atual = 'Tela de início'

    
    if tela_atual == 'Tela de início':
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
