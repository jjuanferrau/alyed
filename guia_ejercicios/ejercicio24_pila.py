class PilaMCU:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def inspeccionar(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamano(self):
        return len(self.items)

def encontrar_posicion(pila, nombre_personaje):
    temp_pila = PilaMCU()
    posicion = 0
    encontrado = False

    while not pila.esta_vacia():
        posicion += 1
        elemento = pila.desapilar()
        temp_pila.apilar(elemento)  # mover elementos a una pila temporal
        if elemento["nombre"] == nombre_personaje:
            encontrado = True
            break

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    if encontrado:
        return posicion
    else:
        return None

def punto_b(pila):
    temp_pila = PilaMCU()
    print("\nPersonajes que participaron en más de 5 películas:")
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["cantidad_peliculas"] > 5:
            print(f"- {personaje['nombre']}: {personaje['cantidad_peliculas']} películas")
        temp_pila.apilar(personaje)

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

def punto_c(pila):
    temp_pila = PilaMCU()
    cantidad = 0
    encontrado = False
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"] == "Viuda Negra":
            cantidad = personaje["cantidad_peliculas"]
            encontrado = True
        temp_pila.apilar(personaje)

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    if encontrado:
        print(f"\nViuda Negra participó en {cantidad} películas.")
    else:
        print("\nNo se encontró información sobre la Viuda Negra en la pila.")

def punto_d(pila):
    temp_pila = PilaMCU()
    print("\nPersonajes cuyos nombres empiezan con C, D o G:")
    letras_interes = ['C', 'D', 'G']
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"][0] in letras_interes:
            print(f"- {personaje['nombre']}")
        temp_pila.apilar(personaje)

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

pila_mcu = PilaMCU()

pila_mcu.apilar({"nombre": "Iron Man", "cantidad_peliculas": 10})
pila_mcu.apilar({"nombre": "Capitán América", "cantidad_peliculas": 7})
pila_mcu.apilar({"nombre": "Thor", "cantidad_peliculas": 8})
pila_mcu.apilar({"nombre": "Viuda Negra", "cantidad_peliculas": 8})
pila_mcu.apilar({"nombre": "Hulk", "cantidad_peliculas": 6})
pila_mcu.apilar({"nombre": "Rocket Raccoon", "cantidad_peliculas": 4})
pila_mcu.apilar({"nombre": "Groot", "cantidad_peliculas": 4})
pila_mcu.apilar({"nombre": "Doctor Strange", "cantidad_peliculas": 4})
pila_mcu.apilar({"nombre": "Gamora", "cantidad_peliculas": 3})
pila_mcu.apilar({"nombre": "Daredevil", "cantidad_peliculas": 0})
pila_mcu.apilar({"nombre": "Carnage", "cantidad_peliculas": 1})

# encontrar a Rocket Raccoon
posicion_rocket = encontrar_posicion(pila_mcu, "Rocket Raccoon")
if posicion_rocket:
    print(f"Rocket Raccoon se encuentra en la posición: {posicion_rocket}")
else:
    print("Rocket Raccoon no se encontró en la pila.")

# encontrar a Groot
posicion_groot = encontrar_posicion(pila_mcu, "Groot")
if posicion_groot:
    print(f"Groot se encuentra en la posición: {posicion_groot}")
else:
    print("Groot no se encontró en la pila.")

# ver personajes que participaron en mas de 5 peliculas
punto_b(pila_mcu)

# ver participacion de viuda negra en peliculas
punto_c(pila_mcu)

# ver personajes cdg
punto_d(pila_mcu)

# mostrar pila al finalizar
print("\nEstado final de la pila:")
temp_pila_final = PilaMCU()
while not pila_mcu.esta_vacia():
    elemento = pila_mcu.desapilar()
    print(elemento["nombre"])
    temp_pila_final.apilar(elemento)
while not temp_pila_final.esta_vacia():
    pila_mcu.apilar(temp_pila_final.desapilar())
