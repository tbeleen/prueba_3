import funciones as fn

while True:
    fn.mostrar_menú()
    opcion = fn.validar_opcion()
    if opcion==1:
        grabar = fn.grabar()
    elif opcion==2:
        buscar = fn.buscar()
    elif opcion==3:
        retirarse = fn.retirarse()
    else:
        salir = fn.salir()
        break


