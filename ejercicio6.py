from class_list import List 
from typing import Any, Optional

# --- Definición de la Clase ---

class Superhero:
    """Clase para representar a un superhéroe."""
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        """Representación legible del objeto."""
        return (f"Nombre: {self.nombre} | Año: {self.anio_aparicion} | "
                f"Casa: {self.casa} | Biografía: {self.biografia[:40]}...")


# --- Funciones Criterio para la clase List ---

# Necesarias para que los métodos sort_by_criterion y search funcionen con objetos
def criterio_nombre(superheroe: Superhero) -> str:
    return superheroe.nombre

def criterio_anio(superheroe: Superhero) -> int:
    return superheroe.anio_aparicion

def criterio_casa(superheroe: Superhero) -> str:
    return superheroe.casa


# --- Inicialización de la Lista ---

superheroes = List([
    Superhero("Linterna Verde", 1940, "DC", "Un miembro de un cuerpo intergaláctico de policía llamado los Green Lantern Corps. Su anillo de poder..."),
    Superhero("Wolverine", 1974, "Marvel", "Mutante con poderes de curación y garras retráctiles de Adamantium. Es conocido por su ferocidad..."),
    Superhero("Dr. Strange", 1963, "DC", "El Hechicero Supremo. Originalmente un neurocirujano brillante, viajó en busca de una cura, encontrando las artes místicas..."),
    Superhero("Iron Man", 1963, "Marvel", "Tony Stark, un genio, millonario... usa un traje de armadura de alta tecnología para combatir el crimen..."),
    Superhero("Capitán América", 1941, "Marvel", "Soldado de la Segunda Guerra Mundial mejorado con un suero. Viste un traje especial y utiliza un escudo de vibranium..."),
    Superhero("Flash", 1940, "DC", "Un metahumano con el poder de la supervelocidad, capaz de correr más rápido que la luz..."),
    Superhero("Star-Lord", 1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia. Un humano con habilidades y equipo avanzados..."),
    Superhero("Batman", 1939, "DC", "El Caballero Oscuro. Bruce Wayne... usa su intelecto, habilidades de detective y un traje blindado..."),
    Superhero("Mujer Maravilla", 1941, "DC", "Diana, una amazona con habilidades divinas. Lucha por la paz y la justicia usando su lazo de la verdad..."),
    Superhero("Capitana Marvel", 1968, "Marvel", "Carol Danvers, una piloto de la Fuerza Aérea con superpoderes cósmicos..."),
    Superhero("Spider-Man", 1962, "Marvel", "Peter Parker, mordido por una araña radiactiva. Viste un traje que él mismo diseñó..."),
    Superhero("Superman", 1938, "DC", "El Hombre de Acero. Un alienígena de Krypton enviado a la Tierra..."),
    Superhero("Black Panther", 1966, "Marvel", "T'Challa, rey de Wakanda. Viste un traje hecho de vibranium."),
])

# Registrar las funciones criterio en la lista (para que funcionen search/sort)
superheroes.add_criterion('nombre', criterio_nombre)
superheroes.add_criterion('anio', criterio_anio)
superheroes.add_criterion('casa', criterio_casa)

print("=========================================")
print("  EJECUCION DE LAS ACTIVIDADES (RESULTADOS)")
print("=========================================\n")


# --- a. eliminar el nodo que contiene la información de Linterna Verde ---
print("--- a. Eliminar Linterna Verde ---")
# Usamos delete_value 
eliminado = superheroes.delete_value("Linterna Verde", key_value='nombre') 

if eliminado:
    print(f"Se ha eliminado a {eliminado.nombre}.")
else:
    print("Linterna Verde no encontrado.")
print("-" * 30)


# --- b. mostrar el año de aparición de Wolverine ---
print("\n--- b. Año de aparición de Wolverine ---")
# Usamos search
indice_wolverine = superheroes.search("Wolverine", search_key='nombre')

if indice_wolverine is not None:
    wolverine = superheroes[indice_wolverine]
    print(f"El año de aparición de {wolverine.nombre} es {wolverine.anio_aparicion}.")
else:
    print("Wolverine no encontrado.")
print("-" * 30)


# --- c. cambiar la casa de Dr. Strange a Marvel ---
print("\n--- c. Cambiar la casa de Dr. Strange a Marvel ---")
# Usamos search
indice_dr_strange = superheroes.search("Dr. Strange", search_key='nombre')

if indice_dr_strange is not None:
    dr_strange = superheroes[indice_dr_strange]
    dr_strange.casa = "Marvel" # Modificación directa del atributo
    print(f"La casa de {dr_strange.nombre} se ha cambiado a {dr_strange.casa}.")
else:
    print("Dr. Strange no encontrado.")
print("-" * 30)


# --- d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura” ---
print("\n--- d. Superhéroes con 'traje' o 'armadura' en biografía ---")
palabras_clave = ["traje", "armadura"]
encontrados_d = []

# Iteración normal, ya que no hay un método de búsqueda binaria por substring en la biografía
for s in superheroes:
    biografia_lower = s.biografia.lower()
    if any(palabra in biografia_lower for palabra in palabras_clave):
        encontrados_d.append(s.nombre)

print("Superhéroes encontrados:")
for nombre in encontrados_d:
    print(f"- {nombre}")
print("-" * 30)


# --- e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963 ---
print("\n--- e. Superhéroes aparecidos antes de 1963 ---")
anio_limite = 1963
encontrados_e = []
for s in superheroes:
    if s.anio_aparicion < anio_limite:
        encontrados_e.append((s.nombre, s.casa))

print(f"Aparecidos antes de {anio_limite}:")
for nombre, casa in encontrados_e:
    print(f"- {nombre} ({casa})")
print("-" * 30)


# --- f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla ---
print("\n--- f. Casa de Capitana Marvel y Mujer Maravilla ---")
nombres_buscados_f = ["Capitana Marvel", "Mujer Maravilla"]

for nombre_buscado in nombres_buscados_f:
    # Usamos search
    indice = superheroes.search(nombre_buscado, search_key='nombre')
    if indice is not None:
        superheroe = superheroes[indice]
        print(f"{nombre_buscado}: {superheroe.casa}")
    else:
        print(f"{nombre_buscado}: No encontrado.")
print("-" * 30)


# --- g. mostrar toda la información de Flash y Star-Lord ---
print("\n--- g. Información completa de Flash y Star-Lord ---")
nombres_buscados_g = ["Flash", "Star-Lord"]

for nombre_buscado in nombres_buscados_g:
    # Usamos search
    indice = superheroes.search(nombre_buscado, search_key='nombre')
    if indice is not None:
        superheroe = superheroes[indice]
        print(f"\n--- {superheroe.nombre} ---")
        print(f"  Año Aparición: {superheroe.anio_aparicion}")
        print(f"  Casa: {superheroe.casa}")
        print(f"  Biografía: {superheroe.biografia}")
    else:
        print(f"{nombre_buscado}: No encontrado.")
print("-" * 30)


# --- h. listar los superhéroes que comienzan con la letra B, M y S ---
print("\n--- h. Superhéroes que comienzan con B, M y S ---")
iniciales = {"B", "M", "S"}
superheroes_por_inicial = {}

# La lista se itera directamente
for s in superheroes:
    primera_letra = s.nombre[0].upper()
    if primera_letra in iniciales:
        if primera_letra not in superheroes_por_inicial:
            superheroes_por_inicial[primera_letra] = []
        superheroes_por_inicial[primera_letra].append(s.nombre)

print("Superhéroes encontrados:")
for inicial in sorted(iniciales):
    nombres = superheroes_por_inicial.get(inicial, [])
    print(f"- {inicial}: {', '.join(nombres) if nombres else 'Ninguno'}")
print("-" * 30)


# --- i. determinar cuántos superhéroes hay de cada casa de comic ---
print("\n--- i. Conteo de Superhéroes por Casa de Comic ---")
conteo = {}

# La lista se itera directamente
for s in superheroes:
    casa = s.casa
    conteo[casa] = conteo.get(casa, 0) + 1
            
print("Conteo final:")
for casa, cantidad in conteo.items():
    print(f"- {casa}: {cantidad} superhéroes.")
print("-" * 30)