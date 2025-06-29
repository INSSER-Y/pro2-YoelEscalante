import random
import json
import os

# Archivos para usuarios y partida
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_PARTIDA = "partida.json"

# === GESTIÓN DE USUARIOS ===
def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def registrar_usuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingresa nuevo nombre de usuario: ")
    if nombre in usuarios:
        print("El nombre ya está registrado.")
        return None
    contrasena = input("Crea una contraseña: ")
    usuarios[nombre] = {"contrasena": contrasena}
    guardar_usuarios(usuarios)
    print("Registro exitoso.")
    return nombre

# === GESTIÓN DE PARTIDAS ===
def guardar_partida(datos):
    with open(ARCHIVO_PARTIDA, "w") as f:
        json.dump(datos, f)

def cargar_partida():
    if os.path.exists(ARCHIVO_PARTIDA):
        with open(ARCHIVO_PARTIDA, "r") as f:
            return json.load(f)
    return None

def borrar_partida():
    if os.path.exists(ARCHIVO_PARTIDA):
        os.remove(ARCHIVO_PARTIDA)

# === CONFIGURACIÓN DEL JUEGO ===
def obtener_tamano():
    filas = int(input("\u00bfCuántas filas quieres en el tablero? "))
    columnas = int(input("\u00bfCuántas columnas quieres en el tablero? "))
    return filas, columnas

def crear_tablero(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    columnas = len(tablero[0])
    print("  " + " ".join(str(i + 1) for i in range(columnas)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("?")
        print(letra + " " + " ".join(fila_mostrar))

def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

def colocar_barcos(tablero, cantidad):
    filas = len(tablero)
    columnas = len(tablero[0])
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

def disparo_normal(tablero_objetivo, tablero_disparos, coord):
    fila, columna = coord_a_indices(coord)
    filas = len(tablero_objetivo)
    columnas = len(tablero_objetivo[0])
    if not (0 <= fila < filas and 0 <= columna < columnas):
        print("\u00a1Coordenada inv\u00e1lida!")
        return False
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print("\u00a1Tocado!")
        return True
    elif tablero_objetivo[fila][columna] in [0, 3]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print("Agua...")
        return True
    else:
        print("Ya disparaste all\u00ed.")
        return False

def disparo_horizontal(tablero_objetivo, tablero_disparos, fila_letra):
    fila = ord(fila_letra.upper()) - ord('A')
    columnas = len(tablero_objetivo[0])
    for columna in range(columnas):
        disparo_normal(tablero_objetivo, tablero_disparos, f"{chr(ord('A') + fila)}{columna + 1}")

def disparo_2x2(tablero_objetivo, tablero_disparos, coord):
    fila, columna = coord_a_indices(coord)
    for i in range(2):
        for j in range(2):
            f = fila + i
            c = columna + j
            if 0 <= f < len(tablero_objetivo) and 0 <= c < len(tablero_objetivo[0]):
                disparo_normal(tablero_objetivo, tablero_disparos, f"{chr(ord('A') + f)}{c + 1}")

def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

def juego():
    print("=== Batalla Naval Guardada ===")
    nombre1 = registrar_usuario()
    if not nombre1:
        return
    modo = input("\u00bfModo 1 jugador (1) o 2 jugadores (2)? ")
    nombre2 = registrar_usuario() if modo == "2" else "CPU"

    filas, columnas = obtener_tamano()
    tablero1 = crear_tablero(filas, columnas)
    tablero2 = crear_tablero(filas, columnas)
    disparos1 = crear_tablero(filas, columnas)
    disparos2 = crear_tablero(filas, columnas)

    colocar_barcos(tablero1, 3)
    colocar_barcos(tablero2, 3)

    usados_j1 = {"h": False, "x": False}
    usados_j2 = {"h": False, "x": False}

    turno = 1
    while quedan_barcos(tablero1) and quedan_barcos(tablero2):
        print(f"\n--- Turno {turno} ---")
        print(f"\n{nombre1}, este es tu tablero:")
        mostrar_tablero(tablero1)
        print(f"\nTablero de disparos hacia {nombre2}:")
        mostrar_tablero(disparos1)
        print(f"\nDisparos especiales restantes → horizontal: {int(not usados_j1['h'])}, 2x2: {int(not usados_j1['x'])}")
        tipo = input(f"{nombre1}, elige tipo de disparo - normal (n), horizontal (h), 2x2 (x): ").lower()
        if tipo == "n":
            coord = input("Ingresa coordenada (ej. A3): ")
            disparo_normal(tablero2, disparos1, coord)
        elif tipo == "h" and not usados_j1["h"]:
            fila = input("Fila (letra) para disparo horizontal: ")
            disparo_horizontal(tablero2, disparos1, fila)
            usados_j1["h"] = True
        elif tipo == "x" and not usados_j1["x"]:
            coord = input("Coordenada superior izquierda del 2x2: ")
            disparo_2x2(tablero2, disparos1, coord)
            usados_j1["x"] = True
        else:
            print("\u00a1Ya usaste ese disparo o tipo inv\u00e1lido!")

        if not quedan_barcos(tablero2):
            break

        print(f"\n{nombre2}, este es tu tablero:")
        mostrar_tablero(tablero2)
        print(f"\nTablero de disparos hacia {nombre1}:")
        mostrar_tablero(disparos2)
        print(f"\nDisparos especiales restantes → horizontal: {int(not usados_j2['h'])}, 2x2: {int(not usados_j2['x'])}")

        if modo == "2":
            tipo = input(f"{nombre2}, elige tipo de disparo - normal (n), horizontal (h), 2x2 (x): ").lower()
            if tipo == "n":
                coord = input("Ingresa coordenada: ")
                disparo_normal(tablero1, disparos2, coord)
            elif tipo == "h" and not usados_j2["h"]:
                fila = input("Fila (letra) para disparo horizontal: ")
                disparo_horizontal(tablero1, disparos2, fila)
                usados_j2["h"] = True
            elif tipo == "x" and not usados_j2["x"]:
                coord = input("Coordenada superior izquierda del 2x2: ")
                disparo_2x2(tablero1, disparos2, coord)
                usados_j2["x"] = True
            else:
                print("\u00a1Ya usaste ese disparo o tipo inv\u00e1lido!")
        else:
            if not usados_j2["x"]:
                coord = f"{chr(ord('A') + random.randint(0, filas - 2))}{random.randint(1, columnas - 1)}"
                print(f"{nombre2} usa disparo 2x2 en {coord}")
                disparo_2x2(tablero1, disparos2, coord)
                usados_j2["x"] = True
            elif not usados_j2["h"]:
                fila = chr(ord('A') + random.randint(0, filas - 1))
                print(f"{nombre2} usa disparo horizontal en fila {fila}")
                disparo_horizontal(tablero1, disparos2, fila)
                usados_j2["h"] = True
            else:
                while True:
                    f = random.randint(0, filas - 1)
                    c = random.randint(0, columnas - 1)
                    if tablero1[f][c] in [0, 1]:
                        break
                coord = f"{chr(ord('A') + f)}{c + 1}"
                print(f"{nombre2} dispara a {coord}")
                disparo_normal(tablero1, disparos2, coord)

        turno += 1

    print("\n=== Fin del juego ===")
    if quedan_barcos(tablero1):
        print(f"\u00a1{nombre1} gana!")
    else:
        print(f"\u00a1{nombre2} gana!")

# Ejecutar el juego
juego()
