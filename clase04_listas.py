#Listas 
#Listas de hobbys
hobbys = ["leer", "viajar", "jugar videojuegos", "escuchar musica", "ver peliculas"]
for nombre in hobbys:
    print(f"Mis hobbis son {nombre}")
print()
#Listas de comidas favoritas
comidas_favoritas = ["pizza", "hamburguesas", "tacos", "sushi", "pasta"]
for nombre in comidas_favoritas:
    mis_comidas_favoritas = input
    print(f"Mis comidas favoritas son {nombre}")
print()
#Listas de nombres de estudiantes
nombres_estudiantes = ['Carlos', 'Anahi', 'Miguel', 'Sofia', 'Diego']
for nombre in nombres_estudiantes:
  print(f"Bienvenido al equipo, {nombre}!")
print()
##Crear una lista de notas numericas
mis_notas = [85.5,92,78,88.5,95,82]
#inicializar Variable para la suma
suma_total = 0
#Usar un bucle for para calcular la suma total sin usar sum()
for nota in mis_notas:
  suma_total += nota
#calcular el promedio
promedio = suma_total / len(mis_notas)
#Imprimir resultados de forma clara
print(f"Suma total de mis notas {mis_notas} : {suma_total}")
print(f"Promedio de las notas de Yoel son: {promedio:.2f}")
print()
#suma de elementos de un vectores
def suma_elementos(vector):
    suma = 0
    for elemento in vector:
        suma += elemento
    return suma
# Casos de Prueba con assert
print("Probando sumar_elementos...")
assert suma_elementos([1, 2, 3, 4, 5]) == 15
assert suma_elementos([10, -2, 5]) == 13
assert suma_elementos([]) == 0 # ¡Importante probar con una lista vacía!
assert suma_elementos([100]) == 100
print("¡Pruebas para sumar_elementos pasaron! ")
vector = [1, 5, 4]
resultado = suma_elementos(vector)
print(f"La suma del vector {vector} es: {resultado}")
print()
#Encontrar el numero mayor de una lista
def encontrar_mayor(lista):
    if len(lista) == 0:
        return None
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
print("\nProbando encontrar_mayor...")
assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
assert encontrar_mayor([-1, -9, -2, -8]) == -1
assert encontrar_mayor([42, 42, 42]) == 42
assert encontrar_mayor([]) == None # Prueba del caso especial
assert encontrar_mayor([5]) == 5
print("¡Pruebas para encontrar_mayor pasaron! ")
vector = [1, 5, 4]
resultado = encontrar_mayor(vector)
print(f"El numero mayor del vector {vector} es: {resultado}")
print()

#contar cuantas veces hay un elemento en una lista
def contar_elemento(lista, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    if contador == 0:
        return f"El elemento {elemento} no se encuentra en la lista"
    return f"El elemento {elemento} de la lista {lista} se repite {contador} veces"
resultado= contar_elemento([1, 2, 3, 4, 5, 6, 7, 5, 9, 10], 5)
print(resultado)
print()
#invertir el orden de una lista
def lista_invertida(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida
print("\nProbando invertir_lista...")
lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = lista_invertida(lista_prueba)
assert lista_resultante == [5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5] # ¡Verifica que la original no cambió!
assert lista_invertida(["a", "b", "c"]) == ["c", "b", "a"]
assert lista_invertida([]) == []
print("¡Pruebas para invertir_lista pasaron! ")
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_invertida(vector)
print(f"Invertir la lista {vector} : la lista invertida es {resultado}")
print()
#busqueda secuencial o lineal
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
# ... (definición de la función aquí arriba) ...
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")
assert busqueda_lineal(mi_lista_desordenada, 42) == 2
assert busqueda_lineal(mi_lista_desordenada, 10) == 0 # Al inicio
assert busqueda_lineal(mi_lista_desordenada, 25) == 6 # Al final
assert busqueda_lineal(mi_lista_desordenada, 99) == -1 # No existe
assert busqueda_lineal([], 5) == -1
print("¡Pruebas para busqueda_lineal pasaron! ")
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 5
resultado = busqueda_lineal(vector, elemento)
if resultado == -1:
    print(f"Buscar si el {elemento} esta en la lista {vector} : No se a encontrado el {elemento}")
print(f"Buscar si el {elemento} esta en la lista {vector} : Si se a encontrado el {resultado}")
#busqueda binaria
def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nProbando busqueda_binaria...")
assert busqueda_binaria(lista_ordenada, 23) == 5
assert busqueda_binaria(lista_ordenada, 91) == 9 # Último
assert busqueda_binaria(lista_ordenada, 2) == 0 # Primero
assert busqueda_binaria(lista_ordenada, 3) == -1 # No existe
assert busqueda_binaria(lista_ordenada, 100) == -1 # Fuera de rango (mayor)
print("¡Pruebas para busqueda_binaria pasaron! ")
Lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento = 23
resultado = busqueda_binaria(Lista, elemento)
if resultado == -1:
    print(f"Buscar si el {elemento} esta en la lista {Lista} : No se a encontrado el {elemento}")
print(f"Buscar si el {elemento} esta en la lista {Lista} : Si se a encontrado el {resultado}")
print()
