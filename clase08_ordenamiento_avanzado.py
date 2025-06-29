def merge_sort(lista):
  # Paso Vencer (Condición Base de la Recursividad):
  if len(lista) <= 1:
      return lista

  # Paso 1: DIVIDIR
  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  # Paso 2: VENCER (Recursión)
  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  # Paso 3: COMBINAR
  print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = j = 0

  # Comparar elementos de izquierda y derecha uno por uno
  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  # Agregar cualquier elemento restante
  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

# --- Prueba ---
lista_prueba = [8, 3, 5, 1]
print("Lista original:", lista_prueba)
resultado = merge_sort(lista_prueba)
print("Lista ordenada:", resultado)

# --- Pruebas automatizadas ---
assert merge_sort([]) == []                         # Lista vacía
assert merge_sort([1]) == [1]                       # Lista con un solo elemento
assert merge_sort([5, 2]) == [2, 5]                  # Lista con dos elementos
assert merge_sort([3, 1, 2]) == [1, 2, 3]            # Lista con tres elementos desordenados
assert merge_sort([10, 5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8, 10]  # Lista par
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]  # Lista en orden descendente
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Lista ya ordenada
assert merge_sort([4, 2, 2, 4, 1]) == [1, 2, 2, 4, 4]  # Lista con elementos repetidos
assert merge_sort([100, -50, 0, 50, -100]) == [-100, -50, 0, 50, 100]  # Lista con enteros negativos y positivos
assert merge_sort([2.5, 1.2, 3.8]) == [1.2, 2.5, 3.8]  # Lista con flotantes
print("¡Todas las pruebas con assert pasaron correctamente!")

print()

#Quicksort
def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    # Elegimos un pivote (usamos el primer elemento en este caso)
    pivote = lista[0]
    # Creamos dos listas: una para menores y otra para mayores al pivote
    menores = []  # Elementos menores al pivote
    mayores = []  # Elementos mayores o iguales al pivote

    # Recorremos el resto de la lista (sin el pivote)
    for elemento in lista[1:]:
        if elemento < pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)
    # Aplicamos quicksort recursivamente a las sublistas y combinamos
    return quicksort(menores) + [pivote] + quicksort(mayores)

mi_lista = [10, 5, 42, 8, 17]
print("Lista original:", mi_lista)
lista_ordenada = quicksort(mi_lista)
print("Lista ordenada:", lista_ordenada)

def insertion_sort(lista, izquierda, derecha):
    for i in range(izquierda + 1, derecha + 1):
        clave = lista[i]
        j = i - 1
        while j >= izquierda and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
def merge(lista, izquierda, medio, derecha):
    izquierda_lista = lista[izquierda:medio + 1]
    derecha_lista = lista[medio + 1:derecha + 1]
    i = j = 0
    k = izquierda

    while i < len(izquierda_lista) and j < len(derecha_lista):
        if izquierda_lista[i] <= derecha_lista[j]:
            lista[k] = izquierda_lista[i]
            i += 1
        else:
            lista[k] = derecha_lista[j]
            j += 1
        k += 1

    while i < len(izquierda_lista):
        lista[k] = izquierda_lista[i]
        i += 1
        k += 1

# Timsort básico
def timsort(lista):
    n = len(lista)
    bloque = 8  # tamaño fijo de run

    # Ordenar por bloques pequeños con Insertion Sort
    for i in range(0, n, bloque):
        insertion_sort(lista, i, min(i + bloque - 1, n - 1))

    # Mezclar bloques de a pares, aumentando tamaño
    tamaño = bloque
    while tamaño < n:
        for izquierda in range(0, n, 2 * tamaño):
            medio = min(izquierda + tamaño - 1, n - 1)
            derecha = min(izquierda + 2 * tamaño - 1, n - 1)
            if medio < derecha:
                merge(lista, izquierda, medio, derecha)
        tamaño *= 2
lista = [5, 3, 8, 1, 9, 2, 4, 7, 6]
print("Original:", lista)
timsort(lista)
print("Ordenada:", lista)
