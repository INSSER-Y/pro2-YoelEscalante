#funcion para transponer una matriz
def transponer_matriz(matriz):
  if not matriz or not matriz[0]:
    return []
  num_filas = len(matriz)
  num_columnas = len(matriz[0])
  matriz_transpuesta = []
  for j in range(num_columnas):
    nueva_fila = []
    for i in range(num_filas):
      nueva_fila.append(matriz[i][j])
    matriz_transpuesta.append(nueva_fila)
  return matriz_transpuesta
matriz = [[1, 2, 3], [4, 5, 6]]
print(transponer_matriz(matriz))
#matriz es simetrica
def es_simetrica(matriz):
  num_filas = len(matriz)
  if num_filas == 0:
    return True
  for i in range(num_filas):
    if len(matriz[i]) != num_filas:
      return False
  for i in range(num_filas):
    for j in range(i + 1, num_filas):
      if matriz[i][j] != matriz[j][i]:
        return False
  return True
matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(es_simetrica(matriz))
matriz = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(es_simetrica(matriz))

def es_simetricaE(matriz):
  num_filas = len(matriz)
  if num_filas == 0:
    return True
  for i in range(num_filas): 
    for j in range(i , num_filas):
      if matriz[i][j] == matriz[j][i]:
        continue
      else:
        return False
  return True
matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(es_simetricaE(matriz))
matriz = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(es_simetricaE(matriz))



def es_simetricaD(matriz):
  num_filas = len(matriz)
  if num_filas == 0:
    return True
  for i in range(num_filas): 
    for j in range(i +1 , num_filas):
      if matriz[i][j] != matriz[j][i]:
        return False
      
  return True
matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(es_simetricaD(matriz))
matriz = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(es_simetricaD(matriz))