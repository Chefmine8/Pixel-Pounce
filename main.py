import pygame
import sys
from first_level import start_first_level

def logo(screen, y_logo):
    image = pygame.image.load("./img/PIXEL_POUNCE_logo.png")
    scaled_image = pygame.transform.scale(image, (300, 210))
    screen.blit(scaled_image, (460, y_logo))

def title_screen_back(screen):
    image = pygame.image.load("./img/titlescreen.jpg")
    scaled_image = pygame.transform.scale(image, (1220, 720))
    screen.blit(scaled_image, (0, 0))

pygame.init()

y_logo = 50
width = 1220
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Pounce")

clock = pygame.time.Clock()
running = True
logo_speed = 10  # Vitesse de descente de l'image

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            while y_logo < height:
                y_logo += logo_speed
                screen.fill((0, 0, 0))  # Efface l'écran avant de redessiner
                title_screen_back(screen)
                logo(screen, y_logo)
                pygame.display.flip()

    if y_logo >= height:
        start_first_level()
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))  # Efface l'écran avant de redessiner
    title_screen_back(screen)
    logo(screen, y_logo)
    pygame.display.flip()

pygame.quit()