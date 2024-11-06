from tkinter import Button

from Menu import *
from Game import *

import sys
import GameState


# Clase principal del juego
class Vista:
    def __init__(self):
        self.state = GameState.MENU

    def run(self):
        """Bucle principal del juego"""
        while True:
            screen.fill(BEIGE)
            if self.state == GameState.MENU:
                menu = Menu(screen)
                menu.mostrar_menu()
            elif self.state == GameState.TRIVIA:
                self.show_trivia()
            elif self.state == GameState.NARRATIVE:
                self.show_narrative()
            pygame.display.flip()
            self.handle_events()

    def show_trivia(self):
        """Dibuja la pantalla de preguntas"""
        trivia_text = font.render("Aquí irán las preguntas", True, BLACK)
        screen.blit(trivia_text, (WIDTH // 2 - trivia_text.get_width() // 2, HEIGHT // 2 - 50))

    def show_narrative(self):
        """Dibuja la pantalla narrativa"""
        narrative_text = font.render("Aquí irá la narrativa", True, BLACK)
        screen.blit(narrative_text, (WIDTH // 2 - narrative_text.get_width() // 2, HEIGHT // 2 - 50))

    def handle_events(self):
        """Maneja eventos de usuario"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Cambiar de estado con la barra espaciadora como ejemplo
                    self.state = GameState.TRIVIA if self.state == GameState.MENU else GameState.NARRATIVE

    def draw(self, screen):
        # Dibujar elementos de la interfaz en la pantalla
        self.title_text.draw(screen)
        self.start_button.draw(screen)