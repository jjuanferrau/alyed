from queue_ import Queue   
from stack import Stack  

class Notification:
    # representa una notificación de redes sociales.
    def __init__(self, hour, app, message):
        self.hour = hour
        self.app = app
        self.message = message

    def __str__(self):
        return f"[{self.hour}] {self.app}: {self.message}"

    def __repr__(self):
        return f"Notification(hour='{self.hour}', app='{self.app}', message='{self.message}')"

def cola_prueba():
    # crea y devuelve una cola de notificaciones de ejemplo.
    q = Queue()
    q.arrive(Notification("10:00", "Facebook", "Nuevo amigo solicitado"))
    q.arrive(Notification("11:30", "Twitter", "¡Mira el nuevo tutorial de Python!"))
    q.arrive(Notification("12:15", "Instagram", "Alguien le gustó tu foto"))
    q.arrive(Notification("13:00", "Facebook", "Tienes 3 notificaciones nuevas"))
    q.arrive(Notification("14:30", "Twitter", "Aprende Python en 5 días con este curso"))
    q.arrive(Notification("15:00", "WhatsApp", "Mensaje de grupo"))
    q.arrive(Notification("15:50", "Facebook", "Feliz cumpleaños a un amigo"))
    q.arrive(Notification("16:00", "Twitter", "Hackeando con Python"))
    q.arrive(Notification("17:00", "LinkedIn", "Nueva conexión"))
    q.arrive(Notification("11:45", "TikTok", "Nuevo video viral"))
    q.arrive(Notification("15:30", "Snapchat", "Filtro divertido"))
    q.arrive(Notification("14:00", "Facebook", "Publicación de tu página"))
    return q

# inicializa la cola de notificaciones
notifications_queue = cola_prueba()
print("--- Cola de Notificaciones Original ---")
notifications_queue.show()
print("-" * 50)

def eliminar_notificaciones_facebook(q: Queue):
    # a. elimina de la cola todas las notificaciones de Facebook.
    # la función reconstruye la cola sin las notificaciones de Facebook.
    print("\n--- Resolviendo punto a: Eliminar notificaciones de Facebook ---")
    temp_queue = Queue()
    deleted_count = 0
    original_size = q.size()

    for _ in range(original_size):
        notification = q.attention()
        if notification.app != "Facebook":
            temp_queue.arrive(notification)
        else:
            deleted_count += 1
            print(f"  Eliminando: {notification}")
    
    for _ in range(temp_queue.size()):
        q.arrive(temp_queue.attention())
    
    print(f"  Total de notificaciones de Facebook eliminadas: {deleted_count}")
    print("  Cola después de eliminar notificaciones de Facebook:")
    q.show()
    print("-" * 50)


def twitter_python(q: Queue):
    # b. muestra todas las notificaciones de twitter, si el mensaje incluye
    # la palabra ‘python’.
    print("\n--- Resolviendo punto b: Mostrar notificaciones de Twitter con 'Python' ---")
    
    python_twitter_notifications = []
    original_size = q.size()

    # iterar sobre la cola
    for _ in range(original_size):
        notification = q.attention()
        if notification.app == "Twitter" and "Python" in notification.message:
            python_twitter_notifications.append(notification)
        q.arrive(notification)
    
    if python_twitter_notifications:
        print("  Notificaciones de Twitter con 'Python':")
        for notif in python_twitter_notifications:
            print(f"  - {notif}")
    else:
        print("  No se encontraron notificaciones de Twitter con la palabra 'Python'.")
    
    print("  Cola después de mostrar notificaciones (datos intactos):")
    q.show()
    print("-" * 50)


def contar_notificaciones(q: Queue):
    # c. Utiliza una pila para almacenar temporalmente las notificaciones
    # producidas entre las 11:43 y las 15:57, y determina cuántas son.
    print("\n--- Resolviendo punto c: Contar notificaciones entre 11:43 y 15:57 ---")
    
    temp_stack = Stack()
    original_size = q.size()
    
    # definir el rango de tiempo
    start_time_str = "11:43"
    end_time_str = "15:57"
    
    notifications_in_range_count = 0

    # recorrer cola, almacenar en la pila y volver a encolar
    for _ in range(original_size):
        notification = q.attention()
        if start_time_str <= notification.hour <= end_time_str:
            temp_stack.push(notification)
            notifications_in_range_count += 1
        q.arrive(notification)

    print(f"  Cantidad de notificaciones entre {start_time_str} y {end_time_str}: {notifications_in_range_count}")
    
    if notifications_in_range_count > 0:
        print("  Notificaciones almacenadas temporalmente en la pila (vacía la pila al mostrar):")
        # mostrar las notificaciones de la pila
        while temp_stack.size() > 0:
            print(f"  - {temp_stack.pop()}")
    else:
        print("  No se encontraron notificaciones en el rango especificado.")
    
    print("  Cola después de procesar el punto c (datos intactos):")
    q.show()
    print("-" * 50)


# ejecucion
if __name__ == "__main__":
    eliminar_notificaciones_facebook(notifications_queue)
    twitter_python(notifications_queue)
    contar_notificaciones(notifications_queue) 

    print("\n--- Estado final de la cola de notificaciones ---")
    notifications_queue.show()
