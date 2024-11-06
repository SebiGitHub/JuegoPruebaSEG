import pygame
import sys
import random
from Palabras import *

pygame.init()


# Constantes
ANCHO, ALTO = 633, 900

SCREEN = pygame.display.set_mode((ANCHO, ALTO))
FONDO = pygame.image.load("Starting Tiles.png")
BACKGROUND_RECT = FONDO.get_rect(center=(317, 300))
ICON = pygame.image.load("Icon.png")

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

#Palabra con la que jugar
CORRECT_WORD = "focal"

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75