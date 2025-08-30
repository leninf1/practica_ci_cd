from operaciones import sumar

def menu():
    print("=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("👋 Saliendo de la calculadora...")
        break
        
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("⚠️ Entrada inválida. Intenta de nuevo.")
        continue
    
    if opcion == "1":
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        print("No implementado")
    elif opcion == "3":
        print("No implementado")
    elif opcion == "4":
        print("No implementado")
    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")