import pygame

def perso(screen, obstacle, self):
    self.personnage = pygame.draw.circle(screen, (0, 255, 0), [300, 300], 20, 0)

    print(self.personnage.colliderect(self.obstacle))
