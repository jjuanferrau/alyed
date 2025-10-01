superheroes_espanol = [
    "Iron Man",
    "Capitán América",
    "Thor",
    "Hulk",
    "Viuda Negra",
    "Spider-Man",
    "Doctor Strange",
    "Wolverine",
    "Storm",
    "Deadpool",
    "Pantera Negra",
    "Capitana Marvel",
    "Ant-Man",
    "Bruja Escarlata",
    "Vision"
]

def buscar_c_a(lista_superheroes: list) -> bool:
    if not lista_superheroes:
        return False
    elif lista_superheroes[0] == "Capitán América":
        print("¡Capitán América ha sido encontrado en la lista!")
        return True
    else:
        return buscar_c_a(lista_superheroes[1:])
