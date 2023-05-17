# perso.py

import pygame


def perso(screen, x, y, face):
    image = pygame.image.load(face)
    scaled_image = pygame.transform.scale(image, (72, 105))
    screen.blit(scaled_image, (x, y))
