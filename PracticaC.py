#Practica
import os
import shutil

def crear_archivo():

    with open('mis notas.txt', 'w') as archivo:

        archivo.write('Este es el archivo de mis notas.')

def crear_carpeta_calificaciones():

    os.makedirs('calificaciones', exist_ok=True)

def crear_carpeta_primer_parcial():

    os.makedirs('calificaciones/primer parcial', exist_ok=True)

def mover_archivo_notas():

    shutil.move('mis notas.txt', 'calificaciones/')

def mover_calculadora():

    shutil.move('calculadora.py', 'calificaciones/primer parcial/')

def mostrar_menu():

    while True:

        print("\nMenú de opciones:")

        print("1. Crear archivo 'mis notas.txt'")

        print("2. Crear carpeta 'calificaciones'")

        print("3. Crear carpeta dentro de 'calificaciones' llamada 'primer parcial'")

        print("4. Mover el archivo 'mis notas.txt' a la carpeta 'calificaciones'")

        print("5. Mover el archivo 'calculadora.py' a la carpeta 'primer parcial'")

        print("6. Salir")

        opcion = input("Introduce el número de la opción deseada: ")

        if opcion == '1':

            crear_archivo()

            print("Archivo 'mis notas.txt' creado exitosamente.")

        elif opcion == '2':

            crear_carpeta_calificaciones()

            print("Carpeta 'calificaciones' creada exitosamente.")

        elif opcion == '3':

            crear_carpeta_primer_parcial()

            print("Carpeta 'primer parcial' dentro de 'calificaciones' creada exitosamente.")

        elif opcion == '4':

            mover_archivo_notas()

            print("Archivo 'mis notas.txt' movido a 'calificaciones' exitosamente.")

        elif opcion == '5':

            mover_calculadora()

            print("Archivo 'calculadora.py' movido a 'primer parcial' exitosamente.")

        elif opcion == '6':

            print("Saliendo del programa...")

            break

        else:

            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":

    mostrar_menu()
