# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
largura = 1200
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Penalty shoot out')
#imagem = pygame.image.load("imagens\logo.webp")

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 80))  # Preenche com a cor branca
    cor = (255, 255, 255)
    vertices = [(200, 475), (200, 510), (1000, 510), (1000, 475)]
    pygame.draw.polygon(window, cor, vertices, width=3)

    i = 200
    while i < 1000:
        cor = (100, 255, 100)
        vertices = [(203, 478), (203, 507), (997, 507), (997, 478)]
        pygame.draw.polygon(window, cor, vertices)


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
