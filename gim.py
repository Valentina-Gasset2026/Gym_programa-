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



activo = False
while not activo:
    menu_principal()
    opcion = leer_opcion()
    if opcion == 1:
        print("nsj")
    else:
        #Salida
        activo = True


#git branch -M main
#$ git push -u origin main