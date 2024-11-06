class MenuBotones:
    def __init__(self, lista_botones):
        self.lista_botones = lista_botones
        self.seleccionado = 0  # Índice del botón seleccionado inicialmente

    def siguiente(self):
        """Selecciona el siguiente botón en la lista"""
        self.lista_botones[self.seleccionado].seleccionado = False
        self.seleccionado = (self.seleccionado + 1) % len(self.lista_botones)
        self.lista_botones[self.seleccionado].seleccionado = True
        return self.seleccionado

    def anterior(self):
        """Selecciona el botón anterior en la lista"""
        self.lista_botones[self.seleccionado].seleccionado = False
        self.seleccionado = (self.seleccionado - 1) % len(self.lista_botones)
        self.lista_botones[self.seleccionado].seleccionado = True
        return self.seleccionado

    def dibujar(self, screen):
        """Dibuja todos los botones en la lista"""
        for boton in self.lista_botones:
            boton.dibujar(screen)

    def actualizar_botones(self, mouse_pos, mouse_click):
        """Actualiza el estado de todos los botones"""
        for boton in self.lista_botones:
            boton.actualizar_estado(mouse_pos, mouse_click)
