#programa para pedir correo electronico y el telefono
import libreria

max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Alumno")
    print("2: Docente")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.alumno()
    if(opc==2):
        libreria.docente()

    if (opc==3):

        if (libreria.mostrar_datos("Submenu2.txt")!=""):
            print(libreria.mostrar_datos("Submenu2.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu2.txt","","w")
