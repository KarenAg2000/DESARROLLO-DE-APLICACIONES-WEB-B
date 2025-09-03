# inventario.py

# ==========================
# Clase Producto
# ==========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto} - {self.nombre} - Cantidad: {self.cantidad} - Precio: ${self.precio:.2f}"

# ==========================
# Clase Inventario
# ==========================
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        print(f"✅ Producto {producto.nombre} agregado/actualizado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            eliminado = self.productos.pop(id_producto)
            print(f"🗑 Producto {eliminado.nombre} eliminado.")
        else:
            print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print(f"♻ Producto {self.productos[id_producto].nombre} actualizado.")
        else:
            print("⚠️ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("🔎 Resultados encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("⚠️ Producto no encontrado.")

    def mostrar_productos(self):
        if self.productos:
            print("📦 Inventario completo:")
            for p in self.productos.values():
                print(p)
        else:
            print("⚠️ No hay productos en el inventario.")

# ==========================
# Menú interactivo
# ==========================
def menu():
    inventario = Inventario()

    # Productos iniciales
    inventario.agregar_producto(Producto("G001", "Google Pixel 4", 10, 60.0))
    inventario.agregar_producto(Producto("G002", "Google Pixel 6 Pro", 5, 95.0))
    inventario.agregar_producto(Producto("H001", "Honor 10 Lite", 8, 40.0))

    while True:
        print("\n===== MENÚ INVENTARIO MG ELECTRÓNICA =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (enter para no cambiar): ")
            precio = input("Nuevo precio (enter para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del inventario...")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

# ==========================
# Ejecutar el menú
# ==========================
if __name__ == "__main__":
    menu()
