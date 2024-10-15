import json
import os

# Lista para almacenar los productos
productos = []

# Función para cargar datos desde un archivo
def cargar_datos():
    global productos
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            productos = json.load(archivo)

# Función para guardar datos en un archivo
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        json.dump(productos, archivo)

# Función para añadir un producto
def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en la lista.")

# Función para actualizar un producto
def actualizar_producto():
    ver_productos()
    if productos:
        index = int(input("Seleccione el número del producto a actualizar: ")) - 1
        if 0 <= index < len(productos):
            print("Deje en blanco el campo que no desea actualizar.")
            nombre = input("Nuevo nombre del producto (actual: {}): ".format(productos[index]['nombre'])) or productos[index]['nombre']
            precio = input("Nuevo precio del producto (actual: {}): ".format(productos[index]['precio'])) or productos[index]['precio']
            cantidad = input("Nueva cantidad del producto (actual: {}): ".format(productos[index]['cantidad'])) or productos[index]['cantidad']
            
            productos[index]['nombre'] = nombre
            productos[index]['precio'] = float(precio)
            productos[index]['cantidad'] = int(cantidad)
            print("Producto actualizado con éxito.")
        else:
            print("Índice no válido.")

# Función para eliminar un producto
def eliminar_producto():
    ver_productos()
    if productos:
        index = int(input("Seleccione el número del producto a eliminar: ")) - 1
        if 0 <= index < len(productos):
            nombre_eliminado = productos[index]['nombre']
            del productos[index]
            print(f"Producto '{nombre_eliminado}' eliminado con éxito.")
        else:
            print("Índice no válido.")

# Función para mostrar el menú y gestionar la interacción
def menu():
    cargar_datos()  # Carga los datos al inicio
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
