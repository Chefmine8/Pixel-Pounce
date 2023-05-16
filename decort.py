import pygame

def obstacle(screen, self):
    self.obstacle = pygame.draw.rect(screen, (0, 0, 255), [0, 700, 1220, 20], 0)