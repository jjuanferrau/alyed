from queue_ import Queue 
class Caracteristicas_Heroe:
    # caracteristicas del personaje
    def __init__(self, character_name, superhero_name, gender):
        self.character_name = character_name
        self.superhero_name = superhero_name
        self.gender = gender 

    def __str__(self):
        # representacion en string del personaje
        return f"Personaje: {self.character_name}, Superhéroe: {self.superhero_name}, Género: {self.gender}"

    def __repr__(self):
        # representacion para prueba
        return f"Caracteristicas_Heroe(character_name='{self.character_name}', superhero_name='{self.superhero_name}', gender='{self.gender}')"

def cargar_cola():
    # crea y devuelve la cola
    q = Queue()
    q.arrive(Caracteristicas_Heroe("Tony Stark", "Iron Man", "M"))
    q.arrive(Caracteristicas_Heroe("Steve Rogers", "Capitán América", "M"))
    q.arrive(Caracteristicas_Heroe("Natasha Romanoff", "Black Widow", "F"))
    q.arrive(Caracteristicas_Heroe("Carol Danvers", "Capitana Marvel", "F"))
    q.arrive(Caracteristicas_Heroe("Bruce Banner", "Hulk", "M"))
    q.arrive(Caracteristicas_Heroe("Scott Lang", "Ant-Man", "M"))
    q.arrive(Caracteristicas_Heroe("Thor Odinson", "Thor", "M"))
    q.arrive(Caracteristicas_Heroe("Wanda Maximoff", "Scarlet Witch", "F"))
    q.arrive(Caracteristicas_Heroe("Peter Parker", "Spider-Man", "M"))
    q.arrive(Caracteristicas_Heroe("Stephen Strange", "Dr. Strange", "M"))
    q.arrive(Caracteristicas_Heroe("Shuri", "Black Panther (nueva)", "F")) 
    q.arrive(Caracteristicas_Heroe("Sam Wilson", "Capitán América (nuevo)", "M")) 
    return q

# inicializa la cola
mcu_characters_queue = cargar_cola()
print("--- Cola de Personajes MCU Original ---")
mcu_characters_queue.show()
print("-" * 50)

def nombre_capitana_marvel(q: Queue):
    # a. determina el nombre del personaje de la superheroe capitana marvel;
    print("\n--- Resolviendo punto a: Nombre del personaje de Capitana Marvel ---")
    
    found_character_name = None
    original_size = q.size()

    # recorre la cola para encontrar el personaje
    for _ in range(original_size):
        character = q.attention()
        if character.superhero_name == "Capitana Marvel":
            found_character_name = character.character_name
        q.arrive(character) 
    
    if found_character_name:
        print(f"  El nombre del personaje de Capitana Marvel es: {found_character_name}")
    else:
        print("  Capitana Marvel no se encontró en la cola.")
    
    print("  Cola después de la operación (datos intactos):")
    q.show()
    print("-" * 50)


def sh_femeninos(q: Queue):
    # b. muestra el nombre de los superheroes femeninos 
    print("\n--- Resolviendo punto b: Nombres de superhéroes femeninos ---")
    
    female_superheroes = []
    original_size = q.size()

    for _ in range(original_size):
        character = q.attention()
        if character.gender == "F":
            female_superheroes.append(character.superhero_name)
        q.arrive(character) 
    
    if female_superheroes:
        print("  Superhéroes femeninos:")
        for superhero in female_superheroes:
            print(f"  - {superhero}")
    else:
        print("  No se encontraron superhéroes femeninos en la cola.")
    
    print("  Cola después de la operación (datos intactos):")
    q.show()
    print("-" * 50)


def sh_masculinos(q: Queue):
    # c. muestra el nombre de los superheroes masculinos
    print("\n--- Resolviendo punto c: Nombres de personajes masculinos ---")
    
    male_characters = []
    original_size = q.size()

    for _ in range(original_size):
        character = q.attention()
        if character.gender == "M":
            male_characters.append(character.character_name)
        q.arrive(character) # Volvemos a encolar el personaje
    
    if male_characters:
        print("  Personajes masculinos:")
        for character_name in male_characters:
            print(f"  - {character_name}")
    else:
        print("  No se encontraron personajes masculinos en la cola.")
    
    print("  Cola después de la operación (datos intactos):")
    q.show()
    print("-" * 50)


def nombre_scott_lang(q: Queue):
    # d. determina el nombre del superhéroe del personaje scott lang;
    print("\n--- Resolviendo punto d: Nombre del superhéroe de Scott Lang ---")
    
    found_superhero_name = None
    original_size = q.size()

    for _ in range(original_size):
        character = q.attention()
        if character.character_name == "Scott Lang":
            found_superhero_name = character.superhero_name
        q.arrive(character)
    
    if found_superhero_name:
        print(f"  El superhéroe de Scott Lang es: {found_superhero_name}")
    else:
        print("  Scott Lang no se encontró en la cola.")
    
    print("  Cola después de la operación (datos intactos):")
    q.show()
    print("-" * 50)


def nombres_inicial_s(q: Queue):
    # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
    # con la letra S;
    print("\n--- Resolviendo punto e: Personajes/Superhéroes que comienzan con 'S' ---")
    
    s_starting_characters = []
    original_size = q.size()

    for _ in range(original_size):
        character = q.attention()
        # verifica si el personaje comienza con la letra s
        if character.character_name.startswith('S') or character.superhero_name.startswith('S'):
            s_starting_characters.append(character)
        q.arrive(character) 
    
    if s_starting_characters:
        print("  Personajes/Superhéroes cuyos nombres (o de personajes) comienzan con 'S':")
        for char in s_starting_characters:
            print(f"  - {char}")
    else:
        print("  No se encontraron personajes o superhéroes que comiencen con 'S'.")
    
    print("  Cola después de la operación (datos intactos):")
    q.show()
    print("-" * 50)

if __name__ == "__main__":
    nombre_capitana_marvel(mcu_characters_queue)
    sh_femeninos(mcu_characters_queue)
    sh_masculinos(mcu_characters_queue)
    nombre_scott_lang(mcu_characters_queue)
    nombres_inicial_s(mcu_characters_queue)

    print("\n--- Estado final de la cola de personajes MCU ---")
    mcu_characters_queue.show()