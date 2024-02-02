def atbash_cifrar(palabra):
    # Definir el tamaño del alfabeto
    N = 26
    
    # Convertir la palabra a minúsculas para asegurar correspondencia
    palabra = palabra.lower()

    # Función de cifrado Atbash
    palabra_cifrada = ''.join(chr((N - 1) - ord(letra) + 2 * ord('a')) if 'a' <= letra <= 'z' else letra for letra in palabra)

    return palabra_cifrada

def atbash_descifrar(palabra_cifrada):
    # Llamar a la función de cifrado para descifrar, ya que Atbash es su propia inversa
    return atbash_cifrar(palabra_cifrada)

# Ejemplo de uso
palabra_original = "GSVUOZTRHHZBDVZIVXIZAB"
palabra_cifrada = atbash_cifrar(palabra_original)
print(f"Palabra original: {palabra_original}")
print(f"Palabra cifrada: {palabra_cifrada}")

# Descifrar la palabra
palabra_descifrada = atbash_descifrar(palabra_cifrada)
print(f"Palabra descifrada: {palabra_descifrada}")
