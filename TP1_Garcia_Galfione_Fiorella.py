# Ejercicio 1 #

print("Hola Mundo!")

# Ejercicio 2 #

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# Ejercicio 3 #

nombre = input(" Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Ejercicio 4 #

radio = input("Ingrese el valor del radio del círculo: ")
radio = float(radio)
area= 3.1416 * radio * radio
perimetro = 2*3.1416 * radio
print(f"El área del circulo es: {area} y el perímetro de mismo es: {perimetro}")

# Ejercicio 5 #

segundos = float(input("Ingrese la cantidad de segundos a convertir: "))
horas = segundos / 3600

print(f"El valor en horas de los segundos ingresados es: {horas} ")

# Ejercicio 6 #

numero = int(input("Ingrese el numero que desea saber su tabla de multiplicar: "))
print(f"La tabla de multiplicar del {numero}")

for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")

# Ejercicio 7 #

numero1=float(input("Ingrese el primer numero: "))

while numero1 == 0:
    print("El número no puede ser 0. Inténtalo de nuevo.")
    numero1 = float(input("Ingrese un número distinto de cero: "))

print(f"Has ingresado el número {numero1}.")

numero2=float(input("Ingrese el segundo numero: "))

while numero2 == 0:
    print("El número no puede ser 0. Inténtalo de nuevo.")
    numero2 = float(input("Ingrese un número distinto de cero: "))

print(f"Has ingresado el número {numero2}.")

suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

print(f"La suma de los dos numeros es: {suma}; la resta de ambos numeros es: {resta}; el producto de ambos numeros es: {multiplicacion}; y la division entre los numeros ingresados es: {division}")

# Ejercicio 8 #

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura*altura)

print(f"Su indice de masa corporal es: {IMC}")

# Ejercicio 9 #

Temp_celsius = float(input("Ingrese el valor de la temperatura en F a convertir: "))

Temp_Fahrenheit = 9/5 * Temp_celsius + 32

print(f"La temp en Fahrenheit es: {Temp_Fahrenheit}")

# Ejercicio 10 #

numero1 = float(input("Ingrese el numero 1: "))
numero2 = float(input("Ingrese el numero 2: "))
numero3 = float(input("Ingrese el numero 3: "))

promedio = (numero1+numero2+numero3)/3

print(f"El promedio de los tres numeros ingresados es: {promedio}")