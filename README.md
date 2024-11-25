# Reto_1

### Primer Punto
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Se crea una funcion llamada calculadora en la que se definen las diferentes operaciones usando condicionales, luego se piden los valores de a y b respectivamente para al final imprimir el resultado.
  ````python
def calculadora(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    else:
        return "Operador no válido"

# Se piden los valores de a y b respectivamente 

a= float(input("Ingrese un numero: "))
b= float(input("Ingrese otro numero: "))
operador= str(input("Ingrese el signo de la operación deseada: "))

# Se llama a la funcion y se imprime el resultado

resultado = calculadora(a, b, operador)
print(resultado)
````
### Segundo Punto
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

Se crea la función palindromo, luego se crea un ciclo en el cual se recorre cada letra verificando si su opuesta es igual o no, despues se pide la palabra a comprobrar y se imprime True or False segun el resultado.
  ````python
def palindromo(palabra):
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

# Se pide una palabra para comprobar si es o no palindromo

palabra= str(input("Ingrese la palabra que desea comprobar: "))

# Se llama a la función y se imprime el resultado

print(palindromo(palabra))
````
### Tercer Punto
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Primero se crea la funcion primo para saber si un numero es primo o no, mirando si el residuo de algun numero dentro del rango es igual a cero, lo que significaria que tiene un divisor lo cual lo convertiria en un numero no primo y retornaria False, despues se crea una funcion llamada filtrar_numeros la que retorna una sublista en la que pone a todos los numeros que devuelvan True en la funcion primo, por ultimo se pide la lista de numeros que va a ser analizada para luego imprimir la sublista con los numeros primos.
````python
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if primo(num)]

# Solicita la lista de números al usuario

numeros = input("Introduce una lista de números separados por espacios: ")
lista_numeros = [int(x) for x in numeros.split()]

# Llama a la función y muestra los números primos

print("Números primos:", filtrar_primos(lista_numeros))
````
### Cuarto Punto
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Primero se crea la funcion mayor_suma_consecutiva la cual toma los valores de lista que sean consecutivos y los va sumando y comparando hasta terminar con el mayor valor, luego se pide la lista de numeros que va a ser analizada para al final imprimir el valor de la mayor suma entre numeros consecutivos.
````python
def mayor_suma_consecutiva(lista):
    max_suma = float('-inf')
    for i in range(len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > max_suma:
            max_suma = suma_actual
    return max_suma

# Se solicita la lista de números

numeros = input("Introduce una lista de números separados por espacios: ")
lista_numeros = [int(x) for x in numeros.split()]

# Llama a la función y muestra la mayor suma consecutiva

print("La mayor suma entre elementos consecutivos es:", mayor_suma_consecutiva(lista_numeros))

````
### Quinto Punto



````python

````
