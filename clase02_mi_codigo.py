"""print(¡Estoy aprendiendo Git y Github en Prog II!)
nombre = Yoel Escalante 
print(fEste commit lo esta haciendo: {Yoel})"""
#ejercicio1
"""Estudiante Yoel Escalante Escobar"""
print("Escriba su edad")
edad = int(input())
if edad >= 18:
    print("Puedes ver peliculas clasificacion R!")
if edad >= 13 and edad < 18:
    print("Puedes ver peliculas clasificacion PG-13!")
if edad < 13 and edad >=0:
  print("Te recomendamos ver peliculas clasificacion G o PG!")
if edad < 0:
  print("Edad no valida!")
#practica
print("Recorriendo un String")
for numero in range(3):
    print(numero)
print ("Recorriendo un String:")
nombre = (input())
for letra in nombre:
    print(letra)    
print ("Bucle while:")
num = int(input())
contador = 0
while contador < num:
    print (f"contador es : {contador}")
    contador+=1
print("Bucle while terminado")
#ejercicio2
num_tabla = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print(f"---Tabla del {num_tabla}---")
for i in range(1,11):
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")
    