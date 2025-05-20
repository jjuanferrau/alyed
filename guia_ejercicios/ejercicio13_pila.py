class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def size(self):
        return len(self.elementos)

pila_trajes = Pila()
pila_trajes.push({'modelo': 'Mark III', 'pelicula': 'Iron Man', 'estado': 'Dañado'})
pila_trajes.push({'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'Destruido'})
pila_trajes.push({'modelo': 'Mark XLII', 'pelicula': 'Iron Man 3', 'estado': 'Destruido'})
pila_trajes.push({'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Dañado'})
pila_trajes.push({'modelo': 'Mark XLVI', 'pelicula': 'Capitan America: Civil War', 'estado': 'Impecable'})
pila_trajes.push({'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Dañado'})
pila_trajes.push({'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Destruido'})

def punto_a(pila):
    pila_aux = Pila()
    peliculas_hulkbuster = []

    while not pila.esta_vacia():
        traje = pila.pop()
        if traje['modelo'] == 'Mark XLIV':
            peliculas_hulkbuster.append(traje['pelicula'])
        pila_aux.push(traje)

    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

    if peliculas_hulkbuster:
        print("\nEl modelo Mark XLIV (Hulkbuster) fue utilizado en las películas:")
        for pelicula in peliculas_hulkbuster:
            print("-", pelicula)
    else:
        print("\nEl modelo Mark XLIV no fue utilizado en ninguna película.")

def punto_b(pila):
    pila_aux = Pila()
    modelos_dañados = []

    while not pila.esta_vacia():
        traje = pila.pop()
        if traje["estado"].lower() == "dañado":
            modelos_dañados.append(traje["modelo"])
        pila_aux.push(traje)

    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

    if modelos_dañados:
        print("\nModelos dañados encontrados:")
        for modelo in set(modelos_dañados):
            print("-", modelo)
    else:
        print("\nNo hay modelos dañados")

def punto_c(pila):
    pila_aux = Pila()
    print("\nModelos destruidos eliminados:")

    while not pila.esta_vacia():
        traje = pila.pop()
        if traje["estado"].lower() == "destruido":
            print("-", traje["modelo"])
        else:
            pila_aux.push(traje)

    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

def punto_d(pila, modelo_nuevo, pelicula_nueva, estado_nuevo):
    existe = False
    pila_aux = Pila()

    while not pila.esta_vacia():
        traje = pila.pop()
        if traje["modelo"] == modelo_nuevo and traje["pelicula"] == pelicula_nueva:
            existe = True
        pila_aux.push(traje)

    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

    if not existe:
        pila.push({
            "modelo": modelo_nuevo,
            "pelicula": pelicula_nueva,
            "estado": estado_nuevo
        })
        print(f"\nSe agregó el modelo {modelo_nuevo} a la película {pelicula_nueva}.")
    else:
        print(f"\nEl modelo {modelo_nuevo} ya estaba cargado para la película {pelicula_nueva}. No se agregó.")

def punto_e(pila):
    pila_aux = Pila()
    trajes_homecoming = []
    trajes_civilwar = []

    while not pila.esta_vacia():
        traje = pila.pop()
        if traje["pelicula"] == "Spider-Man: Homecoming":
            trajes_homecoming.append(traje["modelo"])
        elif traje["pelicula"] == "Capitan America: Civil War":
            trajes_civilwar.append(traje["modelo"])
        pila_aux.push(traje)

    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

    if trajes_homecoming:
        print("\nTrajes utilizados en Spider-Man: Homecoming:")
        for modelo in set(trajes_homecoming):
            print("-", modelo)
    else:
        print("\nNo se encontraron trajes en Spider-Man: Homecoming.")

    if trajes_civilwar:
        print("\nTrajes utilizados en Capitan America: Civil War:")
        for modelo in set(trajes_civilwar):
            print("-", modelo)
    else:
        print("\nNo se encontraron trajes en Capitan America: Civil War.")

punto_a(pila_trajes)

punto_b(pila_trajes)

punto_c(pila_trajes)

punto_d(pila_trajes, "Mark III", "Iron Man 3", "Impecable")
punto_d(pila_trajes, "Mark XLVI", "Capitan America: Civil War", "Dañado")
punto_d(pila_trajes, "Mark XLVI", "Los Vengadores", "Impecable")
punto_d(pila_trajes, "Mark XLVI", "Los Vengadores", "Dañado")

punto_d(pila_trajes, "Mark LXXXV", "Avengers: Endgame", "Destruido")
punto_d(pila_trajes, "Mark LXXXV", "Avengers: Endgame", "Impecable") #no se agrega, ya existe

punto_e(pila_trajes)