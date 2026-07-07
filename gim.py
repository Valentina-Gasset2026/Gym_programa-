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
 
nombre_plan = validar_nombre_plan()


planes = {   
        "nombre_plan":,
        "tipo": ,
        "duracion_meses":,
        "acceso_piscina":,
        "incluye_clases": ,
        "horario": ,
    }

def busqueda_precio(p_min, p_max):
    p_min = int("Ingrese precio mínimo: ")
    p_max = int("Ingrese precio máximo: ")
    validar_precios_planes = False
    while not validar_precios_planes:
        try:
            if p_min >=0 and p_max >=0:
                if p_min <= p_max:
                    validar_precios_planes = True
                    break
                else:
                    print("Error: El precio minimo debe de ser menor o igual al precio maximo")
            else:
                print("Error: El precio minimo y maxiomo deben de ser mayot a 0")
        except ValueError:
            print("Error: Ingrese un dato válido")
    
    #for valor_plan in inscripciones:


inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}

    




activo = False
while not activo:
    menu_principal()
    opcion = leer_opcion()
    if opcion == 1:
        print("nsj")
    else:
        #Salida
        print("Programa finalizado.")
        activo = True


#planes es un diccionario 
#

#Actualizar repositorio
#git branch -M main
#$ git push -u origin main