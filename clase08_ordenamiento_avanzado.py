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

# matrices 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#opcion recorriendo con indices
num_filas = len(matriz)
num_columnas = len(matriz[0])
for i in range(num_filas):#bucle exterior para fila (0,1,2)
    for j in range(num_columnas):#bucle interior para indices de columna (0,1,2)
        elemento = matriz[i][j]
        print(f"Elemento en la fila {i}, columna {j}: {elemento}")
print()
#opcion 2: recorriendo por elemento (mas "pythonico")
for fila_actual in matriz: #bucle exterior toma cada lista-fila
    for elemento in fila_actual:#buecle interior toma cada elemento de esa fila
        print(elemento, end=" ")#"end=' '" para imprimir en la misma linea
    print()#salto de linea al final de cada fila
print()
#---------------------------
#ejercicio 1 Modelando un teclado numerico
#---------------------------
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila_actual in teclado:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()
for fila_actual in teclado:
    for elemento in fila_actual:
        print(elemento, end="\t")
    print()
vacio = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    vacio.append(fila)
    print()
for fila in vacio:
    for elemento in fila:
        print(elemento, end="\t")
    print()
