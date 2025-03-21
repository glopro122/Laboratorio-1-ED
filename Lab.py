print('hola')
def Crear_Archivo_Productos(productos):
    with open('productos.csv', 'w') as file:
        keys = list(productos[0].keys())
        file.write(','.join(keys) + '\n')  # Escribir la cabecera
        for producto in productos:
            file.write(
                str(producto['ID']) + ',' +
                producto['Nombre'] + ',' +
                producto['Categoría'] + ',' +
                str(producto['Precio']) + ',' +
                str(producto['Stock']) + '\n'
            )

def Crear_Archivo_Proveedores(proveedores):
    with open('proveedores.csv', 'w') as file:
        keys = list(proveedores[0].keys())
        file.write(','.join(keys) + '\n')  # Escribir la cabecera
        for proveedor in proveedores:
            file.write(
                proveedor['id'] + ',' +
                proveedor['Nombre'] + ',' +
                proveedor['Contacto'] + ',' +
                proveedor['Direccion'] + '\n'
            )

def Crear_Archivo_Ventas(ventas):
    with open('ventas.csv', 'w') as file:
        keys = list(ventas[0].keys())
        file.write(','.join(keys) + '\n')  # Escribir la cabecera
        for venta in ventas:
            file.write(
                venta['ID_Venta'] + ',' +
                venta['ID_Producto'] + ',' +
                venta['ID_Cliente'] + ',' +
                venta['Fecha_Venta'] + ',' +
                venta['Cantidad'] + '\n'
            )

def Crear_Archivo_Compras(compras):
    with open('compras.csv', 'w') as file:
        keys = list(compras[0].keys())
        file.write(','.join(keys) + '\n') 
        for compra in compras:
            file.write(
                compra['ID_Compra'] + ',' +
                compra['ID_Producto'] + ',' +
                compra['ID_Proveedor'] + ',' +
                compra['Fecha_Compra'] + ',' +
                compra['Cantidad'] + '\n'
            )

def agregar_producto(productos):
    with open("productos.csv", 'a') as file:
        for producto in productos:
            linea = f"{producto['id_producto']},{producto['Nombre']},{producto['Categoria']},{producto['Precio']},{producto['Stock']}\n"
        file.write(linea)

productos = [
    {"ID": 1, "Nombre": "Laptop", "Categoría": "Electrónica", "Precio": 2000000, "Stock": 50},
    {"ID": 2, "Nombre": "Zapatos", "Categoría": "Calzado", "Precio": 270000, "Stock": 10},
    {"ID": 3, "Nombre": "Camiseta", "Categoría": "Ropa", "Precio": 50000, "Stock": 30},
    {"ID": 4, "Nombre": "Cuadernos", "Categoría": "Útiles", "Precio": 5000, "Stock": 10}
]

proveedores = [
    {"id":1, "Nombre":"TecnoSuministros S.A.", "Contacto":"contacto@tecnosuministros.com", "Direccion":"Calle 123 #45-67, Bogotá, Colombia"},
    {"id":2, "Nombre":"Calzados y Más", "Contacto":"info@calzadosymas.com", "Direccion":"Avenida Principal #98-76, Medellín, Colombia"},
    {"id":3, "Nombre":"Textiles Modernos", "Contacto":"ventas@textilesmodernos.com", "Direccion":"Carrera 56 #12-34, Cali, Colombia"},
    {"id":4, "Nombre":"Papelería Educativa", "Contacto":"servicio@papeleriaeducativa.com", "Direccion":"Calle 89 #10-11, Barranquilla, Colombia"}
]

ventas = [
    {"ID_Venta": 1, "ID_Producto": 1, "ID_Cliente": 1, "Fecha_Venta": "2023-10-01", "Cantidad": "2"},
    {"ID_Venta": 2, "ID_Producto": 2, "ID_Cliente": 2, "Fecha_Venta": "2023-10-02", "Cantidad": "1"},
    {"ID_Venta": 3, "ID_Producto": 3, "ID_Cliente": 3, "Fecha_Venta": "2023-10-03", "Cantidad": "5"},
    {"ID_Venta": 4, "ID_Producto": 4, "ID_Cliente": 4, "Fecha_Venta": "2023-10-04", "Cantidad": "3"}
]

compras = [
    {"ID_Compra": 1, "ID_Producto": 1, "ID_Proveedor": 1, "Fecha_Compra": "2023-09-25", "Cantidad": "10"},
    {"ID_Compra": 2, "ID_Producto": 2, "ID_Proveedor": 2, "Fecha_Compra": "2023-09-26", "Cantidad": "20"},
    {"ID_Compra": 3, "ID_Producto": 3, "ID_Proveedor": 3, "Fecha_Compra": "2023-09-27", "Cantidad": "15"},
    {"ID_Compra": 4, "ID_Producto": 4, "ID_Proveedor": 4, "Fecha_Compra": "2023-09-28", "Cantidad": "30"}
]

Crear_Archivo_Productos(productos)
Crear_Archivo_Proveedores(proveedores)
Crear_Archivo_Ventas(ventas)
Crear_Archivo_Compras(compras)
k=4
for i in range(0, 99):  
    condicion= input('¿Que desea hacer? \n 1. Ver productos ordenados por precio \n 2. Agregar un nuevo cliente. \n 3. Calcular el total de ventas por producto. \n 4. Ver clientes que han realizado compras. \n 5. Salir \n')
    while int(condicion)< 1 or int(condicion) > 7:
        print ('Opcion Invalida, digite nuevamente \n')
        condicion = input('¿Que desea hacer? \n 1. Ver opciones de producto \n 2. \n 3. \n 4.  \n 5. Salir \n')

    if condicion == '1':
        co = input('1.Agregar producto \n 2.Actualizar producto \n3.Volver al menú anterior')
        if co == '1':
            k=k+1
            print("\n--- Agregar un Nuevo Producto ---")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = input("Ingrese el precio del producto: ")
            stock = input("Ingrese el stock del producto: ")
            productos = [{"id_producto":k,"Nombre":nombre ,"Categoria":categoria, "Precio":precio, "Stock":stock}]
            agregar_producto(productos)
            print(' \n --- AGREGADO CON EXITO   --- \n')
        elif co == '2':
            break
        elif co == '3':
            break