import pygame
from config import *  # Importa configuraciones externas (como fuentes, colores, tamaños, etc.)

class Letras:
    def __init__(self, text, bg_position):
        # Inicializa los atributos de la clase Letter
        self.bg_color = "white"  # Color de fondo inicial
        self.text_color = "black"  # Color del texto inicial
        self.bg_position = bg_position  # Posición de la letra en la pantalla
        self.bg_x = bg_position[0]  # Coordenada X de la posición del fondo
        self.bg_y = bg_position[1]  # Coordenada Y de la posición del fondo

        # Desplaza los recuadros hacia abajo aumentando bg_y
        self.bg_y += 24  # Desplaza los recuadros hacia abajo 10 píxeles (menos espacio)

        self.bg_rect = (self.bg_x, self.bg_y + 5, TAM_LETRA, TAM_LETRA)  # Rectángulo que define el área de la letra
        self.text = text  # Texto de la letra (carácter que se va a mostrar)

        # Ajusta la posición del texto dentro del rectángulo, también hacia abajo
        self.text_position = (self.bg_x + 36, self.bg_y + 34 + 5)  # Desplaza el texto 5 píxeles hacia abajo
        # Renderiza la letra con la fuente definida en GUESSED_LETTER_FONT
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(
            center=self.text_position)  # Obtiene el rectángulo de la superficie del texto

    def draw(self):
        # Dibuja el fondo de la letra (rectángulo)
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            # Dibuja el borde del rectángulo si el fondo es blanco
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        # Vuelve a renderizar la letra con el color de texto actualizado
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        # Dibuja la letra sobre el fondo
        SCREEN.blit(self.text_surface, self.text_rect)
        # Actualiza la pantalla para mostrar los cambios
        pygame.display.update()

    def delete(self):
        # Elimina visualmente la letra borrándola (pinta el fondo blanco y el borde)
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        # Actualiza la pantalla para reflejar el cambio
        pygame.display.update()
