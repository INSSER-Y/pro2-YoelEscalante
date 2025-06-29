
# 1. Crear el diccionario 'producto'
producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

# 2. Imprimir nombre y precio del producto
print(f"Producto: {producto['nombre']}")
print(f"Precio unitario: Bs. {producto['precio_unitario']}")

# 3. Simular una venta: restar 5 unidades del stock
producto["stock"] -= 5

# 4. Añadir clave "en_oferta" con valor True
producto["en_oferta"] = True

# 5. Imprimir el diccionario completo con todos los cambios
print("\nEstado final del producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
print()
#---------------------------------------
#ejercicio 2: inventario
#---------------------------------------
# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear al menos tres diccionarios de productos diferentes
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "stock": 50
}

producto2 = {
    "nombre": "Café de los Yungas",
    "stock": 100
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "stock": 80
}

# 3. Añadir los productos al inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir cantidad de tipos de producto
print(f"\nCantidad de productos en inventario: {len(inventario)}")

# 5. Recorrer el inventario e imprimir resumen
print("\n--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
print()
#dinamica
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
