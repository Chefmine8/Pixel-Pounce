import pygame
from perso import perso
from decort import obstacle

def start_first_level():
    pygame.init()

    width = 1220
    height = 720

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pixel Pounce")


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))  # Fond blanc pour la première fenêtre du niveau
        obstacle(screen, self)
        perso(screen, obstacle, self)
        pygame.display.flip()

    pygame.quit()
