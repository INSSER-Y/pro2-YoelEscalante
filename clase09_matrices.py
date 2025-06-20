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

print()
print()
# 4. Crear la misma matriz usando comprensión de listas (hace lo mismo pero mas corto)
print("\n▶ MATRIZ 5x5 CON CEROS (usando comprensión de listas):\n")

# Esta línea crea una matriz 5x5 con ceros de forma compacta
matriz_comprension = [[0 for j in range(5)] for i in range(5)]

# Imprimimos la matriz generada
for fila in matriz_comprension:
    for elemento in fila:
        print(elemento, end="\t")
    print()

#Explicación visual para programadores novatos
print("\nEXPLICACIÓN:")
print('''\nmatriz_comprension = [[0 for j in range(5)] for i in range(5)]\n
↳ Parte interna: [0 for j in range(5)] → crea una fila con cinco ceros
↳ Parte externa: for i in range(5) → repite esa fila cinco veces
Resultado: Una matriz de 5x5 completamente llena de ceros.\n''')