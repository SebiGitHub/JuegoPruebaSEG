import pygame
import random

# Inicializa todos los módulos de pygame
pygame.init()

# Inicializa el módulo de fuentes
pygame.font.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 633, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# Fuentes
LETRA_ADIVINADA_FUENTE = pygame.font.Font("assets/FreeSansBold.otf", 50)
LETRA_DISPONIBLE_FUENTE = pygame.font.Font("assets/FreeSansBold.otf", 35)

# Palabras posibles
PALABRAS = ["SECRE", "MUNDO", "HOLA", "PYTHON", "JUEGO"]

# Palabra a adivinar (de la lista)
PALABRA_CORRECTA = random.choice(PALABRAS)


ESP_LETRA_X = 85
ESP_LETRA_Y = 12
TAM_LETRA = 75