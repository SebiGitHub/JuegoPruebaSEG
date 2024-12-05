import pygame
import sys
import random

from Indicador import Indicator  # Importa la clase Indicator para mostrar letras
from Letras import Letras  # Importa la clase Letter para manejar letras individuales
from Palabras import *  # Importa la lista de palabras

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
pygame.display.set_caption("WordleESP!")  # Título de la ventana
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
ALFABETO = ["QWERTYUIOP", "ASDFGHJKLÑ", "ZXCVBNM"]

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
contador_suposiciones = 0  # Contador de intentos

# Lista de intentos de palabras (6 intentos en total)
guesses = [[]] * 6

current_guess = []  # Palabra que el jugador está adivinando actualmente
current_guess_string = ""  # Cadena actual de letras
current_letter_bg_x = 110  # Posición inicial de la primera letra

# Lista de indicadores (botones del teclado virtual)
indicadores = []
resultado_juego = ""  # Resultado del juego: "W" para ganar, "L" para perder, vacío si sigue jugando

# Dibuja los indicadores (teclado virtual)
indicador_x, indicador_y = 20, 600

# Dibuja cada fila del teclado virtual
for i in range(3):
    for letra in ALFABETO[i]:
        nuevo_indicador = Indicator(indicador_x, indicador_y, letra)
        indicadores.append(nuevo_indicador)  # Agrega el indicador a la lista
        nuevo_indicador.draw()  # Dibuja el indicador en pantalla
        indicador_x += 60  # Espaciado horizontal entre letras
    indicador_y += 100  # Espaciado vertical entre filas
    if i == 0:
        indicador_x = 20
    elif i == 1:
        indicador_x = 105


def comprobar_suposicion(guess_to_check):
    # Verifica cada letra de la suposición actual y la compara con la palabra correcta.
    global current_guess, current_guess_string, contador_suposiciones, current_letter_bg_x, resultado_juego
    estado_juego = False  # Variable para evitar múltiples cambios en el estado del juego.

    for a in range(5):  # Itera sobre cada letra de la suposición (asumiendo palabras de 5 letras).
        letra_minuscula = guess_to_check[a].text.lower()  # Convierte la letra a minúscula.

        # Verifica si la letra está en la palabra correcta.
        if letra_minuscula in PALABRA_CORRECTA:
            if letra_minuscula == PALABRA_CORRECTA[a]:  # La letra está en la posición correcta.
                guess_to_check[a].bg_color = VERDE  # Cambia el color de fondo a verde.

                # Actualiza el indicador del teclado visual.
                for indicador in indicadores:
                    if indicador.text == letra_minuscula.upper():
                        indicador.bg_color = VERDE
                        indicador.draw()
                guess_to_check[a].text_color = "white"
                if not estado_juego:
                    resultado_juego = "W"  # Marca el juego como ganado si todas las letras son correctas.
            else:
                guess_to_check[a].bg_color = AMARILLO  # La letra está en la palabra, pero en una posición incorrecta.
                for indicador in indicadores:
                    if indicador.text == letra_minuscula.upper():
                        indicador.bg_color = AMARILLO
                        indicador.draw()
                guess_to_check[a].text_color = "white"
                resultado_juego = ""
                estado_juego = True  # Evita cambiar el estado varias veces.
        else:
            # La letra no está en la palabra.
            guess_to_check[a].bg_color = GRIS  # Cambia el color de fondo a gris.
            for indicador in indicadores:
                if indicador.text == letra_minuscula.upper():
                    indicador.bg_color = GRIS
                    indicador.draw()
            guess_to_check[a].text_color = "white"
            resultado_juego = ""
            estado_juego = True

        # Dibuja la letra con su color actualizado.
        guess_to_check[a].draw()
        pygame.display.update()  # Actualiza la pantalla.

    contador_suposiciones += 1  # Incrementa el contador de suposiciones.
    current_guess = []  # Reinicia la lista de la suposición actual.
    current_guess_string = ""  # Limpia la cadena de la suposición actual.
    current_letter_bg_x = 110  # Restablece la posición de la siguiente letra.

    # Si se alcanzan 6 intentos y no se ha ganado, se marca como pérdida.
    if contador_suposiciones == 6 and resultado_juego == "":
        resultado_juego = "L"


def jugar_otravez():
    # Muestra un mensaje para reiniciar el juego después de ganar o perder.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))  # Borra la parte de abajo de la pantalla.
    jugar_otravez_fuente = pygame.font.Font("assets/FreeSansBold.otf", 35)

    # Muestra el mensaje de reinicio.
    if resultado_juego == "W":
        # Renderiza el primer texto ("VICTORIA") en una línea
        texto_resultado = jugar_otravez_fuente.render("¡VICTORIA!", True, "green")
    else:
        # Renderiza el primer texto ("DERROTA") en una línea
        texto_resultado = jugar_otravez_fuente.render("¡DERROTA!", True, "red")

    texto_resultado_rect = texto_resultado.get_rect(center=(ANCHO / 2, 650))

    # Volver a jugar
    jugar_otravez_texto = jugar_otravez_fuente.render("Presiona ENTER para Volver a jugar!", True, "black")
    jugar_otravez_rect = jugar_otravez_texto.get_rect(center=(ANCHO / 2, 750))

    # Muestra la palabra correcta.
    palabra_correcta_texto = jugar_otravez_fuente.render(f"La palabra era: {PALABRA_CORRECTA}!", True, "black")
    palabra_correcta_rect = palabra_correcta_texto.get_rect(center=(ANCHO / 2, 700))

    # Dibuja los textos en pantalla.
    SCREEN.blit(texto_resultado, texto_resultado_rect)
    SCREEN.blit(palabra_correcta_texto, palabra_correcta_rect)
    SCREEN.blit(jugar_otravez_texto, jugar_otravez_rect)
    pygame.display.update()


def reset():
    # Reinicia el juego a su estado inicial.
    global contador_suposiciones, PALABRA_CORRECTA, guesses, current_guess, current_guess_string, resultado_juego
    SCREEN.fill("white")  # Limpia la pantalla.
    SCREEN.blit(FONDO, FONDO_RECT)  # Redibuja el fondo.
    contador_suposiciones = 0  # Restablece el contador de intentos.
    PALABRA_CORRECTA = random.choice(PALABRAS)  # Selecciona una nueva palabra.
    guesses = [[]] * 6  # Reinicia las suposiciones.
    current_guess = []  # Limpia la suposición actual.
    current_guess_string = ""  # Limpia la cadena de suposición actual.
    resultado_juego = ""  # Reinicia el resultado del juego.
    pygame.display.update()  # Actualiza la pantalla.

    # Reinicia los colores de los indicadores.
    for indicador in indicadores:
        indicador.bg_color = OUTLINE
        indicador.draw()


def create_new_letter():
    global current_guess_string, current_letter_bg_x, contador_suposiciones  # Variables globales usadas para rastrear el estado actual.

    current_guess_string += tecla_presionada  # Agrega la letra presionada a la cadena actual.

    # Crea una instancia de la clase Letter, ubicándola en la posición correcta de la pantalla.
    nueva_letra = Letras(tecla_presionada, (current_letter_bg_x, contador_suposiciones * 90 + LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING  # Desplaza la posición horizontal para la siguiente letra.


    # Verifica si el índice guesses_count está fuera del rango de la lista 'guesses'.
    if contador_suposiciones >= len(guesses):
        guesses.append([])  # Si no existe, añade una nueva sublista vacía.

    # Agrega la nueva letra a la suposición actual.
    guesses[contador_suposiciones].append(nueva_letra)
    current_guess.append(nueva_letra)

    # Redibuja todas las letras de la suposición actual en pantalla.
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    # Elimina la última letra de la suposición actual.
    global current_guess_string, current_letter_bg_x  # Variables globales para rastrear la suposición y la posición de las letras.

    guesses[contador_suposiciones][-1].delete()  # Borra visualmente la última letra de la pantalla.
    guesses[contador_suposiciones].pop()  # Elimina la última letra de la lista de letras.

    # Elimina la última letra de la cadena de suposición actual.
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()  # Elimina la letra de la lista actual.

    current_letter_bg_x -= LETTER_X_SPACING  # Ajusta la posición para la próxima letra.


while True:  # Bucle infinito para mantener el juego en ejecución.
    if resultado_juego != "":  # Si el juego ha terminado (ganado o perdido).
        jugar_otravez()  # Muestra la pantalla de reinicio.

    # Captura los eventos de Pygame, como pulsaciones de teclas o cierre de ventana.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si se cierra la ventana.
            pygame.quit()  # Cierra Pygame.
            sys.exit()  # Sale del programa.

        if event.type == pygame.KEYDOWN:  # Evento de presionar una tecla.
            # Solo permite que la tecla Enter funcione cuando el juego ha terminado (modo jugar_otravez)
            if resultado_juego != "":
                if event.key == pygame.K_RETURN:  # Si se presiona "Enter".
                    reset()  # Reinicia el juego si ya terminó.
            else:
                # Si no estamos en el modo "jugar_otravez", las teclas funcionan normalmente
                if event.key == pygame.K_RETURN:  # Si se presiona "Enter".
                    if len(current_guess_string) == 5 and current_guess_string.lower() in PALABRAS:
                        comprobar_suposicion(current_guess)  # Verifica la suposición actual.

                elif event.key == pygame.K_BACKSPACE:  # Si se presiona "Backspace".
                    if len(current_guess_string) > 0:  # Verifica que haya letras para borrar.
                        delete_letter()  # Borra la última letra ingresada.

                else:  # Para cualquier otra tecla presionada.
                    tecla_presionada = event.unicode.upper()  # Convierte la tecla en mayúscula.
                    # Verifica si la tecla es una letra válida.
                    if tecla_presionada in "QWERTYUIOPASDFGHJKLÑZXCVBNM" and tecla_presionada != "":
                        if len(current_guess_string) < 5:  # Solo permite hasta 5 letras.
                            create_new_letter()  # Crea y agrega una nueva letra a la suposición.

