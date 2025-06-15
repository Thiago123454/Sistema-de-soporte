# VARIABLES GLOBALES
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
#Listas paralelas para los tecnicos
legajos = ["TEC123", "ABC456", "XYZ789", "JKL321", "DEF654"]
nombres = ["Luciano", "Tatiana", "Yamil", "Emilia", "Francisca"]
estado = ["Activo", "Activo", "Activo", "Activo", "Activo"]

#  FUNCION DE LOGIN
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

#  FUNCION PARA MOSTRAR EL MENU Y VALIDAR LA OPCION
def mostrar_menu():
    print("\n--- Menú principal ---")
    print("1. Alta de ticket")
    print("2. Baja de ticket")
    print("3. Modificación de ticket")
    print("4. Listado general por prioridad")
    print("5. Alta de tecnico")
    print("6. Modificacion de tecnicos")
    print("7. Baja de tecnicos")
    print("8. Cantidad de casos por tecnico")
    print("0. Salir del sistema")

    opcion = -1 

    while opcion < 0 or opcion > 8: 
        opcion = int(input("Ingrese una opción del menú para proseguir (0-8): "))
        if opcion < 0 or opcion > 8:
            print("Opción inválida. Debe estar entre 0 y 8.")

    return opcion

#  ALTA DE TICKET

def alta_ticket():
    print("\n--- Alta de nuevo ticket ---")
    descripcion = input("Ingrese descripción del problema: ")
    tecnico_valido = -1  
    while tecnico_valido == -1: 
        tecnico = input("Ingrese el código del técnico asignado: ") 
        tecnico_valido = validacion(legajos, tecnico)
        if tecnico_valido == -1:  
            print()
            print("Técnico invalido. Intentelo de nuevo")
        else:
            if estado[tecnico_valido] == "Inactivo":
                print("Tecnico dado de baja, escoja otro tecnico")
                tecnico_valido = -1
            
    prioridad = 0
    while prioridad != 1 and prioridad != 2 and prioridad != 3:
        prioridad = int(input("Ingrese la prioridad del ticket (1=Alta, 2=Media, 3=Baja): "))
        if prioridad != 1 and prioridad != 2 and prioridad != 3:
            print("Prioridad inválida. Debe ser 1, 2 o 3.")
            print()

# Generamos un numero random entre 1000 y 9999
    numeroRandom = random.randint(1000, 9999)
    repetido = validacion(identificadores, numeroRandom)
    while repetido != -1:
            numeroRandom = random.randint(1000, 9999)
            repetido = validacion(identificadores, numeroRandom)
    nuevo_id = numeroRandom  # Lo usamos como identificador final
    print(nuevo_id)

    identificadores.append(nuevo_id)
    descripciones.append(descripcion)
    tecnicos.append(tecnico)
    prioridades.append(prioridad)

    print("\nSe creó el siguiente ticket:")
    print("ID:", nuevo_id)
    print("Descripción:", descripcion)
    print("Técnico:", tecnico)
    print("Prioridad:", prioridad)

# BUSQUEDA SECUENCIAL
def validacion(lista, numero): 
    i = 0
    while i < len(lista) and lista[i] != numero:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1  

# BAJA DE TICKET

def baja_ticket():
    print("\n--- Baja de ticket ---")
    id_correcto = -1
    while id_correcto == -1:
        id_borrar = int(input("Ingrese el identificador del ticket a eliminar: "))
        id_correcto = validacion(identificadores, id_borrar)
        if id_correcto == -1:
            print("El identificador no existe. Intente nuevamente.")
        else:
            posicion = id_correcto
        
        confirmacion = 0  
    while confirmacion != 1 and confirmacion != 2: 
        print("¿Está seguro que desea eliminar el ticket?")
        print("1. Sí")
        print("2. No")
        confirmacion = int(input("Ingrese una opción (1 para sí o 2 para no): "))
        if confirmacion != 1 and confirmacion != 2: 
                print("Opción inválida. Ingrese 1 para sí o 2 para no.")

        if confirmacion == 1:
            identificadores.pop(posicion)
            descripciones.pop(posicion)
            tecnicos.pop(posicion)
            prioridades.pop(posicion)
            print("Ticket eliminado correctamente.")
        else:
            print("Eliminación cancelada.")



#  MODIFICACIÓN DE TICKET

def modificar_ticket():
    print("\n--- Modificación de ticket ---")
    print(identificadores)
    print(tecnicos)
    posicion = -1

    while posicion == -1:
        id_modificar = int(input("Ingrese el identificador del ticket a modificar: "))
        posicion = validacion(identificadores, id_modificar)
        if posicion == -1:
            print("El identificador no existe. Intente nuevamente.")

    print("1. Modificar descripción")
    print("2. Modificar técnico")
    print("3. Modificar prioridad")
    opcion = int(input("¿Qué desea modificar? (1-3): ")) #

    if opcion == 1:
        nueva_desc = input("Ingrese nueva descripción: ")
        descripciones[posicion] = nueva_desc
        print("Descripción actualizada.")
    elif opcion == 2:
        print(identificadores)
        print(descripciones)
        print(tecnicos)
        tecnico_valido = -1
        while tecnico_valido == -1:
            nuevo_tec = input("Ingrese nuevo código de técnico: ")
            tecnico_valido = validacion(legajos, nuevo_tec)
            if tecnico_valido == -1:
                print("Técnico inválido. Intente de nuevo.")
            else:
                if estado[tecnico_valido] == "Inactivo":
                    print("Tecnico dado de baja, escoja otro tecnico")
                    tecnico_valido = -1
                
                    

        tecnicos[posicion] = nuevo_tec
        print("Técnico actualizado.")
            
    elif opcion == 3:
        nueva_prio = 0
        while nueva_prio != 1 and nueva_prio != 2 and nueva_prio != 3:
            nueva_prio = int(input("Ingrese nueva prioridad (1=Alta, 2=Media, 3=Baja): "))
            if nueva_prio != 1 and nueva_prio != 2 and nueva_prio != 3:
                print("Prioridad inválida.")
            else:
                prioridades[posicion] = nueva_prio
                print("Prioridad actualizada.")
    else:
        print("Opción inválida.")

#  LISTADO GENERAL DE TICKETS

def listado_general():
    print("\n--- Listado general de tickets (ordenados por prioridad) ---")

    largo = len(prioridades)

    # Ordenamos las listas paralelas usando el metodo de SELECCION por prioridad
    for i in range(largo - 1):

        for j in range(i + 1, largo):

            if prioridades[i] > prioridades[j]:

                aux = prioridades[i]
                prioridades[i] = prioridades[j]
                prioridades[j] = aux

                aux = identificadores[i]
                identificadores[i] = identificadores[j]
                identificadores[j] = aux

                aux = descripciones[i]
                descripciones[i] = descripciones[j]
                descripciones[j] = aux

                aux = tecnicos[i]
                tecnicos[i] = tecnicos[j]
                tecnicos[j] = aux

    # Ya estan ordenadas todas las listas por prioridad (de menor a mayor)

    i = 0  

    while i < len(identificadores):  

     
        print("ID:", identificadores[i])

      
        print("Descripción:", descripciones[i])

       
        print("Técnico asignado:", tecnicos[i])

        # Mostramos la prioridad (1 = alta, 2 = media, 3 = baja)
        print("Prioridad:", prioridades[i])

        print("---------------------------")

        i = i + 1

# ALTA DE TECNICO
def alta_tecnico():
    print("\n--- Alta de nuevo tecnico ---")
    nombre_nuevo = input("Ingrese el nombre del nuevo tecnico: ")
    nombres.append(nombre_nuevo)
    print(nombres)
    codigo_valido = -2
    while codigo_valido != -1:
        codigo = input("Ingrese el código del tecnico (debe incluir 3 letras y 3 números. Ej TEC123): ")
        codigo_valido = validacion(legajos, codigo)
        if codigo_valido != -1:
            print("El código de tecnico ya está en la lista. Intentelo de nuevo.")
        else:
            legajos.append(codigo)
            estado.append("Activo")
    print("\nLista de tecnicos actualizada:")
    print("Legajos:", legajos)
    print("Nombres:", nombres)
#  MODIFICACION DE TECNICO
def modificacion_tecnico():
    print("\n--- Modificacion de tecnico ya existente---")
    tecnico_valido = -1
    while tecnico_valido == -1:
        tecnico_a_modificar = input("Ingrese el código del tecnico que quiere modificar: ")
        tecnico_valido = validacion(legajos, tecnico_a_modificar)
        if tecnico_valido == -1:
            print("Tecnico a modificar inexistente. Intente de nuevo.")
        else:
            posicion_tecnico_en_legajos = tecnico_valido
            nombre_nuevo = input("Ingrese el nombre nuevo a reemplazar: ")
            nombres[posicion_tecnico_en_legajos] = nombre_nuevo
    print("\nLista de tecnicos actualizada:")
    print("Legajos:", legajos)
    print("Nombres:", nombres)      
#  BAJA DE TECNICO
def baja_tecnico():
    print("\n--- Baja de tecnico ---")
    legajo_correcto = -1
    while legajo_correcto == -1:
        legajo_borrar = input("Ingrese el código del tecnico a eliminar: ")
        legajo_correcto = validacion(legajos, legajo_borrar)
        if legajo_correcto == -1:
            print("El código del tecnico no existe. Intente nuevamente.")
        else:
            posicion = legajo_correcto
            inactivo = "Inactivo"
            estado[posicion] = inactivo

# Funciones para la MATRIZ que cuenta la cantidad de casos por técnico 

def listas_matriz(identificadores, tecnicos):
    matriz = []
    filas_matriz = len(identificadores)
    for i in range(filas_matriz):
        fila = []
        fila.append(identificadores[i])
        fila.append(tecnicos[i])
        matriz.append(fila)
    return matriz
def conservar_unicos(matriz):
    unicos = []
    for i in range(len(matriz)):
        tecnico = matriz[i][1]
        if validacion(unicos, tecnico) == -1:
            unicos.append(tecnico)
    return unicos

def obtener_cantidad_categoria(tecnicos_totales, tecnico_buscado):
    cantidad = 0
    for i in range(len(tecnicos_totales)):
        if tecnicos_totales[i] == tecnico_buscado:
            cantidad = cantidad + 1
    return cantidad

def armar_matriz_estadisticas(tecnicos_unicos, tecnicos_totales):
    matriz_estadisticas = []
    i = 0
    while i < len(tecnicos_unicos):
        tecnico = tecnicos_unicos[i]
        cantidad = obtener_cantidad_categoria(tecnicos_totales, tecnico)
        fila = []
        fila.append(tecnico)
        fila.append(cantidad)
        matriz_estadisticas.append(fila)
        i = i + 1
    return matriz_estadisticas

def casos_por_tecnico(identificadores, tecnicos):
    matriz = listas_matriz(identificadores, tecnicos)
    tecnicos_unicos = conservar_unicos(matriz)
    tecnicos_totales = []
    for i in range(len(matriz)):
        tecnicos_totales.append(matriz[i][1])
    matriz_estadisticas = armar_matriz_estadisticas(tecnicos_unicos, tecnicos_totales)
    return matriz_estadisticas

def mostrar_casos_por_tecnico():
    print("\n--- Cantidad de casos por técnico ---")
    matriz = casos_por_tecnico(identificadores, tecnicos)
    for i in range(len(matriz)):
        print(f"Técnico: {matriz[i][0]:5} - Casos asignados: {matriz[i][1]:5}")
         
#  PROGRAMA PRINCIPAL
login()
opcion = -1
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
    elif opcion == 5:
        alta_tecnico()
    elif opcion == 6:
        modificacion_tecnico()
    elif opcion == 7:
        baja_tecnico()
    elif opcion == 8:
        mostrar_casos_por_tecnico()

print("Gracias por usar el sistema. Fin.")

