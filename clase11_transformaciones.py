#---------------------------------------
#ejercicio 1: transponer una matriz
#---------------------------------------
def transponer_matriz(matriz):
  if not matriz or not matriz[0]:
    return []
  num_filas = len(matriz)
  num_columnas = len(matriz[0])
  #Inicializamos la transpuesta con la estructura correcta (o la construimos dinamicamente)
  matriz_transpuesta = []
  for j in range(num_columnas): #El bucle exterior itera sobre las columnas originales
    nueva_fila = []
    for i in range(num_filas):  #El bucle interior itera sobre las filas originales
      nueva_fila.append(matriz[i][j])
    matriz_transpuesta.append(nueva_fila)
  return matriz_transpuesta
# Prueba tu función rigurosamente (incluye matrices no cuadradas):
m1 = [[1, 2, 3], [4, 5, 6]]  # 2x3
t1 = transponer_matriz(m1)
assert t1 == [[1, 4], [2, 5], [3, 6]]  # Debe ser 3x2
print("¡Prueba 1 (2x3) pasada! ✅")

# Puedes añadir más pruebas con assert si deseas:
# assert transponer_matriz([[1]]) == [[1]]
# assert transponer_matriz([[1, 2]]) == [[1], [2]]


print()

#---------------------------------------
#Ejercicio 2: Funcion para Verificar Identidad
#---------------------------------------
def es_identidad(matriz):
  #Requisito 1 : Debe ser cuadrado
  num_filas = len(matriz)
  if num_filas == 0:
    return True #Una matriz vacia es trivialmente identidad
  for i in range(num_filas):
    if len(matriz[i]) != num_filas:
      return False # no es cuadrada
  #Requisito 2: Verificar la diagonal y los ceros
  for i in range(num_filas):
    for j in range(num_filas):
      if i == j:
        if matriz[i][j] != 1:# La diagonal no tiene 1
          return False
      else:
        if matriz[i][j] != 0:
          return False # Elemento fuera de la diagonal no es 0
  return True # Cumple con todas las condiciones de matriz identidad
#Prueba 
identidad = [[1,0,0],[0,1,0],[0,0,1]]
no_identidad = [[1,0,0],[0,2,0],[0,0,1]]
no_cuadrada = [[1,0],[0,1],[0,0]]
assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False

print()

#---------------------------------------
#Ejercicio 3: Funcion para verificar simetria
#---------------------------------------
def es_simetrica(matriz):
  # Requisito 1: Debe ser cuadrada
  num_filas = len(matriz)
  if num_filas == 0:
      return True  # Una matriz vacía es trivialmente simétrica

  for i in range(num_filas):
      if len(matriz[i]) != num_filas:
          return False  # No es cuadrada

  # Requisito 2: Comparar matriz[i][j] con matriz[j][i]
  for i in range(num_filas):
      for j in range(i + 1, num_filas):  # Solo necesitamos chequear la triangular superior
          if matriz[i][j] != matriz[j][i]:
              return False  # ¡Con una diferencia es suficiente!

  return True  # Si nunca encontramos diferencias, es simétrica

# Prueba tu función:
sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]

assert es_simetrica(sim) == True
assert es_simetrica(no_sim) == False
assert es_simetrica(no_cuadrada) == False

print("¡Pruebas para es_simetrica pasaron! ✅")

print()
"""
producto = {'codigo' : 'P001' , 'nombre' : 'cafe' , 'precio' : 38.0 , 'stock' : 100}
print("\n--- claves del producti ---")
for clave in producto:
  print(clave)
print("\n--- clave y Valor ---")
for clave in producto:"""

# Diccionario para una Canción
cancion = {
    "titulo": "Shape of You",
    "artista": "Ed Sheeran",
    "album": "Divide",
    "duracion_segundos": 233,
    "genero": "Pop",
    "fecha_lanzamiento": ["2017-01-06"], 
    "colaboradores": ["Johnny McDaid", "Steve Mac"]
}

# Diccionario para un Coche
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Negro",
    "placa": "ABC-1234",
    "caracteristicas": {
        "tipo_motor": "Gasolina",
        "potencia_hp": 132,
        "transmision": "Automática"
    }
}

# Diccionario para un Post de Red Social
post_red_social = {
    "id_post": 987654321,
    "autor": "user.py",
    "contenido_texto": "¡Learning python!",
    "fecha_publicacion": "2025-06-23 15:30:00",
    "likes": 23,
}

# Imprimir 
print("Canción:")
print(cancion)
print("\nCoche:")
print(coche)
print("\nPost de Red Social:")
print(post_red_social)
