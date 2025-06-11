# 1 VARIABLES GLOBALES
# Definimos listas globales asi podemos acceder a los datos desde cualquier parte del programa, puse admin primero porque el profe dijo que todos los sistemas tienen una asi
import random
usuarios = ["admin", "Luciana", "Thiago", "Yanina", "Emiliano", "Franco"]
contrasenias = ["admin", "uade2426", "santodomingo", "yanina1234", "soylider20", "messi10"]

# Listas paralelas para los tickets
identificadores = [1234, 2345, 3456, 4567, 5678]
descripciones = [
    "No enciende la computadora",
    "La computadora está infectada con un virus",
    "Problema con la impresora",
    "Error de red WiFi",
    "Pantalla azul al iniciar"
]
tecnicos = ["TEC123", "ABC456", "XYZ789", "JKL321", "DEF654"]
prioridades = [1, 2, 3, 1, 2]  # 1 = alta 2 = media 3 = baja

# 2 FUNCION DE LOGIN

# Esta funcion valida el acceso del usuario, se va a repetir hasta que se ingresen usuario y contraseña validos

def login():
    print("Bienvenido al sistema de soporte técnico.")

    usuario_incorrecto = True  # Mientras sea True, seguimos pidiendo datos

    while usuario_incorrecto:
        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        i = 0
        encontrado = False  # Sirve para verificar si existe el usuario y contraseña correctos

        while i < len(usuarios):
            if usuario == usuarios[i] and contrasenia == contrasenias[i]:
                encontrado = True  # Si lo encontramos, marcamos True
            i = i + 1  

        if encontrado:
            usuario_incorrecto = False  # Salimos del login si estaba bien
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")

# 3 FUNCION PARA MOSTRAR EL MENU Y VALIDAR LA OPCION

def mostrar_menu():
    print("\n--- Menú principal ---")
    print("1. Alta de ticket")
    print("2. Baja de ticket")
    print("3. Modificación de ticket")
    print("4. Listado general")
    print("0. Salir del sistema")

    opcion = -1 # Valor inicial invalido para entrar al ciclo de validacion
    # Inicializamos "opcion" con -1 para que la variable exista antes del ciclo "while"
    # Esto evita errores porque en thonny se puede usar una variable no definida en una condicion
    # -1 no es una opción valida del menu (que va de 0 a 4), asi que garantiza que el ciclo "while" se ejecute al menos una vez para pedir la opcion al usuario
    # Si no ponemos "opcion" cuando hagamos "while opcion < 0 or opcion > 4:" nos va a salir error xq la variable no esta definida
    # Elegimos un valor fuera del rango valido para asegurarnos que pida una opcion valida antes de continuar

    while opcion < 0 or opcion > 4: # Por si acaso, si el usuario escribe algo que no sea un numero el programa se va a romper pero el profe dijo que eso no importa porque esto lo vemos mas adelante
        opcion = int(input("Ingrese una opción del menú para proseguir (0-4): "))
        if opcion < 0 or opcion > 4:
            print("Opción inválida. Debe estar entre 0 y 4.")

    return opcion

# 4 ALTA DE TICKET

def alta_ticket():
    print("\n--- Alta de nuevo ticket ---")
    descripcion = input("Ingrese descripción del problema: ")
    print("Técnicos válidos: TEC123, ABC456, XYZ789, JKL321, DEF654")
    tecnico_valido = 1  # esta variable sirve para saber si el tecnico ingresado es valido o no. Empezamos con 0 (osea: todavia no es valido)
    while tecnico_valido == 1: # mientras que el tecnico NO sea valido (osea, mientras sea 0), vamos a seguir pidiendo uno
        tecnico = input("Ingrese el código del técnico asignado: ") # pedimos que escriba el codigo del tecnico
        tecnico_valido = numerorepetido(tecnicos, tecnico)
        # contador = 0 # creamos una variable para contar desde el principio de la lista de tecnicos validos
        # while contador < len(tecnicos): # mientras el contador no llegue al final de la lista:
        #     if tecnico == tecnicos[contador]: # si el codigo que ingreso es igual a uno de los tecnicos de la lista pasa esto:
        #         tecnico_valido = 1 # entonces el tecnico es valido POR LO TANTO cambiamos a 1 para salir del ciclo
        #     contador = contador + 1 # aumentamos el contador en 1 para revisar el siguiente tecnico en la lista
        if tecnico_valido == 1:  # cuando termina de recorrer la lista, si todavia no encontro ningun tecnico igual pasa esto
            print("Técnico inválido. Intente de nuevo.")

    prioridad = 0
    while prioridad != 1 and prioridad != 2 and prioridad != 3:
        prioridad = int(input("Ingrese la prioridad del ticket (1=Alta, 2=Media, 3=Baja): "))
        if prioridad != 1 and prioridad != 2 and prioridad != 3:
            print("Prioridad inválida. Debe ser 1, 2 o 3.")

# Generamos un numero random entre 1000 y 9999
    numeroRandom = random.randint(1000, 9999)
    repetido = numerorepetido(identificadores, numeroRandom)
    while repetido == 1:
            numeroRandom = random.randint(1000, 9999)
            repetido = numerorepetido(identificadores, numeroRandom)
# Inicializamos la variable para repetir si es necesario
    #repetido = 1  # Supongamos que esta repetido para entrar al while

# Mientras el numero este repetido, generamos otro
    # while repetido == 1:
    #     repetido = 0  # Suponemos que no esta repetido
    #
    #     contador = 0  # Empezamos a buscar desde el principio de la lista
    #     while contador < len(identificadores):
    #         if numeroRandom == identificadores[contador]:
    #             repetido = 1  # Si lo encontramos repetido, lo marcamos
    #         contador = contador + 1
    

    # Si estaba repetido, generamos uno nuevo para volver a verificar
    

    nuevo_id = numeroRandom  # Lo usamos como identificador final

    identificadores.append(nuevo_id)
    descripciones.append(descripcion)
    tecnicos.append(tecnico)
    prioridades.append(prioridad)

    print("\nSe creó el siguiente ticket:")
    print("ID:", nuevo_id)
    print("Descripción:", descripcion)
    print("Técnico:", tecnico)
    print("Prioridad:", prioridad)

def numerorepetido(lista, numero):
    repetido = 1
    
    while repetido == 1:
        repetido = 0
        contador = 0
        while contador < len(lista):
            if numero == lista[contador]:
                repetido = 1
                contador = len(lista)
            else:
                contador = contador + 1

    return repetido   

# 5 BAJA DE TICKET

def baja_ticket():
    print("\n--- Baja de ticket ---")
    posicion = -1
     # Repetimos hasta que se encuentre un id valido
    while posicion == -1:
        id_borrar = int(input("Ingrese el identificador del ticket a eliminar: "))

        contador = 0
        posicion = -1  # reiniciamos por si el anterior intento fue invalido
        while contador < len(identificadores):
            if identificadores[contador] == id_borrar:
                posicion = contador  # Guardamos la posicion si lo encontramos
            contador = contador + 1

        if posicion == -1:
            print("El identificador no existe. Intente nuevamente.")
        
        confirmacion = 0  # El profe en el ejemplo q hizo dijo que queda bien preguntar si esta seguro de borrar el dato entonces lo agregamos
        while confirmacion != 1 and confirmacion != 2: #es mejor usar while en vez del if porque si la opcion no es 1 ni 2 nosotros NO queremos seguir con el programa, tiene q pedir que de una opcion valida
            print("¿Está seguro que desea eliminar el ticket?")
            print("1. Sí")
            print("2. No")
            confirmacion = int(input("Ingrese una opción (1 para sí o 2 para no): "))
            if confirmacion != 1 and confirmacion != 2: #porque si elige un numero que no es ni 1 ni 2 avisamos que es incorrecto
                print("Opción inválida. Ingrese 1 para sí o 2 para no.")

        if confirmacion == 1:
             # Eliminamos el ticket en todas las listas paralelas
            identificadores.pop(posicion)
            descripciones.pop(posicion)
            tecnicos.pop(posicion)
            prioridades.pop(posicion)
            print("Ticket eliminado correctamente.")
        else:
            print("Eliminación cancelada.")

# 6 MODIFICACIÓN DE TICKET

def modificar_ticket():
    print("\n--- Modificación de ticket ---")
    posicion = -1

    # repetimos hasta que se ingrese un id que exista
    while posicion == -1:
        id_modificar = int(input("Ingrese el identificador del ticket a modificar: "))

        contador = 0
        posicion = -1  # reiniciamos cada vez que vuelve a pedir
        while contador < len(identificadores):
            if identificadores[contador] == id_modificar:
                posicion = contador
            contador = contador + 1

        if posicion == -1:
            print("El identificador no existe. Intente nuevamente.")


    # Mostramos opciones para modificar
        print("1. Modificar descripción")
        print("2. Modificar técnico")
        print("3. Modificar prioridad")
        opcion = int(input("¿Qué desea modificar? (1-3): ")) #

        if opcion == 1:
            nueva_desc = input("Ingrese nueva descripción: ")
            descripciones[posicion] = nueva_desc
            print("Descripción actualizada.")
        elif opcion == 2:
            print("Técnicos válidos: TEC123, ABC456, XYZ789, JKL321, DEF654")
            tecnico_valido = 0
            while tecnico_valido == 0:
                nuevo_tec = input("Ingrese nuevo código de técnico: ")
                contador = 0
                tecnico_valido = 0
                while contador < len(tecnicos) and tecnico_valido == 0:
                    if nuevo_tec == tecnicos[contador]:
                        tecnico_valido = 1
                    contador = contador + 1
                if tecnico_valido == 0:
                    print("Técnico inválido. Intente de nuevo.")
            tecnicos[posicion] = nuevo_tec
            print("Técnico actualizado.")
# Si el usuario elige la opcion 2, quiere modificar el tecnico asignado a un ticket
# 1ro mostramos cuales son los codigos validos que puede usar, por eso el print de tecnicos validos
# Despues entramos a un ciclo (while tecnico_valido == 0:) que se repite hasta que ingrese un codigo correcto
# recorremos la lista de tecnicos y comparamos uno por uno con el valor que ingreso
# si no coincide con ninguno, se vuelve a pedir
# cuando se encuentra uno valido, se actualiza el valor en la lista de tecnicos y se avisa que se modifico 
            
        elif opcion == 3:
            nueva_prio = 0
            while nueva_prio != 1 and nueva_prio != 2 and nueva_prio != 3:
                nueva_prio = int(input("Ingrese nueva prioridad (1=Alta, 2=Media, 3=Baja): "))
                if nueva_prio != 1 and nueva_prio != 2 and nueva_prio != 3:
                    print("Prioridad inválida.")
                else:
                    prioridades[posicion] = nueva_prio #Modificado por Thiago
                    print("Prioridad actualizada.")
        else:
            print("Opción inválida.")

# 7 LISTADO GENERAL DE TICKETS

def listado_general():
    print("\n--- Listado general de tickets (ordenados por prioridad) ---")

    # Guardamos la cantidad de tickets (todas las listas tienen la misma longitud)
    largo = len(prioridades)

    # Ordenamos las listas paralelas usando el metodo de SELECCION
    # Recorremos desde la primera posicion hasta la penultima
    for i in range(largo - 1):

        # En cada paso, comparamos el ticket actual con todos los siguientes
        for j in range(i + 1, largo):

            # Si la prioridad en la posicion i es mayor que en la j, intercambiamos todo
            # Esto es porque queremos que 1 (alta) este antes que 2 o 3 (mas baja)
            if prioridades[i] > prioridades[j]:

                # Intercambiamos los valores de prioridad
                aux = prioridades[i]
                prioridades[i] = prioridades[j]
                prioridades[j] = aux

                # Intercambiamos los identificadores correspondientes
                aux = identificadores[i]
                identificadores[i] = identificadores[j]
                identificadores[j] = aux

                # Intercambiamos las descripciones correspondientes
                aux = descripciones[i]
                descripciones[i] = descripciones[j]
                descripciones[j] = aux

                # Intercambiamos los tecnicos correspondientes
                aux = tecnicos[i]
                tecnicos[i] = tecnicos[j]
                tecnicos[j] = aux

    # Ya estan ordenadas todas las listas por prioridad (de menor a mayor)
    # Ahora mostramos los tickets uno por uno

    i = 0  # Usamos una variable 'i' para recorrer las listas desde el inicio

    # Recorremos todas las posiciones de las listas paralelas
    while i < len(identificadores):  # El largo es el mismo para todas las listas

        # Mostramos el identificador del ticket en la posicion 'i'
        print("ID:", identificadores[i])

        # Mostramos la descripcion del problema en esa misma posicion
        print("Descripción:", descripciones[i])

        # Mostramos el codigo del tecnico asignado
        print("Técnico asignado:", tecnicos[i])

        # Mostramos la prioridad (1 = alta, 2 = media, 3 = baja)
        print("Prioridad:", prioridades[i])

        print("---------------------------")

        # Sumamos 1 a 'i' para pasar al siguiente ticket
        i = i + 1
        
# 8 PROGRAMA PRINCIPAL
# Primero pedimos login al usuario
login()
# Inicializamos opcion con -1 para evitar error de variable no definida antes de entrar al while
opcion = -1
# mostramos el menu mientras el usuario no elija salir (osea la opcion 0)
while opcion != 0:
    opcion = mostrar_menu()

    if opcion == 1:
        alta_ticket()
    elif opcion == 2:
        baja_ticket()
    elif opcion == 3:
        modificar_ticket()
    elif opcion == 4:
        listado_general()

print("Gracias por usar el sistema. Fin.")

