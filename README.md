# 🧮 Calculadora en Python (Proyecto Modularizado)

Este proyecto es una **calculadora básica en Python**, diseñada de forma **modularizada** para demostrar buenas prácticas de organización de código.  
Permite realizar las operaciones fundamentales: **suma, resta, multiplicación y división**.  

---

## 📁 Estructura del proyecto
calculadora/
│── main.py # Programa principal
│── operaciones/ # Carpeta con los módulos de operaciones
│ ├── init.py # Inicializa el paquete y expone las funciones
│ ├── suma.py # Función para sumar
│ ├── resta.py # Función para restar
│ ├── multiplicacion.py # Función para multiplicar
│ └── division.py # Función para dividir

🖥️ Uso

El programa muestra un menú interactivo en consola:

=== Calculadora Básica ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir


Ejemplo:

Elige una opción: 1
Ingresa el primer número: 10
Ingresa el segundo número: 5
Resultado: 15.0

🧩 Modularización

Cada operación está separada en un archivo independiente dentro de la carpeta operaciones/.
Esto permite:

Código más limpio y fácil de mantener.

Reutilización de funciones en otros proyectos.

Escalabilidad (pueden añadirse nuevas operaciones fácilmente, como potencias o raíces).