import pygame
from config import *  # Importa configuraciones externas (como fuentes, colores, tamaños, etc.)

class Indicator:
    def __init__(self, x, y, letter):
        # Inicializa los atributos de la clase Indicator
        self.x = x  # Posición X del indicador
        self.y = y  # Posición Y del indicador
        self.text = letter  # Letra que se va a mostrar en el indicador
        self.rect = (self.x, self.y, 57, 75)  # Rectángulo que define el área del indicador (tamaño fijo)
        self.bg_color = OUTLINE  # Color de fondo del indicador (definido por OUTLINE)

    def draw(self):
        # Dibuja el rectángulo de fondo del indicador con el color de fondo especificado
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        # Renderiza la letra con la fuente definida en AVAILABLE_LETTER_FONT y color blanco
        self.text_surface = LETRA_DISPONIBLE_FUENTE.render(self.text, True, "white")
        # Obtiene el rectángulo de la superficie del texto y lo centra en el área del indicador
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        # Dibuja el texto sobre el fondo del rectángulo
        SCREEN.blit(self.text_surface, self.text_rect)
        # Actualiza la pantalla para mostrar el indicador con la letra
        pygame.display.update()
