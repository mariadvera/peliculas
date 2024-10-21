from peliculas import Show

class Cine:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pases = []

    def agregar_pase(self, pase):
        self.pases.append(pase)

    def ver_cartelera(self):
        peliculas_y_horas = {}
        for pase in self.pases:
            if pase.pelicula.titulo not in peliculas_y_horas:
                peliculas_y_horas[pase.pelicula.titulo] = []
            peliculas_y_horas[pase.pelicula.titulo].append(pase.hora)

        for pelicula, horas in peliculas_y_horas.items():
            print(f'Película: {pelicula}, Horas: {", ".join(horas)}')

class Pelicula(Show):
    def __init__(self, titulo):
        super().__init__(titulo, 'film')
        self.pases = []

    def agregar_pase(self, pase):
        self.pases.append(pase)

    def donde_la_veo(self):
        cines_y_horas = {}
        for pase in self.pases:
            if pase.cine.nombre not in cines_y_horas:
                cines_y_horas[pase.cine.nombre] = []
            cines_y_horas[pase.cine.nombre].append(pase.hora)

        for cine, horas in cines_y_horas.items():
            print(f'Cine: {cine}, Horas: {", ".join(horas)}')

class Pase:
    def __init__(self, cine, pelicula, hora):
        if not isinstance(cine, Cine):
            raise TypeError("cine debe ser una instancia de la clase Cine")
        if not isinstance(pelicula, Pelicula):
            raise TypeError("pelicula debe ser una instancia de la clase Pelicula")

        self.cine = cine
        self.pelicula = pelicula
        self.hora = hora

        cine.agregar_pase(self)
        pelicula.agregar_pase(self)
