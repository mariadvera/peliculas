from datetime import date

class Show:
    """
    Representa los datos necesarios y la forma de utilizarlos  para crear la listas de las  pelícualas , documentales o series vistas.
    
    """

    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo  
        self.terminada = False 
        self.fecha_entrada = date.today()  


    def marcar_como_terminada(self):
        self.terminada = True

  
if __name__ == '__main__' :  
  
    mis_pelis = []

    star_wars = Show('Star Wars', 'película')
    avatar_2 = Show('Avatar 2', 'película')
    wormwood = Show('Wormwood', 'documental')
    the_wire = Show('The Wire', 'serie')


    mis_pelis.append(star_wars)
    mis_pelis.append(avatar_2)
    mis_pelis.append(wormwood)
    mis_pelis.append(the_wire)


    the_wire.marcar_como_terminada()

    for pelicula in mis_pelis:
        print(f'Título: {pelicula.titulo} \t Tipo: {pelicula.tipo} \t Terminada: {pelicula.terminada} \t Fecha de entrada: {pelicula.fecha_entrada}')

   