from collections import deque

# --- Definición de las Clases del Árbol ---

class NodoArbol:
    """
    Define la estructura de un nodo del árbol.
    - criatura (str): El nombre de la criatura (Clave del árbol).
    - capturada_por (str): Nombre del héroe o dios que la capturó.
    - descripcion (str): Descripción de la criatura.
    """
    def __init__(self, criatura, capturada_por=None, descripcion=""):
        self.criatura = criatura
        self.capturada_por = capturada_por
        self.descripcion = descripcion
        self.izq = None
        self.der = None

class ArbolMitologia:
    """Implementa la lógica del Árbol Binario de Búsqueda y las operaciones solicitadas."""
    def __init__(self):
        self.raiz = None

    # --- Métodos Básicos del Árbol (Insertar, Buscar, Eliminar) ---

    def insertar(self, criatura, capturada_por=None, descripcion=""):
        """Método público para insertar un nodo."""
        self.raiz = self._insertar(self.raiz, criatura, capturada_por, descripcion)

    def _insertar(self, nodo, criatura, capturada_por, descripcion):
        """Método recursivo privado para la inserción."""
        if nodo is None:
            return NodoArbol(criatura, capturada_por, descripcion)
        
        if criatura < nodo.criatura:
            nodo.izq = self._insertar(nodo.izq, criatura, capturada_por, descripcion)
        else:
            nodo.der = self._insertar(nodo.der, criatura, capturada_por, descripcion)
        return nodo

    def buscar(self, criatura):
        """Método público para buscar un nodo."""
        return self._buscar(self.raiz, criatura)

    def _buscar(self, nodo, criatura):
        """Método recursivo privado para buscar."""
        if nodo is None or nodo.criatura == criatura:
            return nodo
        
        if criatura < nodo.criatura:
            return self._buscar(nodo.izq, criatura)
        else:
            return self._buscar(nodo.der, criatura)

    def _obtener_minimo(self, nodo):
        """Obtiene el nodo con el valor mínimo (más a la izquierda)."""
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def eliminar(self, criatura):
        """Método público para eliminar un nodo."""
        print(f"   [Acción] Eliminando a '{criatura}'...")
        self.raiz = self._eliminar(self.raiz, criatura)

    def _eliminar(self, nodo, criatura):
        """Método recursivo privado para eliminar."""
        if nodo is None:
            return nodo

        # Buscar el nodo a eliminar
        if criatura < nodo.criatura:
            nodo.izq = self._eliminar(nodo.izq, criatura)
        elif criatura > nodo.criatura:
            nodo.der = self._eliminar(nodo.der, criatura)
        else:
            # Nodo encontrado. Casos de eliminación:
            # 1. Nodo con un solo hijo o sin hijos
            if nodo.izq is None:
                temp = nodo.der
                nodo = None
                return temp
            elif nodo.der is None:
                temp = nodo.izq
                nodo = None
                return temp
            
            # 2. Nodo con dos hijos
            # Encontrar el sucesor inorden (el más pequeño del subárbol derecho)
            temp = self._obtener_minimo(nodo.der)
            
            # Copiar los datos del sucesor a este nodo
            nodo.criatura = temp.criatura
            nodo.capturada_por = temp.capturada_por
            nodo.descripcion = temp.descripcion
            
            # Eliminar el sucesor inorden
            nodo.der = self._eliminar(nodo.der, temp.criatura)
            
        return nodo

    # --- Soluciones a los Requisitos del Problema ---

    # a. Listado inorden de las criaturas y quienes la derrotaron
    def listado_inorden_captor(self):
        print("Listado Inorden (Criatura - Capturada por):")
        self._inorden_captor(self.raiz)

    def _inorden_captor(self, nodo):
        if nodo is not None:
            self._inorden_captor(nodo.izq)
            captor = nodo.capturada_por if nodo.capturada_por else "Nadie"
            print(f"- {nodo.criatura:<20} (Capturada por: {captor})")
            self._inorden_captor(nodo.der)

    # b. Permitir cargar una breve descripción sobre cada criatura
    def agregar_descripcion(self, criatura, descripcion):
        nodo = self.buscar(criatura)
        if nodo:
            nodo.descripcion = descripcion
            print(f"   [Acción] Descripción agregada a '{criatura}'.")
        else:
            print(f"   [Error] No se encontró a '{criatura}' para agregar descripción.")

    # c. Mostrar toda la información de la criatura Talos
    def mostrar_informacion(self, criatura):
        print(f"Información completa de '{criatura}':")
        nodo = self.buscar(criatura)
        if nodo:
            print(f"  - Nombre: {nodo.criatura}")
            captor = nodo.capturada_por if nodo.capturada_por else "Nadie"
            print(f"  - Capturada por: {captor}")
            desc = nodo.descripcion if nodo.descripcion else "(Sin descripción)"
            print(f"  - Descripción: {desc}")
        else:
            print(f"  - No se encontró a la criatura '{criatura}'.")

    # d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
    def top_3_derrotadores(self):
        print("Top 3 héroes/dioses con más criaturas derrotadas:")
        conteo = {}
        self._contar_derrotas(self.raiz, conteo)
        
        # Filtrar a 'Nadie' o None
        if None in conteo:
            del conteo[None]
        
        # Ordenar el diccionario por valores (cantidad de derrotas) de forma descendente
        heroes_ordenados = sorted(conteo.items(), key=lambda item: item[1], reverse=True)
        
        # Mostrar los 3 primeros
        for i, (heroe, cantidad) in enumerate(heroes_ordenados[:3]):
            print(f"  {i+1}. {heroe} (con {cantidad} criaturas)")

    def _contar_derrotas(self, nodo, conteo):
        """Recorre el árbol y llena el diccionario de conteo."""
        if nodo is not None:
            captor = nodo.capturada_por
            if captor:
                conteo[captor] = conteo.get(captor, 0) + 1
            
            self._contar_derrotas(nodo.izq, conteo)
            self._contar_derrotas(nodo.der, conteo)

    # e. y n. Listar las criaturas derrotadas/capturadas por Heracles
    def listar_derrotadas_por(self, heroe_dios):
        print(f"Criaturas capturadas por '{heroe_dios}':")
        self._inorden_derrotadas_por(self.raiz, heroe_dios)

    def _inorden_derrotadas_por(self, nodo, heroe_dios):
        if nodo is not None:
            self._inorden_derrotadas_por(nodo.izq, heroe_dios)
            if nodo.capturada_por == heroe_dios:
                print(f"- {nodo.criatura}")
            self._inorden_derrotadas_por(nodo.der, heroe_dios)

    # f. Listar las criaturas que no han sido derrotadas
    def listar_no_derrotadas(self):
        print("Criaturas que no han sido derrotadas:")
        self._inorden_no_derrotadas(self.raiz)

    def _inorden_no_derrotadas(self, nodo):
        if nodo is not None:
            self._inorden_no_derrotadas(nodo.izq)
            if not nodo.capturada_por: # Si es None o ""
                print(f"- {nodo.criatura}")
            self._inorden_no_derrotadas(nodo.der)

    # h. Modificar nodos indicando que Heracles las atrapó
    def asignar_captura_heracles(self, criaturas_lista):
        print("   [Acción] Asignando capturas a Heracles...")
        for criatura in criaturas_lista:
            nodo = self.buscar(criatura)
            if nodo:
                nodo.capturada_por = "Heracles"
                print(f"   - '{criatura}' ahora está capturada por Heracles.")
            else:
                print(f"   - [Error] No se encontró a '{criatura}' para modificar.")

    # i. Permitir búsquedas por coincidencia
    def busqueda_por_coincidencia(self, subcadena):
        print(f"Resultados de búsqueda por coincidencia para '{subcadena}':")
        self._preorden_coincidencia(self.raiz, subcadena)

    def _preorden_coincidencia(self, nodo, subcadena):
        """Recorre en preorden buscando coincidencias."""
        if nodo is not None:
            if subcadena.lower() in nodo.criatura.lower():
                print(f"  - Coincidencia encontrada: {nodo.criatura}")
                self.mostrar_informacion(nodo.criatura) # Reutilizamos el método 'c'
            
            self._preorden_coincidencia(nodo.izq, subcadena)
            self._preorden_coincidencia(nodo.der, subcadena)

    # l. Modificar el nombre de la criatura Ladón por Dragón Ladón
    def modificar_nombre(self, nombre_viejo, nombre_nuevo):
        """
        Modifica la clave de un nodo.
        Esto requiere eliminar el nodo viejo y reinsertar uno nuevo.
        """
        print(f"   [Acción] Modificando '{nombre_viejo}' a '{nombre_nuevo}'...")
        nodo_viejo = self.buscar(nombre_viejo)
        if nodo_viejo:
            # Guardar datos
            captor = nodo_viejo.capturada_por
            desc = nodo_viejo.descripcion
            
            # Eliminar e insertar
            self.eliminar(nombre_viejo)
            self.insertar(nombre_nuevo, captor, desc)
            print(f"   - Modificación completa.")
        else:
            print(f"   - [Error] No se encontró a '{nombre_viejo}' para renombrar.")
    
    # m. Realizar un listado por nivel del árbol
    def listado_por_nivel(self):
        print("Listado por Nivel (Recorrido BFS):")
        if not self.raiz:
            print("  - El árbol está vacío.")
            return

        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            print(f"- {nodo.criatura}")
            
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)


# --- Función Principal (Main) ---

def main():
    # Cargar los datos de la tabla
    datos_criaturas = [
        ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
        ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
        ("Caribdis", None), ("Euriále", None), ("Esteno", None),
        ("Medusa", "Perseo"), ("Ladón", "Heracles"), ("Águila del Cáucaso", None),
        ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
        ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"),
        ("Dragón de la Cólquida", None), ("Cerbero", None), ("Cerda de Cromión", "Teseo"),
        ("Ortro", "Heracles"), ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"),
        ("Carcinos", None), ("Gerión", "Heracles"), ("Cloto", None),
        ("Láquesis", None), ("Átropos", None), ("Minotauro de Creta", "Teseo"),
        ("Harpías", None), ("Argos Panoptes", "Hermes"), ("Aves del Estínfalo", None),
        ("Talos", "Medea"), ("Sirenas", None), ("Pitón", "Apolo"),
        ("Cierva Cerinea", None), ("Basilisco", None), ("Jabalí de Erimanto", None)
    ]
    
    # Crear el árbol
    arbol_mitos = ArbolMitologia()
    print("Cargando criaturas en el árbol...")
    for criatura, captor in datos_criaturas:
        arbol_mitos.insertar(criatura, captor)
    
    print("\n" + "="*50)
    print("   EJECUCIÓN DE LOS REQUISITOS (MITOLOGÍA)")
    print("="*50)

    # a. Listado inorden de las criaturas y quienes la derrotaron
    print("\n--- Requisito a: Listado Inorden ---")
    arbol_mitos.listado_inorden_captor()

    # b. Permitir cargar una breve descripción
    print("\n--- Requisito b: Cargar Descripción ---")
    arbol_mitos.agregar_descripcion("Talos", "Un gigante de bronce que protegía Creta.")
    arbol_mitos.agregar_descripcion("Quimera", "Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente.")

    # c. Mostrar toda la información de la criatura Talos
    print("\n--- Requisito c: Mostrar Información de Talos ---")
    arbol_mitos.mostrar_informacion("Talos")

    # d. Determinar los 3 héroes o dioses con más derrotas
    print("\n--- Requisito d: Top 3 Derrotadores ---")
    arbol_mitos.top_3_derrotadores()

    # e. Listar las criaturas derrotadas por Heracles
    print("\n--- Requisito e: Derrotadas por Heracles (Inicial) ---")
    arbol_mitos.listar_derrotadas_por("Heracles")

    # f. Listar las criaturas que no han sido derrotadas
    print("\n--- Requisito f: Criaturas no Derrotadas (Inicial) ---")
    arbol_mitos.listar_no_derrotadas()

    # h. Modificar nodos (Cerbero, Toro de Creta, etc.)
    print("\n--- Requisito h: Asignar Capturas a Heracles ---")
    criaturas_para_heracles = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
    arbol_mitos.asignar_captura_heracles(criaturas_para_heracles)

    # i. Permitir búsquedas por coincidencia
    print("\n--- Requisito i: Búsqueda por Coincidencia ('Jabalí') ---")
    arbol_mitos.busqueda_por_coincidencia("Jabalí")

    # j. Eliminar a Basilisco y a las Sirenas
    print("\n--- Requisito j: Eliminar Nodos ---")
    arbol_mitos.eliminar("Basilisco")
    arbol_mitos.eliminar("Sirenas")

    # k. Modificar nodo Aves del Estínfalo
    print("\n--- Requisito k: Modificar Aves del Estínfalo ---")
    arbol_mitos.agregar_descripcion("Aves del Estínfalo", "Heracles derrotó a varias de ellas con sus flechas.")
    # Adicionalmente, asignamos a Heracles como captor ya que la tabla original
    # no tenía uno y el texto lo implica.
    nodo_aves = arbol_mitos.buscar("Aves del Estínfalo")
    if nodo_aves:
        nodo_aves.capturada_por = "Heracles"
        print("   [Acción] Se asigna 'Heracles' como captor de 'Aves del Estínfalo'.")


    # l. Modificar el nombre de Ladón por Dragón Ladón
    print("\n--- Requisito l: Modificar Nombre (Ladón -> Dragón Ladón) ---")
    arbol_mitos.modificar_nombre("Ladón", "Dragón Ladón")

    # m. Realizar un listado por nivel del árbol
    print("\n--- Requisito m: Listado por Nivel (BFS) ---")
    arbol_mitos.listado_por_nivel()

    # n. Muestre las criaturas capturadas por Heracles (Post-modificaciones)
    print("\n--- Requisito n: Capturadas por Heracles (Actualizado) ---")
    # Este listado ahora incluirá las criaturas del punto 'h' y 'k'
    arbol_mitos.listar_derrotadas_por("Heracles")

    # Verificación final del Top 3 (después de las modificaciones de Heracles)
    print("\n--- Verificación: Top 3 Derrotadores (Actualizado) ---")
    arbol_mitos.top_3_derrotadores()

# Ejecutar el script
if __name__ == "__main__":
    main()