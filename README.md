# Reto_1

### Primer Punto
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Se crea una funcion llamada "calculadora" en la que se definen las diferentes operaciones usando condicionales, luego se piden los valores de a y b respectivamente para al final imprimir el resultado.
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
