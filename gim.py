def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    validar_opcion = False
    while not validar_opcion:
        try:
            opt = int(input("Ingrese opción: "))
            if opt >= 1 and opt <= 6:
                validar_opcion = True
            else:
                print("Error, ingrese una opción entre el 1 y el 6.")
        except ValueError:
            print("Error: Ingrese un dato válido.")
    return opt

def cupos_tipo(tipo):
    tipo_plan = input("Ingrese tipo de plan a consultar:").lower().title()
    


 #validacion de cada dato de planes

def validar_nombre_plan():
    validar_nombre = False
    while not validar_nombre:
        nombre_del_plan = input("Ingrese nombre del plan: ").lower().strip()
        if nombre_del_plan == "":
            print("No debe contener solo espacios en blanco ni estar vacío")
        else:
            validar_nombre = True
    return nombre_del_plan
 
nombre = validar_nombre_plan()

def validar_duración_meses():
    validar_duración = False
    while not validar_duración:
        try:
            duracion_meses = int(input("Ingrese duración (meses) : "))
            if duracion_meses > 0:
                validar_duración = True
            else:
                print("Error: Ingrese un numero mayor que 0")
        except ValueError:
            print("Debe ingresar valores enteros")
    return duracion_meses

duracion = validar_duración_meses()

def validación_acceso_piscina():
    validar_acceso = False
    while not validar_acceso:
        acceso = input("¿Incluye acceso a piscina? (s/n): ")
        if acceso == 's':
            acceso = True
        elif acceso == 'n':
            acceso = False
        else:
            print("Debe de ingresar s/n")
    return acceso

acceso_piscina = validación_acceso_piscina()

def validación_incluye_clases():
    validar_incluye_clases = False
    while not validar_incluye_clases:
        clases = input("¿Incluye acceso a piscina? (s/n): ")
        if clases == 's':
            clases = True
        elif clases == 'n':
            clases = False
        else:
            print("Debe de ingresar s/n")
    return clases

incluye_clases = validación_incluye_clases()

def validacion_horario():
    validar_horario = False
    while not validar_horario:
        horario_disponible = input("Ingrese nombre del plan: ").lower().strip()
        if horario_disponible == "":
            print("No debe contener solo espacios en blanco ni estar vacío")
        else:
            validar_horario = True
    return horario_disponible
 
horario = validacion_horario()

planes = [
         
    {   
        'codigo': ['nombre_plan', 'cupos_tipo', 'duracion', 'acceso_piscina', 'incluye_clases', 'horario'],
      
    }
]

def busqueda_precio(p_min, p_max):
    validar_precios_planes = False
    while not validar_precios_planes:
        try:
            p_min = int("Ingrese precio mínimo: ")
            p_max = int("Ingrese precio máximo: ")
            if p_min >=0 and p_max >=0:
                if p_min <= p_max:
                    validar_precios_planes = True
                    break
                else:
                    print("Error: El precio minimo debe de ser menor o igual al precio maximo")
            else:
                print("Error: El precio minimo y maxiomo deben de ser mayot a 0")
        except ValueError:
            print("Debe ingresar valores enteros")
    
    

    #for valor_plan in inscripciones:


inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}

    
def mostrar_codigo():
    validar_codigo = False
    while not validar_codigo:
        codigo_agregar = input("Ingrese codigo: ")
        if codigo_agregar == "" or codigo_agregar == " ":
            print("No vacío ni solo espacios en blanco")
        #agregar codigo repetido
        else:
            validar_codigo = True
            break
    return codigo_agregar

codigo = mostrar_codigo()

def validacion_cupos():
    validar_cupos = False
    while not validar_cupos:
        try:
            cantidad_cupos = int(input("Ingrese cupos: "))
            if cantidad_cupos >=0:
                validar_cupos = True
                break
            else:
                print("Ingrese un numero mayor o igual a 0")
        except ValueError:
            print("Ingrese un valor válido")
    return cantidad_cupos

cupos = validacion_cupos()

def validacion_precios():
    validar_precio = False
    while not validar_precio:
        try:
            precio_plan = int(input("Ingrese precio: "))
            if precio_plan > 0:
                validar_precio = True
                break
            else:
                print("Debe de ingresar un precio mayor a 0")
        except ValueError:
            print("Error: Ingrese un valor válido.")
    return precio_plan

precio = validacion_precios()

def agregar_plan(planes):
    
    
    


activo = False
while not activo:
    menu_principal()
    opcion = leer_opcion()
    if opcion == 1:
        
    else:
        #Salida
        print("Programa finalizado.")
        activo = True


#planes es un diccionario 
#

#Actualizar repositorio
#git branch -M main
#$ git push -u origin main