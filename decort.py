# decort.py

import pygame


def background(screen):
    image = pygame.image.load("./img/background.png")
    scaled_image = pygame.transform.scale(image, (1220, 720))
    screen.blit(scaled_image, (0, 0))
