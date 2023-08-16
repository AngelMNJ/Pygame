import pygame
import sys

pygame.init()

window_size = (1000, 625)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego con movimiento")

# Colores
background_image = pygame.image.load("fondo.png")
background_rect = background_image.get_rect()
enemy_image = pygame.image.load("enemigo.png")
player_image = pygame.image.load("personaje.png")
shot_image = pygame.image.load("balas.png")

# Posicion Jugador
player_rect = player_image.get_rect()
player_rect.centerx = window_size[0] // 2 
player_rect.bottom = window_size[1] - 10 

# Posicion Enemigo
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = window_size[0] // 2 
enemy_rect.top = 5

shots = []

def detect_collisions():
    for shot in shots:
        if shot.colliderect(enemy_image):
            shots.remove(shot)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                shot_rect = shot_image.get_rect()
                shot_rect.centerx = player_rect.centerx
                shot_rect.centery = player_rect.centery - 20
                shots.append(shot_rect)
                
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 3
    if keys[pygame.K_RIGHT]:
        player_rect.x += 3
    if keys[pygame.K_UP]:
        player_rect.y -= 3
    if keys[pygame.K_DOWN]:
        player_rect.y += 3
    for shot in shots:
        shot.y -= 2
        if shot.y < 0:
            shots.remove(shot)

    # Actualizar pantalla
    screen.blit(background_image, background_rect)  # Renderizar la imagen de fondo en la pantalla
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    for shot in shots:
        screen.blit(shot_image, shot)
    pygame.display.flip()
pygame.quit()
sys.exit()
