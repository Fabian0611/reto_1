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
