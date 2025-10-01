from class_list import List 
from typing import Any, Optional

# --- 1. Definición de la Clase Jedi ---

class Jedi:
    """Clase para representar a un Jedi."""
    def __init__(self, nombre: str, maestros: list, sables: list, especie: str):
        self.nombre = nombre
        self.maestros = maestros  # Lista de nombres de maestros
        self.sables = sables      # Lista de colores de sable de luz
        self.especie = especie

    def __str__(self):
        """Representación legible del objeto."""
        maestros_str = ", ".join(self.maestros)
        sables_str = ", ".join(self.sables)
        return (f"Nombre: {self.nombre} | Especie: {self.especie} | "
                f"Maestros: [{maestros_str}] | Sables: [{sables_str}]")


# --- 2. Funciones Criterio para la clase List ---

# Necesarias para que los métodos sort_by_criterion y search funcionen con objetos
def criterio_nombre(jedi: Jedi) -> str:
    return jedi.nombre

def criterio_especie(jedi: Jedi) -> str:
    return jedi.especie


# --- 3. Inicialización de la Lista ---

jedi_list = List([
    Jedi("Yoda", ["Maestro Gark"], ["verde"], "desconocida"),
    Jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn"], ["azul"], "humano"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul", "rojo"], "humano"),
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "amarillo", "blanco"], "togruta"),
    Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde"], "humano"),
    Jedi("Kit Fisto", ["Yoda"], ["verde"], "nautolano"),
    Jedi("Plo Koon", ["Maestro Sifo-Dyas"], ["azul"], "kel dor"),
    Jedi("Mace Windu", ["Yoda"], ["violeta"], "humano"),
    Jedi("Qui-Gon Jinn", ["Conde Dooku"], ["verde"], "humano"),
    Jedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "twi'lek"),
    Jedi("Ki-Adi-Mundi", ["Yoda"], ["azul"], "cereano"),
])

# Registrar las funciones criterio en la lista (para que funcionen search/sort)
jedi_list.add_criterion('nombre', criterio_nombre)
jedi_list.add_criterion('especie', criterio_especie)


print("=========================================")
print("  EJECUCIÓN DE LAS ACTIVIDADES (JEDI)")
print("=========================================\n")


# --- a. listado ordenado por nombre y por especie ---
print("--- a. Listado ordenado por nombre ---")
# Usamos sort_by_criterion
jedi_list.sort_by_criterion('nombre')
jedi_list.show() # Usamos el método show()

print("\n--- a. Listado ordenado por especie ---")
jedi_list.sort_by_criterion('especie')
jedi_list.show()
print("-" * 30)


# --- b. mostrar toda la información de Ahsoka Tano y Kit Fisto ---
print("\n--- b. Información completa de Ahsoka Tano y Kit Fisto ---")
nombres_buscados_b = ["Ahsoka Tano", "Kit Fisto"]

for nombre_buscado in nombres_buscados_b:
    # Usamos search
    indice = jedi_list.search(nombre_buscado, search_key='nombre')
    if indice is not None:
        jedi = jedi_list[indice]
        print(f"\n--- {jedi.nombre} ---")
        print(f"  Especie: {jedi.especie}")
        print(f"  Maestros: {', '.join(jedi.maestros)}")
        print(f"  Sables: {', '.join(jedi.sables)}")
    else:
        print(f"{nombre_buscado}: No encontrado.")
print("-" * 30)


# --- c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices ---
print("\n--- c. Padawans de Yoda y Luke Skywalker ---")
maestros_buscados_c = ["Yoda", "Luke Skywalker"]
padawans_encontrados = {}

for jedi in jedi_list:
    for maestro in maestros_buscados_c:
        if maestro in jedi.maestros:
            if maestro not in padawans_encontrados:
                padawans_encontrados[maestro] = []
            padawans_encontrados[maestro].append(jedi.nombre)

for maestro, padawans in padawans_encontrados.items():
    print(f"Padawans de {maestro}: {', '.join(padawans)}")

# Si Luke no tiene padawan en la lista, su clave no aparecerá
if "Luke Skywalker" not in padawans_encontrados:
    print("Padawans de Luke Skywalker: Ninguno en la lista.")
print("-" * 30)


# --- d. mostrar los Jedi de especie humana y twi'lek ---
print("\n--- d. Jedi de especie humana y twi'lek ---")
especies_buscadas_d = ["humano", "twi'lek"]
jedi_encontrados_d = []

for jedi in jedi_list:
    if jedi.especie.lower() in especies_buscadas_d:
        jedi_encontrados_d.append((jedi.nombre, jedi.especie))

for nombre, especie in jedi_encontrados_d:
    print(f"- {nombre} (Especie: {especie})")
print("-" * 30)


# --- e. listar todos los Jedi que comienzan con A ---
print("\n--- e. Jedi que comienzan con 'A' ---")
jedi_con_a = []

for jedi in jedi_list:
    if jedi.nombre.startswith('A'):
        jedi_con_a.append(jedi.nombre)

print("Jedi encontrados:", ", ".join(jedi_con_a))
print("-" * 30)


# --- f. mostrar los Jedi que usaron sable de luz de más de un color ---
print("\n--- f. Jedi que usaron más de un color de sable ---")
jedi_multi_sable = []

for jedi in jedi_list:
    if len(jedi.sables) > 1:
        sables_str = ", ".join(jedi.sables)
        jedi_multi_sable.append(f"{jedi.nombre} (Colores: {sables_str})")

for info in jedi_multi_sable:
    print(f"- {info}")
print("-" * 30)


# --- g. indicar los Jedi que utilizaron sable de luz amarillo o violeta ---
print("\n--- g. Jedi con sable de luz amarillo o violeta ---")
colores_buscados_g = {"amarillo", "violeta"}
jedi_con_color = []

for jedi in jedi_list:
    # Convertimos la lista de sables a un conjunto para una verificación más rápida
    if colores_buscados_g.intersection(set(jedi.sables)):
        jedi_con_color.append(jedi.nombre)

print("Jedi encontrados:", ", ".join(jedi_con_color))
print("-" * 30)


# --- h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron ---
print("\n--- h. Padawans de Qui-Gon Jin y Mace Windu ---")
maestros_buscados_h = ["Qui-Gon Jinn", "Mace Windu"]
padawans_encontrados_h = {m: [] for m in maestros_buscados_h}

for jedi in jedi_list:
    for maestro in maestros_buscados_h:
        if maestro in jedi.maestros:
            padawans_encontrados_h[maestro].append(jedi.nombre)

for maestro, padawans in padawans_encontrados_h.items():
    if padawans:
        print(f"Padawans de {maestro}: {', '.join(padawans)}")
    else:
        print(f"Padawans de {maestro}: Ninguno en la lista.")
print("-" * 30)