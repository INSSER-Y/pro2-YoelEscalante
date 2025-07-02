# Ejercicio 1: Crear y escribir en un archivo de texto llamado "mi_diario.txt"
# Paso 1: Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"
# Paso 2: Usamos 'with open(...)' en modo escritura ('w')
# Esto Crea el archivo si no existe, y lo sobreescribe si ya existe.
with open(nombre_archivo, "w") as diario_file:
    # Paso 3: Escribimos varias líneas en el archivo usando .write()
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("¡Pero también es muy útil para comenzar desde cero!\n")

# Paso 4: Confirmamos que se ha terminado de escribir
print("✅ Diario creado y primeras entradas guardadas.")

# Ejercicio 2: Leer el contenido del diario después de escribirlo

print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())  # .strip() elimina el salto de línea al final
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# Ejercicio 3: Añadir nuevas entradas al archivo sin borrar lo anterior (modo 'a')

print("\n📝 Añadiendo nuevas entradas al diario...")

# Abrimos el archivo en modo añadir ('a')
with open(nombre_archivo, "a") as diario_file:
    # Escribimos nuevas líneas. También podemos añadir una línea separadora.
    diario_file.write("\n--- Entrada del 20 de Junio de 2025 ---\n")
    diario_file.write("El modo 'a' es genial para no perder datos.\n")
    diario_file.write("Ahora mi diario puede crecer cada día.\n")

# Confirmamos que se añadieron las nuevas entradas
print("✅ Nuevas entradas guardadas.")

# Verificamos que las nuevas entradas se añadieron correctamente
print("\n📖 Verificando el contenido final del diario...")

try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.") 
    
# Ejercicio Actividad: Agregar entradas al diario sin borrar lo anterior

# Paso 1: Definir el nombre del archivo
nombre_archivo = "mi_diario.txt"
# Paso 2: Abrir en modo 'append' (agregar al final sin borrar lo anterior)
with open(nombre_archivo, "a") as diario_file:
    print("")
    diario_file.write("Querido diario,\n")
    while True:
        entrada = input("> ")
        if entrada.lower() == "fin":
            break
        diario_file.write(entrada + "\n")
# Paso 3: Confirmar que se guardaron las entradas
print("Se guardo el texto")
