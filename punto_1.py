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
