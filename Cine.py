# Crear la sala con precios fijos
def crear_sala(filas, columnas):
    sala = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append({"estado": "L", "precio": 25})
        sala.append(fila)
    return sala

# Mostrar la sala con precios y estados
def mostrar_sala(sala):
    print("\n     " + " ".join(f"{j:^5}" for j in range(len(sala[0]))))
    print("     " + " ".join("─" * 5 for _ in range(len(sala[0]))))
    for i, fila in enumerate(sala):
        estado_fila = " ".join(f"{a['estado']:^5}" for a in fila)
        print(f"F{i:>2} | {estado_fila}")

# Método de pago simulado
def metodo_de_pago(total):
    print(f"\n💳 Total a pagar: Bs. {total}")
    print("Métodos de pago:")
    print("1. Efectivo")
    print("2. QR (simulado)")
    opcion = input("Selecciona método de pago: ")
    if opcion in ['1', '2']:
        print("✅ Pago procesado con éxito.")
    else:
        print("❌ Método no reconocido. Se asume pago en efectivo.")
    print("🎟️ ¡Gracias por tu compra!\n")

# Ocupar asiento individual
def ocupar_asiento(sala, fila, columna):
    if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]):
        asiento = sala[fila][columna]
        if asiento["estado"] == "L":
            asiento["estado"] = "O"
            total = asiento["precio"]
            print(f"Asiento ({fila}, {columna}) reservado por Bs. {total}")
            metodo_de_pago(total)
            return True
        else:
            print("❌ Ese asiento ya está ocupado.")
            return False
    else:
        print("❌ Coordenadas inválidas.")
        return False

# Buscar N asientos juntos en una fila
def buscar_asientos_juntos(sala, cantidad):
    for i, fila in enumerate(sala):
        consecutivos = 0
        for j, asiento in enumerate(fila):
            if asiento["estado"] == "L":
                consecutivos += 1
                if consecutivos == cantidad:
                    return i, j - cantidad + 1
            else:
                consecutivos = 0
    return None, None

# Ocupar N asientos juntos
def ocupar_asientos_juntos(sala, cantidad):
    fila, inicio = buscar_asientos_juntos(sala, cantidad)
    if fila is not None:
        total = 0
        for j in range(inicio, inicio + cantidad):
            sala[fila][j]["estado"] = "O"
            total += sala[fila][j]["precio"]
        print(f"🎟️ {cantidad} asientos reservados en fila {fila}, desde columna {inicio}.")
        metodo_de_pago(total)
        return True
    else:
        print("❌ No hay suficientes asientos contiguos disponibles.")
        return False

# Contar asientos libres
def contar_asientos_libres(sala):
    return sum(asiento["estado"] == "L" for fila in sala for asiento in fila)

# Programa principal
def main():
    filas, columnas = 5, 8
    sala = crear_sala(filas, columnas)

    while True:
        print("\n🎬 Sala actual:")
        mostrar_sala(sala)
        print(f"Asientos libres: {contar_asientos_libres(sala)}")
        print("\nMenú:")
        print("1. Ocupar asiento individual")
        print("2. Buscar y ocupar N asientos juntos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
                ocupar_asiento(sala, fila, columna)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == '2':
            try:
                n = int(input("¿Cuántos asientos necesitas juntos?: "))
                ocupar_asientos_juntos(sala, n)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == '0':
            print("Gracias por usar el sistema de reserva de cine. 🎥")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar
if __name__ == "__main__":
    main()
