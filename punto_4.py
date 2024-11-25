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
