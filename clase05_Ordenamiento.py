#ordenamiento burbuja
def ordenamiento_burbuja(lista):
    n= len(lista) #Cantidad de elementos en la lista
    for i in range(n -1): #Bucle exterior para las pasadas
        hubo_intercambio = False  #Marca si hubo un intercambio en esta pasada
        for j in range(n - 1 - i):#cada pasada evita revisar los ultimos ya ordenados
            if lista[j] > lista[j + 1]:
                #Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio: #Si no hubo intercambio en esta pasada, la lista está ordenada
            break
    return lista #opcional tambien se puede omitir
if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después:", numeros)
# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_burbuja(lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"
# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_burbuja(lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"
# Caso 3: Lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_burbuja(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"
# Caso 4: Lista con elementos duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_burbuja(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"
# Caso borde: Lista vacía
assert ordenamiento_burbuja([]) == [], "Fallo en lista vacía"
# Caso borde: Lista con un solo elemento
assert ordenamiento_burbuja([42]) == [42], "Fallo en lista con un solo elemento"
print("¡Todas las pruebas ordenamiento burbuja pasaron! ✅")
#Prueba de la funcion
lista_a_ordenar = [64,34,25,12,22,11,90]
print(f"Lista original: {lista_a_ordenar}")
ordenamiento_burbuja(lista_a_ordenar)#llamamos a la funcion
print(f"Lista ordenada: {lista_a_ordenar}")
print()

#ordenamiento por insercion
def ordenamiento_insercion(lista):
    #Empezamos desde el segundo elemento(indice1)
    for i in range(1,len(lista)):
        valor_actual = lista[i]#la"carta" que vamos a insertar
        posicion_actual = i
        #Desplazar elementos mayores hacia la derecha
        #mientras la posicion sea valida y el elemento a la izquierda sea mayor
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1] #desplazamiento
            posicion_actual -= 1
        #Insertar la "carta" en su posicion correcta"
        lista[posicion_actual] = valor_actual
    return lista
if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_insercion(numeros)
    print("Después:", numeros)
# Pruebas usando assert algoritmo de inserción
# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_insercion(lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"
# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_insercion(lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"
# Caso 3: Lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_insercion(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"
# Caso 4: Lista con duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_insercion(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"
# Caso borde: Lista vacía
assert ordenamiento_insercion([]) == [], "Fallo en lista vacía"
# Caso borde: Lista con un solo elemento
assert ordenamiento_insercion([42]) == [42], "Fallo en lista con un solo elemento"
print("¡Todas las pruebas del ordenamiento por inserción pasaron! ✅")
print()

#
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Mientras haya elementos en ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añadir los restos de cada lista si quedan
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    numeros = merge_sort(numeros)
    print("Después:", numeros)
print()

