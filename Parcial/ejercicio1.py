def contar_palabra(palabra, vector):
    if len(vector) == 0:
        return 0
    if vector[0] == palabra:
        return 1 + contar_palabra(palabra, vector[1:])
    return contar_palabra(palabra, vector[1:])

vector = ["Buenas", "mundo", "Hola", "Hola", "adiós"]
palabra = "Hola"
resultado = contar_palabra(palabra, vector)
print(f"La palabra '{palabra}' aparece {resultado} veces en el vector.")
