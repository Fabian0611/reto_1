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

Se crea la función palindromo, luego se crea un ciclo en el cual se recorre cada letra verificando si su opuesta es igual o no, despues se pide la palabra a comprobrar y se imprime True or False segun el resultado
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
