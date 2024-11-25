def mismos_caracteres(lista):
    resultado = []
    for palabra in lista:
        if sorted(palabra) == sorted(lista[0]):
            resultado.append(palabra)
    return resultado

# Se solicita la lista de palabras

palabras = input("Introduce una lista de palabras separadas por espacios: ")
lista_palabras = palabras.split()

# Llama a la función y muestra las palabras con los mismos caracteres

print("Palabras con los mismos caracteres:", mismos_caracteres(lista_palabras))
