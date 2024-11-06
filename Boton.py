import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, imagen_sin_seleccionar, imagen_seleccionado, imagen_pulsado):
        # Posición y dimensiones
        self.rect = pygame.Rect(x, y, ancho, alto)

        # Cargar imágenes para cada estado del botón
        self.imagen_sin_seleccionar = pygame.image.load(imagen_sin_seleccionar).convert_alpha()
        self.imagen_seleccionado = pygame.image.load(imagen_seleccionado).convert_alpha()
        self.imagen_pulsado = pygame.image.load(imagen_pulsado).convert_alpha()

        # Estado del botón
        self.seleccionado = False
        self.clickado = False

    def actualizar_estado(self, mouse_pos, mouse_click):
        """Actualiza el estado del botón en función de la posición y clic del mouse"""
        if self.rect.collidepoint(mouse_pos):  # El mouse está sobre el botón
            self.seleccionado = True
            if mouse_click:  # El mouse está presionando el botón
                self.clickado = True
            else:
                self.clickado = False
        else:  # El mouse no está sobre el botón
            self.seleccionado = False
            self.clickado = False

    def dibujar(self, screen):
        """Dibuja el botón según su estado"""
        # Seleccionar la imagen según el estado actual del botón
        if self.clickado:
            imagen = self.imagen_pulsado
        elif self.seleccionado:
            imagen = self.imagen_seleccionado
        else:
            imagen = self.imagen_sin_seleccionar

        # Dibujar la imagen del botón
        screen.blit(imagen, self.rect)

