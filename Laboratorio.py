producto = 'productos.csv'
proveedor = 'proveedores.csv'
venta = 'ventas.csv'
compra = 'compras.csv'


def Crear_Archivo_Productos(productos):
    with open('productos.csv', 'w') as file:
        keys = list(productos[0].keys())
        file.write(','.join(keys) + '\n')
        for producto in productos:
            file.write(
                f"{producto['ID_Producto']},{producto['Nombre']},{producto['Categoría']},{producto['Precio']},{producto['Stock']}\n"
            )

def Crear_Archivo_Proveedores(proveedores):
    with open('proveedores.csv', 'w') as file:
        keys = list(proveedores[0].keys())
        file.write(','.join(keys) + '\n') 
        for proveedor in proveedores:
            file.write(
                f"{proveedor['id']},{proveedor['Nombre']},{proveedor['Contacto']},{proveedor['Direccion']}\n"
            )

def Crear_Archivo_Ventas(ventas):
    with open('ventas.csv', 'w') as file:
        keys = list(ventas[0].keys())
        file.write(','.join(keys) + '\n') 
        for venta in ventas:
            file.write(
                f"{venta['ID_Venta']},{venta['ID_Producto']},{venta['ID_Cliente']},{venta['Fecha_Venta']},{venta['Cantidad']}\n"
            )

def Crear_Archivo_Compras(compras):
    with open('compras.csv', 'w') as file:
        keys = list(compras[0].keys())
        file.write(','.join(keys) + '\n') 
        for compra in compras:
            file.write(
                f"{compra['ID_Compra']},{compra['ID_Producto']},{compra['ID_Proveedor']},{compra['Fecha_Compra']},{compra['Cantidad']}\n"
            )

def create_indexp():
    with open('productos.csv', 'r') as file:
        lines = file.readlines()
    with open ('index_produc.csv', 'w') as file:
        for i in range (1, len(lines)):
            id = lines[i].split(',')[0]
            file.write(str(i) + ',' + id + '\n')

def create_indexp2():
    with open('proveedores.csv', 'r') as file:
        lines = file.readlines()
    with open ('index_proveedores.csv', 'w') as file:
        for i in range (1, len(lines)):
            id = lines[i].split(',')[0]
            file.write(str(i) + ',' + id + '\n')

def create_indexv():
    with open('ventas.csv', 'r') as file:
        lines = file.readlines()
    with open ('index_ventas.csv', 'w') as file:
        for i in range (1, len(lines)):
            id = lines[i].split(',')[0]
            file.write(str(i) + ',' + id + '\n')

def create_indexc():
    with open('compras.csv', 'r') as file:
        lines = file.readlines()
    with open ('index_compras.csv', 'w') as file:
        for i in range (1, len(lines)):
            id = lines[i].split(',')[0]
            file.write(str(i) + ',' + id + '\n')

def agregar_producto(productos):
    with open("productos.csv", 'a') as file:
        for producto in productos:
            linea = f"{producto['ID_Producto']},{producto['Nombre']},{producto['Categoría']},{producto['Precio']},{producto['Stock']}\n"
            file.write(linea)

def mostrarp(id):
    with open("productos.csv", 'r') as file:
        lines = file.readlines()
        j=0
        k=0
        for line in lines:
            j=j+1
        for line in lines:
            k=k+1
            v =line.split(',')
            if v[0] != 'ID_Producto' and int(v[0]) == int(id):
                print('La id del pedido es:'+v[0]+'\nEl nombre del pedido es: '+ v[1] +'\nLa categoria del pedido es: '+v[2]+'\nEl precio del pedido es: '+v[3]+'\nEl stock del pedido es: '+v[4])

def actualizarp(id,productos):
    with open('productos.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('productos.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'ID_Producto' and int(v[0]) == int(id):
                    for i in productos:
                        file.write(str(v[0])+ ',' +i['Nombre'] + ',' + i['Categoría'] + ',' + i['Precio'] + ',' + i['Stock'] + '\n')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def eliminarp(id):
    with open('productos.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('productos.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'ID_Producto' and int(v[0]) == int(id):
                    for i in productos:
                        file.write('')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def agregar_proveedor(proveedores):
    with open("proveedores.csv", 'a') as file:
        for proveedor in proveedores:
            linea = f"{proveedor['id']},{proveedor['Nombre']},{proveedor['Contacto']},{proveedor['Direccion']}\n"
            file.write(linea)

def mostrarp2(id):
    with open("proveedores.csv", 'r') as file:
        lines = file.readlines()
        j=0
        k=0
        for line in lines:
            j=j+1
        for line in lines:
            k=k+1
            v =line.split(',')
            if v[0] != 'id' and int(v[0]) == int(id):
                print('La id del proveedor es: '+v[0]+'\nEl nombre del proveedor es: '+ v[1] +'\nEl contacto del proveedor es: '+v[2]+'\nLa direccion del proveedor es: '+v[3]+v[4]+v[5])
            elif k==j:
                print('El pedido no existe')

def actualizarp2(id,proveedores):
    with open('proveedores.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('proveedores.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'id' and int(v[0]) == int(id):
                    for i in productos:
                        file.write(str(v[0]) + ',' + i['Nombre'] + ',' + i['Contacto'] + ',' + i['Direccion'] + '\n')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def eliminarp2(id):
    with open('proveedores.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('proveedores.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'id' and int(v[0]) == int(id):
                    for i in productos:
                        file.write('')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el proveedor')
                else:
                    file.write(line)

def agregar_venta(ventas):
    with open("ventas.csv", 'a') as file:
        for venta in ventas:
            file.write(
                f"{venta['ID_Venta']},{venta['ID_Producto']},{venta['ID_Cliente']},{venta['Fecha_Venta']},{venta['Cantidad']}\n"
            )

def mostrarv(id):
    with open("ventas.csv", 'r') as file:
        lines = file.readlines()
        j=0
        k=0
        for line in lines:
            j=j+1
        for line in lines:
            k=k+1
            v =line.split(',')
            if v[0] != 'ID_Venta' and int(v[0]) == int(id):
                print('La id de la venta es es: '+v[0]+'\nLa id del producto es: '+ v[1] +'\nLa fecha de la venta es: '+v[2]+'\nLa cantidad de la venta es: '+v[3])

def actualizarv(id,venta):
    with open('ventas.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('ventas.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'id' and int(v[0]) == int(id):
                    for i in venta:
                        file.write(str(v[0]) + ',' + i['Nombre'] + ',' + i['Contacto'] + ',' + i['Direccion'] + '\n')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def eliminarv(id):
    with open('proveedores.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('proveedores.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'id' and int(v[0]) == int(id):
                    for i in productos:
                        file.write('')
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el proveedor')
                else:
                    file.write(line)

productos = [
    {"ID_Producto": 1, "Nombre": "Laptop", "Categoría": "Electrónica", "Precio": 2000000, "Stock": 50},
    {"ID_Producto": 2, "Nombre": "Zapatos", "Categoría": "Calzado", "Precio": 270000, "Stock": 10},
    {"ID_Producto": 3, "Nombre": "Camiseta", "Categoría": "Ropa", "Precio": 50000, "Stock": 30},
    {"ID_Producto": 4, "Nombre": "Cuadernos", "Categoría": "Útiles", "Precio": 5000, "Stock": 10}
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
create_indexp()
create_indexp2()
create_indexv()
create_indexc()
c=4
k=4
f=4
y=4
for i in range(0, 99):
    create_indexp()
    create_indexp2()
    create_indexv()
    create_indexc()
    h = True
    condicion= input('¿Que desea hacer? \n1. Gestión de Productos \n2. Gestión de Proveedores \n3. Gestión de Ventas \n4. Gestión de Compras \n5. Reportes \n6. Salir\n')
    while int(condicion)< 1 or int(condicion) > 6:
        print ('Opcion Invalida, digite nuevamente')
        condicion = input('¿Que desea hacer? \n1. Gestión de Productos \n2. Gestión de Proveedores \n3. Gestión de Ventas \n4. Gestión de Compras \n5. Reportes \n6. Salir\n')

    if condicion == '1':
        co = input('\n1. Registrar Producto\n2. Buscar Producto\n3. Actualizar Producto\n4. Eliminar Producto\n5. Volver al menú principal\n')
        if co == '1':
            k=k+1
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = input("Ingrese el precio del producto: ")
            stock = input("Ingrese el stock del producto: ")
            productos = [{"ID_Producto":k,"Nombre":nombre ,"Categoría":categoria, "Precio":precio, "Stock":stock}]
            agregar_producto(productos)
            print(' \nAgregado con exito \n')
        elif co == '2':
            print('¿Que producto quiere buscar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es la id?')
                        ids = input()
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es la id?')
                    ids = input()
            mostrarp(ids)

        elif co == '3':
            print('¿Que producto quiere actualizar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es su id?')
                        ids = input()
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = input("Ingrese el precio del producto: ")
            stock = input("Ingrese el stock del producto: ")
            productos = [{"Nombre":nombre ,"Categoría":categoria, "Precio":precio, "Stock":stock}]
            actualizarp(ids,productos)

        elif co == '4':
            print('¿Que producto quiere eliminar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es el id?')
                        ids = input()
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            eliminarp(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '2':
        co = input('\n1. Registrar Proveedor\n2. Buscar Proveedor\n3. Actualizar Proveedor\n4. Eliminar Proveedor\n5. Volver al Menú Principal\n')

        if co == '1':
            c=c+1
            nombre = input("Ingrese el nombre del proveedor: ")
            contacto = input("Ingrese el contacto del proveedor: ")
            direccion = input("Ingrese la direccion del proveedor: ")
            proveedor = [{"id":c,"Nombre":nombre ,"Contacto":contacto, "Direccion":direccion}]
            agregar_proveedor(proveedor)
            print(' \nAgregado con exito \n')

        elif co == '2':
            print('¿Que producto quiere buscar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es su id?')
                        ids = input()
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            mostrarp2(ids)

        elif co == '3':
            print('¿Que proveedor quiere actualizar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es su id?')
                        ids = input()
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            nombre = input("Ingrese el nombre del proveedor: ")
            contacto = input("Ingrese el contacto del proveedor: ")
            direccion = input("Ingrese la direccion del proveedor: ")
            productos = [{"Nombre":nombre ,"Contacto":contacto, "Direccion":direccion}]
            actualizarp2(ids,productos)

        elif co == '4':
            print('¿Que proveedor quiere eliminar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es el id?')
                        ids = input()
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            eliminarp2(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '3':
        co = input('\n1. Registrar Venta\n2. Buscar Venta\n3. Actualizar Venta\n4. Eliminar Venta\n5. Volver al Menú Principal\n')

        if co == '1':
            f=f+1
            idp = input("Ingrese el id del producto ")
            idc = input("Ingrese el id del cliente: ")
            fecha = input("Ingrese la fecha: ")
            cantidad = input('Ingrese la cantidad de venta: ')
            venta = [{"ID_Venta":f,"ID_Producto":idp ,"ID_Cliente":idc, "Fecha_Venta":fecha, "Cantidad":cantidad}]
            agregar_venta(venta)
            print(' \nAgregado con exito \n')

        elif co == '2':
            print('¿Que venta quiere buscar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >f:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es su id?')
                        ids = input()
                    if int(ids) <= f:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            mostrarv(ids)

        elif co == '3':
            print('¿Que venta quiere actualizar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >f:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es su id?')
                        ids = input()
                    if int(ids) <= f:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            nombre = input("Ingrese el nombre del proveedor: ")
            contacto = input("Ingrese el contacto del proveedor: ")
            direccion = input("Ingrese la direccion del proveedor: ")
            productos = [{"Nombre":nombre ,"Contacto":contacto, "Direccion":direccion}]
            actualizarp2(ids,productos)

        elif co == '4':
            print('¿Que venta quiere eliminar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >f:
                        print('Ese numero no corresponde a ninguna id registrada')
                        print('¿Cual es el id?')
                        ids = input()
                    if int(ids) <= f:
                        h = False
                except ValueError:
                    print('Por favor escriba un numero')
                    print('¿Cual es su id?')
                    ids = input()
            eliminarp2(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '4':
        co = input('\n1. Registrar Compra\n2. Buscar Compra\n3. Actualizar Compra\n4. Eliminar Compra\n5. Volver al Menú Principal\n')

    elif condicion == '5':
        co = input('\n1. Productos con menor stock\n2. Proveedores más frecuentes\n3. Ventas por período de tiempo\n4. Productos más vendidos\n')

    elif condicion == '6':
        print('\nSaliendo del sistema...')
        break