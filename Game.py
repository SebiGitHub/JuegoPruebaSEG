import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Majotori")

# Colores y fuentes
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font_name = "Fuente.ttf"
font = pygame.font.Font(font_name, 70)
