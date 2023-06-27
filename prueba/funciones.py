import numpy
import os
import time
import msvcrt
guarderia = numpy.zeros((2,5), int)

lista_rut = []
lista_nom_dueño = []
lista_id_unico = []
lista_nom_mascota =[]
lista_cantidad_dias = []
lista_habitacion = []


def mostrar_menú():
    os.system('cls')
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in (1,2,3,4):
                return opcion
            else:
                print("Debe ingresar una opción válida!")
            
        except:
            print("ERROR! debeingresar un número entero!")

def id_unico():
    contador = 1
    print(contador)
    contador +=1


        
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("Debe ingresar rut sin puntos ni dígito verificador!")
            
        except:
            print("ERROR! debe ingresar un número entero!")
        
def validar_nombre(nombre):
    while True:
        nombre = input(f"Ingrese nombre de {nombre}: ")
        if len(nombre.strip())>= 3 and nombre.isalpha():
            return nombre
        else:
            print("El nombre debe tener al menos 3 caracteres! ")
    
def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de días que se alojará su mascota: "))
            if cantidad >=1:
                return cantidad
            else:
                print("Debe ingresar una cantidad  positiva!")        
        except:
            print("ERROR! debe ingresar un número entero!") 
            
def habitacion_elegida():
    while True:
        try:
            habitacion = int(input("Ingrese habitación: "))
            if habitacion>=1 and habitacion<=10:
                return habitacion
            else:
                print("Debe ingresar una cantidad entre 1 y 10!")
        except:
            print("ERROR! debe ingresar un número entero!")

def grabar():
    rut = validar_rut()
    lista_rut.append(rut)
    nombre_dueño = validar_nombre("dueño")
    nombre_mascota = validar_nombre("mascota")
    cantidad_dias = validar_cantidad()
    print("Habitaciones:\n ")
    contador = 1
    for x in range(2):
        print(f"Fila {x+1}\t",end="")
        for y in range(5):
            print(f"habitacion {contador}:",guarderia[x][y], end=" ")
            contador +=1
        print()

    habitacion = habitacion_elegida()
    if guarderia[x][y] == 0:
        guarderia[x][y]=1
        print("Habitacion elegida exitosamente!")
        print("PRESIONE UNA TECLA PARA CONTINUAR...")
        msvcrt.getch()
    else:
        print("Habitacion ocupada! eliga otra")

    lista_nom_dueño.append(nombre_dueño)
    lista_nom_mascota.append(nombre_mascota)
    lista_cantidad_dias.append(cantidad_dias)
    lista_id_unico.append(id_unico)
    lista_habitacion.append(habitacion)

def buscar():
    habitacion = lista_habitacion
    rut = validar_rut()
    if rut in lista_rut:
        for x in range(2):
            for y in range(5):
                if guarderia[x][y] == habitacion:
                    lista_rut.append(rut)
                    lista_habitacion.append(habitacion)
                    print("su habitacion es: ",lista_habitacion)               
    else:
        print("El rut no se encuentra registrado!")
    print("PRESIONE UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

def retirarse():
    dia = 15000
    cantidad_dias = lista_cantidad_dias
    rut = validar_rut()
    if rut in lista_rut:
        for x in range(2):
            for y in range(5):
                guarderia[x][y]
                lista_rut.append(rut)
                total = dia*cantidad_dias
                print("Su total a pagar es $: ",total)
    else:
        print("Su mascota no fue registrada")
   

def salir():
    print("SALIDA")




        



        
  