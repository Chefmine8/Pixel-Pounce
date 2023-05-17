# first_level.py

import pygame
from perso import perso
from decort import background
from decort import sol


def check_collision(perso_x, perso_y):
    # Position de l'objet collision
    collision_x = 0
    collision_y = 720 - 65

    perso_rect = pygame.Rect(perso_x, perso_y, 72, 105)
    collision_rect = pygame.Rect(collision_x, collision_y, 1220, 65)
    return perso_rect.colliderect(collision_rect)


def start_first_level():
    pygame.init()
    face = "./img/perso/walk/Char_1.png"
    width = 1220
    height = 720

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pixel Pounce")

    perso_y = 550  # Position verticale du personnage
    perso_x = 10
    falling = True  # Indicateur de descente
    speed = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if jumpe == False:
                face = "./img/perso/walk/Char_1.png"
            perso_x += speed
        if keys[pygame.K_LEFT]:
            if jumpe == False:
                face = "./img/perso/walk/Char_2.png"
            perso_x -= speed

        if keys[pygame.K_UP]:
            falling = True
            jumpe = True
            face = "./img/perso/Jump/Char_3.png"
            perso_y -= 20
            pygame.time.wait(10)
            face = "./img/perso/Jump/Char_4.png"
            perso_y -= 20

        screen.fill((255, 255, 255))  # Fond blanc pour la première fenêtre du niveau
        background(screen)
        sol(screen)

        if check_collision(perso_x, perso_y):
            falling = False # Arrêt de la descente du personnage
            jumpe = False


        perso(screen, perso_x, perso_y, face)  # Affichage du personnage à sa position actuelle

        if falling:  # Déplacement vertical du personnage si la descente continue
            perso_y += 5

        pygame.display.flip()

    pygame.quit()
