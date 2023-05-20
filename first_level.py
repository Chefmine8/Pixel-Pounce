# first_level.py

import pygame
from perso import perso
from decort import background

def sol(screen, sol_y):
    image = pygame.image.load("./img/Platform_test_layer_1.png")
    scaled_image = pygame.transform.scale(image, (1220, 61))
    screen.blit(scaled_image, (0, sol_y))
def check_collision(perso_x, perso_y, sol_y):
    if perso_x < 200 and perso_x > 100:
        return False

    # Position de l'objet collision
    perso_rect = pygame.Rect(perso_x, perso_y, 72, 105)
    collision_rect = pygame.Rect(perso_x, sol_y, 1220, 65)
    return perso_rect.colliderect(collision_rect)


def start_first_level():
    pygame.init()
    face = "./img/perso/walk/Char_1.png"
    width = 1220
    height = 720
    sol_y = height - 65
    jumpe = True

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

        if perso_y >= 720:
            running = False
        falling = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if jumpe == False:
                face = "./img/perso/walk/Char_1.png"
            else:
                face = "./img/perso/Jump/Char_4.png"
            perso_x += speed
        if keys[pygame.K_LEFT]:
            if jumpe == False:
                face = "./img/perso/walk/Char_2.png"
            else:
                face = "./img/perso/Jump/Char_2.png"
            perso_x -= speed

        if jumpe != True:
            if keys[pygame.K_UP]:
                falling = True
                jumpe = True
                face = "./img/perso/Jump/Char_3.png"
                perso_y -= 50
                pygame.time.wait(50)
                face = "./img/perso/Jump/Char_4.png"
                perso_y -= 50

        screen.fill((255, 255, 255))  # Fond blanc pour la première fenêtre du niveau
        background(screen)
        sol(screen, sol_y)

        if check_collision(perso_x, perso_y, sol_y):
            falling = False # Arrêt de la descente du personnage
            jumpe = False


        perso(screen, perso_x, perso_y, face)  # Affichage du personnage à sa position actuelle

        if falling:  # Déplacement vertical du personnage si la descente continue
            if jumpe == False:
                perso_y += 20
            else:
                perso_y += 3

        pygame.display.flip()

    pygame.quit()
