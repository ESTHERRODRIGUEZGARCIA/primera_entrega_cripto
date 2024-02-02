def cifrar_palabra(palabra):
    # Definir el mapeo de letras
    mapeo = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
             'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
             'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
             's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
             'y': 'b', 'z': 'a'}

    # Convertir la palabra a minúsculas para asegurar correspondencia
    palabra = palabra.lower()

    # Cifrar la palabra letra por letra
    palabra_cifrada = ''.join(mapeo[letra] if letra in mapeo else letra for letra in palabra)

    return palabra_cifrada

# Ejemplo de uso
palabra_original = "GSVUOZTRHHZBDVZIVXIZAB"
palabra_cifrada = cifrar_palabra(palabra_original)
print(f"Palabra original: {palabra_original}")
print(f"Palabra cifrada: {palabra_cifrada}")