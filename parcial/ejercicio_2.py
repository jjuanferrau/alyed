from graph import Graph
from stack import Stack
from star_wars_data import character_data, edge_data

def print_mst(mst_string):
    """
    Toma el string de salida de Kruskal y lo imprime de forma legible calculando el peso total.
    """
    if not mst_string:
        print("No se pudo generar el árbol.")
        return

    total_weight = 0
    print("  Aristas del Árbol de Expansión Mínimo:")
    try:
        edges = mst_string.split(';')
        for edge in edges:
            parts = edge.split('-')
            if len(parts) == 3:
                origin, dest, weight = parts
                print(f"    - {origin} <-> {dest} (Episodios: {weight})")
                total_weight += int(weight)
        print(f"  Peso total del árbol (mínimo de episodios): {total_weight}\n")
    except Exception as e:
        print(f"  Error parseando el árbol: {mst_string} ({e})")


def find_shortest_path(graph, origin, destination):
    """
    Ejecuta Dijkstra y parsea la pila resultante
    para mostrar el camino más corto y su costo.
    """
    
    #Obtenemos la pila de Dijkstra
    path_stack = graph.dijkstra(origin)

    #Parseamos la pila para encontrar el camino
    total_weight = None
    full_path = []

    # Como la pila se consume al leerla, la copiamos para el análisis
    temp_stack = Stack()
    while path_stack.size() > 0:
        temp_stack.push(path_stack.pop())
    
    # Restauramos la pila original y buscamos el destino
    dest_copy = destination
    while temp_stack.size() > 0:
        value = temp_stack.pop()
        path_stack.push(value)
        
        if value[0] == dest_copy:
            if total_weight is None:
                # El costo total es el del nodo destino
                total_weight = value[1] 
            full_path.append(value[0])
            dest_copy = value[2] # Movemos al "padre"
    
    full_path.reverse()

    #Imprimimos el resultado
    print(f"Camino más corto de {origin} a {destination}:")
    if total_weight is not None and full_path[0] == origin:
        print(f"  Camino: {' -> '.join(full_path)}")
        print(f"  Costo total (mínima suma de episodios): {total_weight}")
    else:
        print(f"  No se encontró un camino.")

#Cargar el grafo

print("Cargando grafo de Star Wars...")
g = Graph(is_directed=True) 

#Insertar vértices
for name, data in character_data:
    g.insert_vertex(name, other_values=data)

#Insertar aristas
for origin, dest, weight in edge_data:
    g.insert_edge(origin, dest, weight)

print("Grafo cargado.")

#Árbol de expansión mínimo

print("\n--- Árbol de Expansión Mínimo (MST) ---")

mst_vertices = ['C-3PO', 'Yoda', 'Leia']
for vertex_name in mst_vertices:
    print(f"Calculando MST desde {vertex_name}:")
    # La función kruskal() devuelve un string con las aristas
    mst_result_string = g.kruskal(vertex_name)
    print_mst(mst_result_string)

#Número máximo de episodios compartidos

print("\n--- Pares con Máximo de Episodios Compartidos ---")
max_weight = 0
pairs = []
visited_edges = set()

# Iteramos sobre el grafo
for vertex in g:
    # Iteramos sobre las aristas de cada vértice
    for edge in vertex.edges:
        weight = edge.weight
        # Usamos un tuple ordenado para no duplicar (A,B) y (B,A)
        pair = tuple(sorted((vertex.value, edge.value)))
        
        if pair in visited_edges:
            continue

        if weight > max_weight:
            max_weight = weight
            pairs = [pair] # Nueva lista con el nuevo máximo
        elif weight == max_weight:
            pairs.append(pair) # Añadir a la lista de máximos
        
        visited_edges.add(pair)

print(f"El número máximo de episodios compartidos es: {max_weight}")
print("Pares que coinciden con este número:")
for pair in pairs:
    print(f"  - {pair[0]} y {pair[1]}")

#Camino más corto (Dijkstra)

print("\n--- Camino Más Corto (Dijkstra) ---")

find_shortest_path(g, 'C-3PO', 'R2-D2')
print()
find_shortest_path(g, 'Yoda', 'Darth Vader')

#Personajes en 9 episodios

print("\n--- Personajes en los Nueve Episodios ---")

nine_episode_chars = []
for vertex in g:
    if (vertex.other_values and 
        vertex.other_values.get('episodes') == 9):
        nine_episode_chars.append(vertex.value)

if nine_episode_chars:
    print("Personajes encontrados (según datos cargados):")
    for char_name in nine_episode_chars:
        print(f"  - {char_name}")
else:
    print("Ningún personaje tiene 9 episodios (según datos cargados).")