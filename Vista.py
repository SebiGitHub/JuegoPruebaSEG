from tkinter import Text, Button


def __init__(self):
    # Crear los elementos de interfaz
    self.title_text = Text(200, 100, "Bienvenido a Majotori", "Arial")
    self.start_button = Button(300, 300, 200, 50, "Start", "Arial")


def draw(self, screen):
    # Dibujar elementos de la interfaz en la pantalla
    self.title_text.draw(screen)
    self.start_button.draw(screen)


def handle_event(self, event):
    # Maneja eventos y devuelve True si el botón de inicio fue clickeado
    return self.start_button.is_clicked(event)