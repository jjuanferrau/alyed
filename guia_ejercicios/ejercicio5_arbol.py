import os

# --- Definición de las Clases del Árbol ---

class NodoArbol:
    """Define la estructura de un nodo del árbol."""
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre       # Clave para el ordenamiento (alfabético)
        self.es_heroe = es_heroe   # Campo booleano (requisito a)
        self.izq = None
        self.der = None

class ArbolMCU:
    """Implementa la lógica del Árbol Binario de Búsqueda y las operaciones solicitadas."""
    def __init__(self):
        self.raiz = None

    # --- Métodos Básicos del Árbol ---

    def insertar(self, nombre, es_heroe):
        """Método público para insertar un nodo."""
        self.raiz = self._insertar(self.raiz, nombre, es_heroe)

    def _insertar(self, nodo, nombre, es_heroe):
        """Método recursivo privado para la inserción."""
        if nodo is None:
            return NodoArbol(nombre, es_heroe)
        
        # El orden es alfabético por nombre
        if nombre < nodo.nombre:
            nodo.izq = self._insertar(nodo.izq, nombre, es_heroe)
        else:
            nodo.der = self._insertar(nodo.der, nombre, es_heroe)
        return nodo

    # --- Soluciones a los Requisitos del Problema ---

    # b. Listar villanos ordenados alfabéticamente
    def listar_villanos_alfabeticamente(self):
        """Inicia el recorrido in-order para villanos."""
        print("Listado de villanos (orden alfabético):")
        self._in_order_villanos(self.raiz)

    def _in_order_villanos(self, nodo):
        """Recorrido in-order (izq, raíz, der) filtrando por villanos."""
        if nodo is not None:
            self._in_order_villanos(nodo.izq)
            if not nodo.es_heroe:  # False si es villano
                print(f"- {nodo.nombre}")
            self._in_order_villanos(nodo.der)

    # c. Mostrar todos los superhéroes que empiezan con C
    def mostrar_heroes_con_c(self):
        """Inicia el recorrido para buscar héroes que empiezan con 'C'."""
        print("Superhéroes cuyo nombre empieza con 'C':")
        self._post_order_heroes_c(self.raiz)

    def _post_order_heroes_c(self, nodo):
        """Recorre el árbol (cualquier orden sirve) y muestra héroes con 'C'."""
        if nodo is not None:
            self._post_order_heroes_c(nodo.izq)
            self._post_order_heroes_c(nodo.der)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                print(f"- {nodo.nombre}")

    # d. Determinar cuántos superhéroes hay en el árbol
    def contar_superheroes(self):
        """Inicia el conteo recursivo de superhéroes."""
        count = self._contar_heroes(self.raiz)
        print(f"Número total de superhéroes: {count}")
        return count

    def _contar_heroes(self, nodo):
        """Suma 1 por cada nodo de héroe encontrado."""
        if nodo is None:
            return 0
        
        # Cuenta 1 si es héroe, 0 si no
        es_heroe_actual = 1 if nodo.es_heroe else 0
        
        # Suma el nodo actual más los de sus subárboles
        return es_heroe_actual + self._contar_heroes(nodo.izq) + self._contar_heroes(nodo.der)

    # e. Búsqueda por proximidad y modificación
    def corregir_nombre(self, subcadena_buscar, nombre_correcto):
        """
        Busca un nodo por "proximidad" (usando una subcadena) 
        y modifica su nombre.
        """
        print(f"Buscando personaje que contenga '{subcadena_buscar}' para corregirlo...")
        self._buscar_y_modificar(self.raiz, subcadena_buscar, nombre_correcto)

    def _buscar_y_modificar(self, nodo, subcadena, nombre_nuevo):
        """
        Recorre el árbol. Si encuentra la subcadena, renombra el nodo.
        Nota: Esto puede romper el orden del BST si el nuevo nombre 
        es muy diferente, pero para un typo (Dcoctor -> Doctor) suele funcionar.
        """
        if nodo is not None:
            if subcadena in nodo.nombre:
                print(f"   [Encontrado] '{nodo.nombre}'. Modificando a '{nombre_nuevo}'.")
                nodo.nombre = nombre_nuevo
                return # Asumimos que solo hay uno
            
            # Continuar búsqueda
            self._buscar_y_modificar(nodo.izq, subcadena, nombre_nuevo)
            self._buscar_y_modificar(nodo.der, subcadena, nombre_nuevo)


    # f. Listar superhéroes ordenados de manera descendente
    def listar_heroes_descendente(self):
        """Inicia el recorrido in-order inverso para héroes."""
        print("Listado de superhéroes (orden descendente):")
        self._in_order_heroes_desc(self.raiz)

    def _in_order_heroes_desc(self, nodo):
        """Recorrido in-order inverso (der, raíz, izq) filtrando por héroes."""
        if nodo is not None:
            self._in_order_heroes_desc(nodo.der)
            if nodo.es_heroe:
                print(f"- {nodo.nombre}")
            self._in_order_heroes_desc(nodo.izq)

    # g. Generar un bosque (árbol de héroes y árbol de villanos)
    def generar_bosque(self):
        """Crea dos nuevos árboles (héroes y villanos) a partir del árbol principal."""
        arbol_heroes = ArbolMCU()
        arbol_villanos = ArbolMCU()
        
        print("Generando bosque (árbol de héroes y árbol de villanos)...")
        self._recorrer_y_separar(self.raiz, arbol_heroes, arbol_villanos)
        
        return arbol_heroes, arbol_villanos

    def _recorrer_y_separar(self, nodo, arbol_heroes, arbol_villanos):
        """Recorre el árbol original e inserta cada nodo en el árbol correspondiente."""
        if nodo is not None:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            
            self._recorrer_y_separar(nodo.izq, arbol_heroes, arbol_villanos)
            self._recorrer_y_separar(nodo.der, arbol_heroes, arbol_villanos)

    # --- Métodos Auxiliares para el Bosque (g-I y g-II) ---

    def contar_nodos(self):
        """Cuenta todos los nodos en este árbol."""
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izq) + self._contar_nodos_recursivo(nodo.der)

    def listar_alfabeticamente(self):
        """Imprime todos los nodos del árbol en orden alfabético."""
        self._in_order_completo(self.raiz)
    
    def _in_order_completo(self, nodo):
        if nodo is not None:
            self._in_order_completo(nodo.izq)
            print(f"- {nodo.nombre}")
            self._in_order_completo(nodo.der)


# --- Función Principal (Main) ---

def main():
    # Creamos el árbol principal
    arbol_mcu = ArbolMCU()

    # Lista de personajes (True = Héroe, False = Villano)
    # Incluimos el typo "Dcoctor Strange"
    personajes_mcu = [
        ("Iron Man", True),
        ("Thanos", False),
        ("Captain America", True),
        ("Loki", False),
        ("Thor", True),
        ("Red Skull", False),
        ("Hulk", True),
        ("Hela", False),
        ("Black Widow", True),
        ("Dcoctor Strange", True),  # <-- El error para el punto 'e'
        ("Spider-Man", True),
        ("Ultron", False),
        ("Captain Marvel", True),
        ("Killmonger", False),
        ("Hawkeye", True),
        ("Black Panther", True),
        ("Cable", True) # Otro héroe con C
    ]

    # Insertamos todos los personajes en el árbol
    print("Cargando personajes en el árbol MCU...")
    for nombre, es_heroe in personajes_mcu:
        arbol_mcu.insertar(nombre, es_heroe)
    
    # --- Ejecución de los Requisitos ---

    print("\n" + "="*40)
    print("   EJECUCIÓN DE LOS REQUISITOS")
    print("="*40)

    # b. Listar villanos ordenados alfabéticamente
    print("\n--- Requisito b: Villanos Alfabéticamente ---")
    arbol_mcu.listar_villanos_alfabeticamente()

    # c. Mostrar todos los superhéroes que empiezan con C
    print("\n--- Requisito c: Superhéroes con 'C' ---")
    arbol_mcu.mostrar_heroes_con_c()

    # d. Determinar cuántos superhéroes hay
    print("\n--- Requisito d: Conteo de Superhéroes ---")
    arbol_mcu.contar_superheroes()

    # e. Corregir "Dcoctor Strange"
    print("\n--- Requisito e: Corregir Nombre (Proximidad) ---")
    # Usamos "Strange" como búsqueda por proximidad
    arbol_mcu.corregir_nombre("Strange", "Doctor Strange")

    # f. Listar superhéroes ordenados de manera descendente
    print("\n--- Requisito f: Superhéroes Descendente ---")
    # Nota: "Doctor Strange" ahora aparecerá correctamente listado
    arbol_mcu.listar_heroes_descendente()

    # g. Generar un bosque
    print("\n--- Requisito g: Generar Bosque ---")
    arbol_heroes, arbol_villanos = arbol_mcu.generar_bosque()

    # g-I. Determinar cuántos nodos tiene cada árbol
    print("\n--- Requisito g-I: Conteo de Nodos del Bosque ---")
    print(f"Nodos en el árbol de HÉROES: {arbol_heroes.contar_nodos()}")
    print(f"Nodos en el árbol de VILLANOS: {arbol_villanos.contar_nodos()}")

    # g-II. Barrido ordenado alfabéticamente de cada árbol
    print("\n--- Requisito g-II: Barrido Alfabético (Héroes) ---")
    arbol_heroes.listar_alfabeticamente()
    
    print("\n--- Requisito g-II: Barrido Alfabético (Villanos) ---")
    arbol_villanos.listar_alfabeticamente()


# Ejecutar el script
if __name__ == "__main__":
    main()