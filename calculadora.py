# calculadora.py
def suma(a, b):
   return a + b
def resta(a, b):
   return a - b
def multiplicacion(a, b):
   return a * b
def division(a, b):
   try:
       return a / b
   except ZeroDivisionError:
       return "Error: División por cero."
def menu():
   print("\n--- Calculadora ---")
   print("1. Suma")
   print("2. Resta")
   print("3. Multiplicación")
   print("4. División")
   print("5. Salir")
   opcion = input("Seleccione una operación o '5' para salir: ")
   return opcion
def main():
   while True:
       opcion = menu()
       if opcion.isdigit():
           opcion = int(opcion)
           if opcion == 5:
               print("Saliendo del programa...")
               break
           elif opcion in [1, 2, 3, 4]:
               num1 = float(input("Ingrese el primer número: "))
               num2 = float(input("Ingrese el segundo número: "))
               operaciones = {
                   1: suma,
                   2: resta,
                   3: multiplicacion,
                   4: division
               }
               resultado = operaciones[opcion](num1, num2)
               print(f"El resultado es: {resultado}")
           else:
               print("Opción no válida. Por favor, intente de nuevo.")
       else:
           print("Por favor, ingrese un número válido.")
if __name__ == "__main__":
   main()
