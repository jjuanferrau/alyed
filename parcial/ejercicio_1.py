from tree import BinaryTree
from pokemon_data import pokemon_data # Importamos los datos

tree_name = BinaryTree()
tree_number = BinaryTree()
tree_type = BinaryTree()

print("Cargando árboles...")
for pokemon in pokemon_data:
    tree_name.insert(pokemon['name'], pokemon)
    tree_number.insert(pokemon['number'], pokemon)
    
    for tipo in pokemon['types']:
        tree_type.insert(tipo, pokemon)

print("Árboles cargados.")

def search_by_proximity(root, search_value):
    """
    Busca por proximidad (si 'search_value' está en el nombre).
    """
    if root is not None:
        if search_value.lower() in root.value.lower():
            # Imprime el Pokémon encontrado
            print(f"  - {root.value} (N°{root.other_values['number']}): {root.other_values}")
        
        # Recorre ambos subárboles
        search_by_proximity(root.left, search_value)
        search_by_proximity(root.right, search_value)

def list_pokemon_by_type(root, type_to_search):
    """
    Muestra los nombres de Pokémon de un tipo específico, usando la
    búsqueda BST del árbol de tipos.
    """
    if root is not None:
        if root.value == type_to_search:
            # Encontramos uno, lo imprimimos y seguimos buscando en ambos lados por si hay más con la misma clave (tipo)
            print(f"  - {root.other_values['name']}")
            list_pokemon_by_type(root.left, type_to_search)
            list_pokemon_by_type(root.right, type_to_search)
        elif type_to_search < root.value:
            list_pokemon_by_type(root.left, type_to_search)
        else:
            list_pokemon_by_type(root.right, type_to_search)

def find_weak_pokemon(root, target_types):
    """
    Recorre el árbol y muestra los Pokémon cuyas debilidades
    coinciden con la lista 'target_types'.
    """
    if root is not None:
        find_weak_pokemon(root.left, target_types)
        
        pokemon_weaknesses = root.other_values['weaknesses']
        # Comprueba si alguna de las debilidades del Pokémon está en la lista objetivo
        if any(weakness in pokemon_weaknesses for weakness in target_types):
            print(f"  - {root.value} es débil a uno de los tipos {target_types}")
            
        find_weak_pokemon(root.right, target_types)

def count_types_in_tree(root, type_counts_dict):
    """
    Recorre el árbol de tipos y cuenta las ocurrencias de cada tipo.
    """
    if root is not None:
        count_types_in_tree(root.left, type_counts_dict)
        
        tipo = root.value
        type_counts_dict[tipo] = type_counts_dict.get(tipo, 0) + 1
            
        count_types_in_tree(root.right, type_counts_dict)

def count_by_bool_key(root, key_name):
    """
    Contador genérico basado en 'count_heroes' del 'tree.py'.
    Cuenta cuántos nodos tienen 'other_values[key_name]' == True.
    """
    count = 0
    if root is not None:
        if root.other_values[key_name] is True:
            count += 1
        count += count_by_bool_key(root.left, key_name)
        count += count_by_bool_key(root.right, key_name)
    return count



print("\n--- Búsqueda por número y nombre ---")
#Búsqueda por número
numero_a_buscar = 94
print(f"Buscando N° {numero_a_buscar}:")
node_result = tree_number.search(numero_a_buscar)
if node_result:
    print(f"Encontrado: {node_result.value}, {node_result.other_values}")
else:
    print("No encontrado.")

#Búsqueda por nombre
nombre_a_buscar = "char"
print(f"\nBuscando por proximidad '{nombre_a_buscar}':")
search_by_proximity(tree_name.root, nombre_a_buscar)

#Listar por tipos específicos

print("\n--- Listar Pokémon por tipo ---")
tipos_a_listar = ['Fantasma', 'Fuego', 'Acero', 'Eléctrico']
for tipo in tipos_a_listar:
    print(f"\nTipo: {tipo}")
    list_pokemon_by_type(tree_type.root, tipo)

#Listados (ascendente y por nivel)

print("\n--- Listados ---")

print("\nListado ascendente por NÚMERO:")
# El 'in_order' de tree.py imprime valor y other_values
tree_number.in_order()

print("\nListado ascendente por NOMBRE:")
tree_name.in_order()

print("\nListado por NIVEL (Nombres):")
tree_name.by_level()

#Débiles frente a Jolteon, Lycanroc y Tyrantrum

print("\n--- Débiles frente a Jolteon, Lycanroc y Tyrantrum ---")
#Obtenemos los tipos de esos Pokémon
pokemon_objetivo_nombres = ["Jolteon", "Lycanroc", "Tyrantrum"]
tipos_debilidad_objetivo = set() # Usamos un set para evitar duplicados

for nombre in pokemon_objetivo_nombres:
    node = tree_name.search(nombre)
    if node:
        for tipo in node.other_values['types']:
            tipos_debilidad_objetivo.add(tipo)

print(f"Tipos a buscar (de {pokemon_objetivo_nombres}): {tipos_debilidad_objetivo}")

#Recorremos el árbol de nombres y comparamos debilidades
find_weak_pokemon(tree_name.root, list(tipos_debilidad_objetivo))

#Conteo de tipos de Pokémon

print("\n--- Conteo de tipos ---")
type_counts = {}
# Usamos el árbol de tipos (tree_type) para contarlos
count_types_in_tree(tree_type.root, type_counts)

for tipo, cantidad in type_counts.items():
    print(f"  - Tipo {tipo}: {cantidad} Pokémon")

#Contar Pokémon con Megaevolución

print("\n--- Conteo de Megaevoluciones ---")
# Usamos la función contadora genérica en el árbol de nombres
mega_count = count_by_bool_key(tree_name.root, 'mega')
print(f"Total de Pokémon con Megaevolución: {mega_count}")

#Contar Pokémon con forma Gigamax

print("\n--- Conteo de formas Gigamax ---")
gigamax_count = count_by_bool_key(tree_name.root, 'gigamax')
print(f"Total de Pokémon con forma Gigamax: {gigamax_count}")