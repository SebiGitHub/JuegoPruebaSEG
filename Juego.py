import pygame
import sys
import random

from Indicador import Indicator  # Importa la clase Indicator para mostrar letras
from Letras import Letras  # Importa la clase Letter para manejar letras individuales
from Palabras import *  # Importa la lista de palabras o cualquier otra funcionalidad de Palabras

pygame.init()  # Inicializa todas las funciones de pygame


# Definición de la clase principal del juego
class Juego:
    def run(self):
        # Metodo principal para ejecutar el bucle del juego
        running = True
        while running:
            for event in pygame.event.get():  # Captura los eventos de la ventana
                if event.type == pygame.QUIT:  # Si se cierra la ventana, termina el juego
                    running = False
            self.SCREEN.fill((255, 255, 255))  # Rellena la pantalla con color blanco
            pygame.display.update()  # Actualiza la pantalla para mostrar cambios

        pygame.quit()  # Cierra pygame cuando se termina el bucle


# Constantes de configuración
ANCHO, ALTURA = 633, 880

# Configuración de la pantalla
SCREEN = pygame.display.set_mode((ANCHO, ALTURA), pygame.RESIZABLE)
FONDO = pygame.image.load("assets/Starting Tiles.png")  # Carga la imagen de fondo
FONDO =  pygame.transform.scale(FONDO, (422, 520))
FONDO_RECT = FONDO.get_rect(center=(318, 300))  # Posición del fondo
ICON = pygame.image.load("assets/Icon.png")  # Carga el ícono del juego

# Configuración del sonido
pygame.mixer.music.load("assets/musica_defondo.mp3")  # Carga la música de fondo
pygame.mixer.music.play(-1)  # Reproduce la música en bucle infinito
pygame.mixer.music.set_volume(0.9)  # Ajusta el volumen de la música

# Configuración de la ventana del juego
pygame.display.set_caption("Wordle!")  # Título de la ventana
pygame.display.set_icon(ICON)  # Configura el ícono de la ventana

# Colores usados en el juego
VERDE = "#6aaa64"
AMARILLO = "#c9b458"
GRIS = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# Selección de la palabra correcta para adivinar
PALABRA_CORRECTA = random.choice(PALABRAS)

# Configuración del teclado virtual
ALFABETO = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

# Configuración de fuentes
LETRA_ACIERTO_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
LETRA_DISPONIBLE_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

# Dibuja el fondo inicial
SCREEN.fill("white")
SCREEN.blit(FONDO, FONDO_RECT)
pygame.display.update()

# Espaciado y tamaño de las letras
LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

# Variables globales
guesses_count = 0  # Contador de intentos

# Lista de intentos de palabras (6 intentos en total)
guesses = [[]] * 6

current_guess = []  # Palabra que el jugador está adivinando actualmente
current_guess_string = ""  # Cadena actual de letras
current_letter_bg_x = 110  # Posición inicial de la primera letra

# Lista de indicadores (botones del teclado virtual)
indicators = []
game_result = ""  # Resultado del juego: "W" para ganar, "L" para perder, vacío si sigue jugando

# Dibuja los indicadores (teclado virtual)
indicator_x, indicator_y = 20, 600

# Dibuja cada fila del teclado virtual
for i in range(3):
    for letter in ALFABETO[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)  # Agrega el indicador a la lista
        new_indicator.draw()  # Dibuja el indicador en pantalla
        indicator_x += 60  # Espaciado horizontal entre letras
    indicator_y += 100  # Espaciado vertical entre filas
    if i == 0:
        indicator_x = 50
    elif i == 1:
        indicator_x = 105


def check_guess(guess_to_check):
    # Verifica cada letra de la suposición actual y la compara con la palabra correcta.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False  # Variable para evitar múltiples cambios en el estado del juego.

    for i in range(5):  # Itera sobre cada letra de la suposición (asumiendo palabras de 5 letras).
        lowercase_letter = guess_to_check[i].text.lower()  # Convierte la letra a minúscula.

        # Verifica si la letra está en la palabra correcta.
        if lowercase_letter in PALABRA_CORRECTA:
            if lowercase_letter == PALABRA_CORRECTA[i]:  # La letra está en la posición correcta.
                guess_to_check[i].bg_color = VERDE  # Cambia el color de fondo a verde.
                # Actualiza el indicador del teclado visual.
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = VERDE
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"  # Marca el juego como ganado si todas las letras son correctas.
            else:
                guess_to_check[i].bg_color = AMARILLO  # La letra está en la palabra, pero en una posición incorrecta.
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = AMARILLO
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True  # Evita cambiar el estado varias veces.
        else:
            # La letra no está en la palabra.
            guess_to_check[i].bg_color = GRIS  # Cambia el color de fondo a gris.
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GRIS
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True

        # Dibuja la letra con su color actualizado.
        guess_to_check[i].draw()
        pygame.display.update()  # Actualiza la pantalla.

    guesses_count += 1  # Incrementa el contador de suposiciones.
    current_guess = []  # Reinicia la lista de la suposición actual.
    current_guess_string = ""  # Limpia la cadena de la suposición actual.
    current_letter_bg_x = 110  # Restablece la posición de la siguiente letra.

    # Si se alcanzan 6 intentos y no se ha ganado, se marca como pérdida.
    if guesses_count == 6 and game_result == "":
        game_result = "L"


def play_again():
    # Muestra un mensaje para reiniciar el juego después de ganar o perder.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))  # Borra la parte de abajo de la pantalla.
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 35)

    # Muestra el mensaje de reinicio.
    if (game_result == "w"):
        # Renderiza el primer texto ("VICTORIA") en una línea
        resultado_text = play_again_font.render("¡VICTORIA!", True, "green")
    else:
        # Renderiza el primer texto ("DERROTA") en una línea
        resultado_text = play_again_font.render("¡DERROTA!", True, "red")

    resultado_text_rect = resultado_text.get_rect(center=(ANCHO / 2, 650))

    # Volver a jugar
    play_again_text = play_again_font.render("Presiona ENTER para Volver a jugar!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(ANCHO / 2, 750))

    # Muestra la palabra correcta.
    word_was_text = play_again_font.render(f"La palabra era: {PALABRA_CORRECTA}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(ANCHO / 2, 700))

    # Dibuja los textos en pantalla.
    SCREEN.blit(resultado_text, resultado_text_rect)
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()


def reset():
    # Reinicia el juego a su estado inicial.
    global guesses_count, PALABRA_CORRECTA, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill("white")  # Limpia la pantalla.
    SCREEN.blit(FONDO, FONDO_RECT)  # Redibuja el fondo.
    guesses_count = 0  # Restablece el contador de intentos.
    PALABRA_CORRECTA = random.choice(PALABRAS)  # Selecciona una nueva palabra.
    guesses = [[]] * 6  # Reinicia las suposiciones.
    current_guess = []  # Limpia la suposición actual.
    current_guess_string = ""  # Limpia la cadena de suposición actual.
    game_result = ""  # Reinicia el resultado del juego.
    pygame.display.update()  # Actualiza la pantalla.

    # Reinicia los colores de los indicadores.
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


def create_new_letter():
    global current_guess_string, current_letter_bg_x, guesses_count  # Variables globales usadas para rastrear el estado actual.

    current_guess_string += key_pressed  # Agrega la letra presionada a la cadena actual.

    # Crea una instancia de la clase Letter, ubicándola en la posición correcta de la pantalla.
    new_letter = Letras(key_pressed, (current_letter_bg_x, guesses_count * 90 + LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING  # Desplaza la posición horizontal para la siguiente letra.


    # Verifica si el índice guesses_count está fuera del rango de la lista 'guesses'.
    if guesses_count >= len(guesses):
        guesses.append([])  # Si no existe, añade una nueva sublista vacía.

    # Agrega la nueva letra a la suposición actual.
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)

    # Redibuja todas las letras de la suposición actual en pantalla.
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    # Elimina la última letra de la suposición actual.
    global current_guess_string, current_letter_bg_x  # Variables globales para rastrear la suposición y la posición de las letras.

    guesses[guesses_count][-1].delete()  # Borra visualmente la última letra de la pantalla.
    guesses[guesses_count].pop()  # Elimina la última letra de la lista de letras.

    # Elimina la última letra de la cadena de suposición actual.
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()  # Elimina la letra de la lista actual.

    current_letter_bg_x -= LETTER_X_SPACING  # Ajusta la posición para la próxima letra.


while True:  # Bucle infinito para mantener el juego en ejecución.
    if game_result != "":  # Si el juego ha terminado (ganado o perdido).
        play_again()  # Muestra la pantalla de reinicio.

    # Captura los eventos de Pygame, como pulsaciones de teclas o cierre de ventana.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si se cierra la ventana.
            pygame.quit()  # Cierra Pygame.
            sys.exit()  # Sale del programa.

        if event.type == pygame.KEYDOWN:  # Evento de presionar una tecla.
            # Solo permite que la tecla Enter funcione cuando el juego ha terminado (modo play_again)
            if game_result != "":
                if event.key == pygame.K_RETURN:  # Si se presiona "Enter".
                    reset()  # Reinicia el juego si ya terminó.
            else:
                # Si no estamos en el modo "play_again", las teclas funcionan normalmente
                if event.key == pygame.K_RETURN:  # Si se presiona "Enter".
                    if len(current_guess_string) == 5 and current_guess_string.lower() in PALABRAS:
                        check_guess(current_guess)  # Verifica la suposición actual.

                elif event.key == pygame.K_BACKSPACE:  # Si se presiona "Backspace".
                    if len(current_guess_string) > 0:  # Verifica que haya letras para borrar.
                        delete_letter()  # Borra la última letra ingresada.

                else:  # Para cualquier otra tecla presionada.
                    key_pressed = event.unicode.upper()  # Convierte la tecla en mayúscula.
                    # Verifica si la tecla es una letra válida.
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        if len(current_guess_string) < 5:  # Solo permite hasta 5 letras.
                            create_new_letter()  # Crea y agrega una nueva letra a la suposición.

