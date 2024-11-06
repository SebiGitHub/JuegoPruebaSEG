import pygame
import sys
from Boton import Boton

# Colores
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_name = "Fuente.ttf"

        # Fuente para el título
        self.myFont = pygame.font.Font(self.font_name, 130)

        # Título
        self.title_text = self.myFont.render("Majotori", True, BLACK)

        # Posición del título
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

        # Crear el botón Start con posición, tamaño y rutas de imagen
        self.start_button = Boton(
            x=WIDTH // 2 - 75,  # Posición x
            y=self.title_rect.bottom + 80,  # Posición y, 80 píxeles debajo del título
            ancho=150,  # Ancho del botón
            alto=50,  # Altura del botón
            imagen_sin_seleccionar="botonStart.png",
            imagen_seleccionado="botonSeleccionado.png",
            imagen_pulsado="botonPulsado.png",
        )

    def mostrar_menu(self):
        """Dibuja el menú principal con título y botón Start"""
        while True:
            self.screen.fill(BEIGE)
            self.screen.blit(self.title_text, (WIDTH // 2 - self.title_text.get_width() // 2, HEIGHT // 3))

            # Determinar y dibujar el estado del botón Start
            self.start_button.dibujar(self.screen)

            # Manejo de eventos
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type == pygame.MOUSEMOTION:
                    # Cambia el estado a seleccionado si el mouse está sobre el botón
                    self.start_button.actualizar_estado(pygame.mouse.get_pos(), False)
                elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    # Cambia el estado a pulsado si el botón es clickeado
                    self.start_button.actualizar_estado(pygame.mouse.get_pos(), True)
                elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                    # Cuando se suelta el botón del mouse
                    self.start_button.actualizar_estado(pygame.mouse.get_pos(), False)
                    if self.start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        print("Clic en Start")

            pygame.display.flip()
