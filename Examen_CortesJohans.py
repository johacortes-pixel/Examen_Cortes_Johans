peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    
}

def buscar_codigo(codigo):
    for i in peliculas, cartelera:
        if (codigo.lower()) == (peliculas[i].lower()) and codigo == (cartelera[i].lower()):
            print("Codigo encontrado")
            buscar_codigo() == True
        else:
            print("Codigo no encontrado")
            buscar_codigo() == False
def leer_opcion():
    
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    try:
        opcion = int(input("Ingrese una opcion : "))
    except ValueError:
        print("Se esperaba un numero, intente de nuevo")
    
    if opcion >= 1 and opcion <= 6:
        match(opcion):
            
            case(1):
                cupos_genero()

                print("Debe de ingresar una opcion valida (1-6)")



#El sistema solicita al usuario el nombre de un género (por ejemplo: drama, acción o
#comedia). La búsqueda no distingue entre mayúsculas y minúsculas, por lo que
#"drama" y "DRAMA" deben producir el mismo resultado. El sistema recorre el
#diccionario películas identificando todas las películas que pertenezcan a ese género.
#Por cada película encontrada, se debe buscar su código en el diccionario cartelera,
#extraer la cantidad de cupos disponibles (el segundo elemento de la lista) y
#acumularla en un total. Una vez procesadas todas las películas, se debe mostrar
#dicho total acumulado en pantalla.
#4
#Para implementar esta opción:
#Define una función llamada cupos_genero(genero). Recibe el género como
#parámetro, no retorna ningún valor y muestra el resultado directamente por
#pantalla

#No debe contener solo
#espacios en blanco ni
#estar vacío

def cupos_genero(genero):
    genero = " "
    while genero == " " or genero == None:
        genero = input("Ingrese el genero que desea buscar (Drama, Accion, Docuental, Comedia, Thiller o Ciencia Ficcion)")
        if genero == " " or genero == None:
            print("La busqueda no puede estar vacia o contner solo espacios, intente de nuevo")
    for i in peliculas:
        if genero.lower() == peliculas[i][1]:
            print(peliculas[i])
genero = " "
while genero == " " or genero == None:
    genero = input("Ingrese el genero que desea buscar (Drama, Accion, Docuental, Comedia, Thiller o Ciencia Ficcion)")
    if genero == " " or genero == None:
        print("La busqueda no puede estar vacia o contner solo espacios, intente de nuevo")
for i in peliculas:
    if genero.lower() == peliculas[i][1]:
        print(peliculas[i])


#código	No vacío ni solo espacios en blanco, y que no exista ya en los diccionarios
#título	No vacío ni solo espacios en blanco
#género	No vacío ni solo espacios en blanco
#duración	Número entero mayor que cero
#clasificación	Debe ser exactamente 'A', 'B' o 'C'
#idioma	No vacío ni solo espacios en blanco
#es_3d	El usuario ingresa 's' o 'n'. El sistema almacena True si es 's', False si es 'n'
#precio	Número entero mayor que cero
#cupos	Número entero mayor o igual a cero


def agregar_pelicula():
    codigo = " "
    while codigo == " " or codigo == None or codigo == peliculas:
        codigo = input("Ingrese el codigo de la nueva pelicula: ")
        if codigo == " " or codigo == None:
            print("El codigo no puede tener solo espacios o estar vacio")
        for i in peliculas:
            if codigo == peliculas[i]:
                print("El codigo ya existe, intente con otro ")
                
    while titulo == " " or titulo == None:
        titulo = input("Ingrese el titulo de la pelicula: ")
        if titulo == " " or titulo == None:
            print("El texto no puede contener solo espacios o estar en blanco")
            
    while genero == " " or genero == None:
        genero = input("Ingrese el genero de la pelicula")
        genero_lower = genero.lower()
        if genero == " " or genero == None:
            print("El texto no puede contener solo espacios o estar en blanco")
            
    while duracion <= 0:
        duracion = int(input("Ingrese la duracion de la pelicula (Minutos): "))
        if duracion <= 0:
            print("Ingrese un numero mayor a 0: ")
    
    while clasificacion.title() != "A" or clasificacion.title() != "B" or clasificacion.title() != "C":
        clasificacion = str(input("Ingrese la clasificacion de la pelicula"))
        if clasificacion.title() != "A" or clasificacion.title() != "B" or clasificacion.title() != "C":
            print("Debe ingresar exclusivamente una de las tres opciones (A,B,C)")
    
    while idioma == " " or idioma == None:
        idioma = input("Ingrese el idioma de la pelicula")
        if idioma == " " or idioma == None:
            print("El texto no puede contener solo espacios o estar en blanco")
    
    while es_3d.lower() != "s" or es_3d.lower() != "n":
        es_3d = input("Ingrese si es 3D (s/n)")
        if es_3d.lower() == "s":
            es_3d = True
        elif es_3d.lower() == "n":
            es_3d = False
            
    while precio <= 0:
        precio = input("Ingrese el precio de la pelicula")
        if precio <= 0:
            print("Debe de ser un numero mayor o igual a 0")
    while cupos < 0:
        cupos = int(input("Ingrese los cupos de la pelicula"))
        if cupos < 0:
            print("Debe ingresar un numero mayor o igual a 0")
    
    peliculas[codigo] = [titulo,genero_lower,duracion,clasificacion,idioma,es_3d]
    cartelera[codigo] = [precio,cupos]

def finalizar_programa():
    print("Programa finalizado.")

def busqueda_precio(p_min,p_max):
    
    p_min = int(input("Ingrese el valor minimo"))
    p_max = int(input("Ingree el valor maximo"))

    for i in cartelera:
        if  cartelera[i][0] > p_min and cartelera[i][0] < p_max:
            print(f"Las peliculas dentro de este rago son: {peliculas[i][0], cartelera[i]}")


def eliminar_pelicula(codigo):
    codigo = input("Ingrese el codigo que desea buscar: ")
    buscar_codigo(codigo)
    if buscar_codigo(codigo) == True:
        print("La pelicula ha sido eliminada.")
        del cartelera[codigo]
        del peliculas[codigo]
    elif buscar_codigo(codigo) == False: 
        print("Codigo no encontrado")