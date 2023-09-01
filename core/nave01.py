import pygame
import random


# Inicialização do pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define as cores
white = (255, 255, 255)
# Cor de fundo
background_color = (0, 0, 0)

# Carrega a imagem da nave
ship_image = pygame.image.load("nave.png")

# Obtém as dimensões da imagem da nave
ship_width = ship_image.get_width()
ship_height = ship_image.get_height()

# Define a posição inicial da nave
ship_x = (screen_width / 2) - (ship_width / 2)
ship_y = screen_height - ship_height

# Define a velocidade da nave
ship_speed = 0.5

# Define a pontuação
score = 0

# Cria uma lista de inimigos
enemies = []

# Carrega a imagem do inimigo
enemy_image = pygame.image.load("enemy_small.png")

# Adiciona 10 inimigos à tela
for i in range(10):
    enemy_x = random.randint(0, screen_width - enemy_image.get_width())
    enemy_y = random.randint(0, 100)
    enemies.append([enemy_x, enemy_y])

# Cria uma lista de tiros
shots = []

# Carrega a imagem do tiro
shot_image = pygame.image.load("shot.png")

########################
# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtém as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Move a nave para a esquerda
    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed

    # Move a nave para a direita
    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed

    # Verifica se a nave colidiu com a borda da tela
    if ship_x < 0:
        ship_x = 0
    elif ship_x > screen_width - ship_width:
        ship_x = screen_width - ship_width

#################
    # Atira com a barra de espaço
    if keys[pygame.K_SPACE]:
        shots.append([ship_x + (ship_width / 2), ship_y])

    # Move os tiros
    for shot in shots:
        shot[1] -= 1

    # Preenche a tela com a cor de fundo
    screen.fill(background_color)

    # Desenha os tiros na tela
    for shot in shots:
        screen.blit(shot_image, (shot[0], shot[1]))

    # Desenha a nave na tela
    screen.blit(ship_image, (ship_x, ship_y))

    # Atualiza a tela
    pygame.display.update()

    ###############################################

    # Move os inimigos
    for enemy in enemies:
        enemy[1] += 0.1

    # Desenha os inimigos na tela
    for enemy in enemies:
        screen.blit(enemy_image, (enemy[0], enemy[1]))

    # Verifica se algum tiro colidiu com algum inimigo
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_image.get_width(), enemy_image.get_height())
        for shot in shots:
            shot_rect = pygame.Rect(shot[0], shot[1], shot_image.get_width(), shot_image.get_height())
            if enemy_rect.colliderect(shot_rect):
                if len(enemies)>0: enemies.remove(enemy)
                shots.remove(shot)
                score += 1

    if len(enemies)==0:       
        enemies = []
        for i in range(10):
            enemy_x = random.randint(0, screen_width - enemy_image.get_width())
            enemy_y = random.randint(0, 100)
            enemies.append([enemy_x, enemy_y])


    # Verifica se a nave colidiu com algum inimigo
    ship_rect = pygame.Rect(ship_x, ship_y, ship_width, ship_height)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_image.get_width(), enemy_image.get_height())
        if ship_rect.colliderect(enemy_rect):
            print("Colisão!")
            break

    # Atualiza a tela
    pygame.display.update()

# Finaliza o pygame
pygame.quit()





    # Verifica se a nave colidiu com algum inimigo
"""     ship_rect = pygame.Rect(ship_x, ship_y, ship_width, ship_height)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_image.get_width(), enemy_image.get_height())
        if ship_rect.colliderect(enemy_rect):
            print("Colisão!")
 """
    #
