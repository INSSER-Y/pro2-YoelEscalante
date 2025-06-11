#Listas 
#Listas de hobbys
hobbys = ["leer", "viajar", "jugar videojuegos", "escuchar musica", "ver peliculas"]
for nombre in hobbys:
    print(f"Mis hobbis son {nombre}")
print()
#Listas de comidas favoritas
comidas_favoritas = ["pizza", "hamburguesas", "tacos", "sushi", "pasta"]
for nombre in comidas_favoritas:
    print(f"Mis comidas favoritas son {nombre}")
print()
#Listas de nombres de estudiantes
nombres_estudiantes = ['Carlos', 'Ana', 'Miguel', 'Sofia', 'Diego']
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
print(f"Suma total de las notas: {suma_total}")
print(f"Promedio de las notas de Yoel son: {promedio:.2f}")
print()