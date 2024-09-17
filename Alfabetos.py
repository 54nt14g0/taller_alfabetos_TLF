# Función para generar combinaciones de caracteres con una longitud específica
# y un número máximo de combinaciones
def combinar_caracteres(caracteres, longitud_deseada, limite):
    combinaciones = ['']  # Lista inicial con una cadena vacía para empezar las combinaciones

    # Bucle para generar combinaciones hasta alcanzar la longitud deseada
    for _ in range(longitud_deseada):
        nuevas_combinaciones = []  # Almacena las nuevas combinaciones generadas en cada iteración
        for combinacion in combinaciones:
            # Para cada combinación actual, se agregan caracteres del alfabeto
            for caracter in caracteres:
                if len(nuevas_combinaciones) >= limite:  # Si alcanzamos el límite de combinaciones, detenemos
                    break
                nuevas_combinaciones.append(combinacion + caracter)  # Añadimos el carácter a la combinación

        combinaciones = nuevas_combinaciones  # Actualizamos las combinaciones con las nuevas generadas

    return combinaciones  # Retornamos la lista de combinaciones generadas


# Función para verificar si una palabra está en el lenguaje generado
def verificarPalabra(lenguaje, palabra):
    if palabra in lenguaje:  # Verifica si la palabra está en la lista de lenguaje
        print("La palabra está en el lenguaje.")
    else:
        print("La palabra no está en el lenguaje.")

# función que verifica que se cumpan las reglas
def verificar_cadena(cadena, alfabeto, letra_inicial=None):
    # Regla 1: La cadena solo puede contener simbolos que estén en el alfabeto proporcionado
    for letra in cadena:
        if letra not in alfabeto:
            return False, f"La letra '{letra}' no pertenece al alfabeto."

    # Regla 2: La cadena debe comenzar con una letra específica (si se proporciona)
    if letra_inicial and cadena[0] != letra_inicial:
        return False, f"La cadena debe comenzar con la letra '{letra_inicial}'."

    # Regla 3: La cadena debe tener 2 letras repetidas al final
    if len(cadena) < 2 or cadena[-1] != cadena[-2]:
        return False, "La cadena debe tener 2 letras repetidas al final."

    return True, "La cadena es válida."


# Función para añadir un prefijo y un sufijo a todas las palabras del lenguaje generado
def prefijo_sufijo(lenguaje, sufijo, prefijo):
    lenguajeModificado = []  # Lista vacía para almacenar las palabras con prefijo y sufijo añadidos
    for palabra in lenguaje:
        lenguajeModificado.append(prefijo + palabra + sufijo)  # Se añaden el prefijo y sufijo a cada palabra
    return lenguajeModificado  # Retorna la lista modificada


# Función principal que ejecuta el programa
def main():
    # Primer punto: generar un lenguaje combinando caracteres con una longitud deseada
    print("Primer punto: Se generará un lenguaje combinando los símbolos ingresados.")
    caracteres = input("Ingrese el alfabeto, caracteres separados por comas (sin espacios): ")
    alfabeto = caracteres.split(',')  # Convertimos la entrada en una lista de caracteres
    longitudPalabras = int(input("Digite la longitud de palabra que desea: "))  # Longitud de las combinaciones
    limite = int(input("Digite la cantidad máxima de palabras que desea: "))  # Límite de combinaciones
    resultado = combinar_caracteres(alfabeto, longitudPalabras, limite)  # Generamos las combinaciones
    print(resultado)  # Imprimimos las combinaciones generadas
    print(f"Se generaron {len(resultado)} palabras.")  # Imprimimos cuántas palabras se generaron

    # Segundo punto: verificar si una palabra ingresada está en el lenguaje
    print("Segundo punto: Verificación de si una palabra está en el lenguaje generado.")
    palabra = input("Ingrese la palabra que desea verificar: ")  # Pedimos una palabra para verificar
    verificarPalabra(resultado, palabra)  # Verificamos si la palabra está en el lenguaje




    # Tercer punto: verificar si una palabra está en el lenguaje y si comienza con una letra específica
    alfabeto = set(input("Introduce el alfabeto permitido (sin espacios, por ejemplo: abcdefg): ").strip())
    
    # Se pide si debe haber letra inicial obligatoria
    letra_inicial = input("Introduce una letra inicial específica (o presiona Enter para omitir): ").strip()
    letra_inicial = letra_inicial if letra_inicial else None  # Convertir cadena vacía a None

    # se pide la cadena
    cadena = input("Introduce la cadena a verificar: ").strip().lower()

    # Verifica la cadena
    mensaje = verificar_cadena(cadena, alfabeto, letra_inicial)

    print(mensaje)

    # Cuarto punto: añadir un prefijo y sufijo a todas las palabras del lenguaje generado
    print("Cuarto punto: Se agregará un prefijo y sufijo a todas las palabras generadas.")
    prefijo = input("Ingrese el prefijo que desea agregar: ")  # Pedimos el prefijo
    sufijo = input("Ingrese el sufijo que desea agregar: ")  # Pedimos el sufijo
    print(prefijo_sufijo(resultado, sufijo, prefijo))  # Mostramos las palabras con prefijo y sufijo

# Ejecuta la función principal
main()
