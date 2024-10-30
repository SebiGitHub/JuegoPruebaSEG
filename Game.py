import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Majotori")

# Colores y fuentes
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)
font_name = "Fuente.ttf"
font = pygame.font.Font(font_name, 70)

# Estados del juego
class GameState:
    MENU = 1
    TRIVIA = 2
    NARRATIVE = 3

# Clase principal del juego
class Game:
    def __init__(self):
        self.state = GameState.MENU

    def run(self):
        """Bucle principal del juego"""
        while True:
            screen.fill(BEIGE)
            if self.state == GameState.MENU:
                self.show_menu()
            elif self.state == GameState.TRIVIA:
                self.show_trivia()
            elif self.state == GameState.NARRATIVE:
                self.show_narrative()
            pygame.display.flip()
            self.handle_events()

    def show_menu(self):
        """Dibuja el menú principal"""
        title_text = font.render("Bienvenido a Majotori", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))

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


