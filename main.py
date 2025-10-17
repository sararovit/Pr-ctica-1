import statistics

def leer_datos(nombre_archivo):
    """Lee números enteros de un fichero, uno por línea."""
    numeros = []

    with open(nombre_archivo, 'r') as f:    
            for linea in f:
                numero = int(linea.strip())  # Quita espacios y convierte a entero
                numeros.append(numero) #añade a la lista numeros

    return numeros

def calcular_estadisticas(numeros):
    """Calcula la media y la mediana de una lista de números."""
    
    # Calcular la media
    media = sum(numeros) / len(numeros)

    # Calcular la mediana
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mitad = n // 2
    if n % 2 == 1:
        # Si la cantidad es impar, la mediana es el elemento del medio
        mediana = numeros_ordenados[mitad]
    else:
        # Si es par, la mediana es el promedio de los dos elementos centrales
        mediana = (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2

    return media, mediana


if __name__ == "__main__":
   
    lista_numeros = leer_datos("datos.txt")
    print("Números leídos del fichero:")
    print(lista_numeros)

    media, mediana=calcular_estadisticas(lista_numeros)
    print("Media:", media)
    print("Mediana:",mediana)
          



