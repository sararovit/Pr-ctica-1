def leer_datos(fichero):
    """Lee números enteros de un fichero, uno por línea."""
    numeros = []
    try:
        with open(fichero, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if linea:  # Ignora líneas vacías
                    numeros.append(int(linea))
    except FileNotFoundError:
        print(f"Error: El fichero '{fichero}' no existe.")
    except ValueError as e:
        print(f"Error de conversión: {e}")
    return numeros

def calcular_estadisticas(numeros):
    """Calcula la media y la mediana de una lista de números."""
    if not numeros:
        return None, None  # Evita dividir por cero si la lista está vacía

    # Calcular la media
    media = sum(numeros) / len(numeros)

    # Calcular la mediana
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mitad = n // 2

    if n % 2 == 0:
        mediana = (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    else:
        mediana = numeros_ordenados[mitad]

    return media, mediana

if __name__ == "__main__":
    nombre_fichero = "datos.txt"
    lista_numeros = leer_datos(nombre_fichero)
    print("Números leídos del fichero:")
    print(lista_numeros)


