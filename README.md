# primera_entrega_cripto

El cifrado Atbash es una técnica de cifrado alfabético que se basa en la sustitución de letras. En este método, cada letra del alfabeto se reemplaza por su opuesta en la secuencia alfabética. Matemáticamente, para un alfabeto de tamaño \(N\), la función de cifrado Atbash se define como \(E_k(x) = (N - 1) - x\). En esta expresión, \(x\) representa el valor numérico de la letra original. La implementación en Python utiliza las funciones ord() y chr() para obtener y convertir los valores ASCII de las letras. La simplicidad del cifrado Atbash lo hace más ilustrativo que seguro, y su función de descifrado es idéntica al cifrado, lo que lo clasifica como un cifrado simétrico.

Explicación de la fórmula: 

Posiciones:

a=0, b=1, ..., z=25


E_k(x) es la posición de la letra que quieres cifrar, ej: a = 0

x es la posición de la letra cifrada original, ej: z = 25

N es la longitud del alfabeto, ej: 26 en el alfabeto sin ñ

