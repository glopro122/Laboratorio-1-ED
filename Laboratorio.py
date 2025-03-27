from classes import Compra, Venta, Producto, Proveedor

def Crear_Archivo_Productos(productos):
    with open('productos.csv', 'w') as file:
        keys = list(productos[0].keys())
        file.write(','.join(keys) + '\n')
        for producto in productos:
            file.write(
                f"{producto['ID_Producto']},{producto['Nombre']},{producto['Categoría']},{producto['Precio']},{producto['Stock']}\n"
            )

def escribir(doc, line):
    with open(doc,'a') as file:
        if isinstance(line, Producto):
            line_str = f"{line.id_producto},{line.nombre},{line.categoria},{line.precio},{line.stock}\n"
        elif isinstance(line, Compra):
            line_str = f"{line.id_compra},{line.id_producto},{line.id_proveedor},{line.fecha_compra},{line.cantidad}\n"
        elif isinstance(line, Venta):
            line_str = f"{line.id_venta},{line.id_producto},{line.id_cliente},{line.fecha_venta},{line.cantidad}\n"
        elif isinstance(line, Proveedor):
            line_str = f"{line.id},{line.nombre},{line.contacto},{line.direccion}\n"
        file.write(line_str)

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
    encon=False
    with open('productos.csv', 'r') as file:
        lines = file.readlines()
        j=0
        #for line in lines:
            #j=j+1
        with open('productos.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'ID_Producto' and int(v[0]) == int(id):
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

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
                    for i in proveedores:
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
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el proveedor')
                else:
                    file.write(line)

def resta(cantidad,id):
    z=True
    with open("productos.csv", 'r') as file:
        lines = file.readlines()
    with open("productos.csv", 'w') as file:
        for line in lines:   
            v =line.split(',')
            if v[0] == id:
                try:
                    stock_actual = int(v[4])
                    cantidad_vendida = int(cantidad)
                    if cantidad_vendida > stock_actual:
                        z=False
                        v[4] = "0" 
                    else:
                        v[4] = str(stock_actual - cantidad_vendida) 
                    linea = ",".join(v) + "\n"
                except (ValueError, IndexError):
                    linea = line
            else:
                linea = line 
            file.write(linea)

def suma(cantidad,id):
    with open("productos.csv", 'r') as file:
        lines = file.readlines()
    with open("productos.csv", 'w') as file:
        for line in lines:   
            v =line.split(',')
            if v[0] == id:
                nuevo_stock =  int(v[4]) + int(cantidad)   
                v[4]=str(nuevo_stock)
                linea = f"{v[0]},{v[1]},{v[2]},{v[3]},{v[4]}\n"
            else:
                linea = line 
            file.write(linea)
 
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
                v = line.strip().split(',')
                l=l+1
                if v[0] != 'ID_Venta' and int(v[0]) == int(id):
                    for i in venta:
                        file.write(str(v[0]) + ',' + i['ID_Producto'] + ',' + i['ID_Cliente'] + ',' + i['Fecha_Venta'] + ',' + i['Cantidad'] + '\n')
                        if int(v[4]) < int(cantidad):
                            resta(int(cantidad) - int(v[4]))
                        elif int(v[4]) > int(cantidad):
                            suma(int(v[4]) - int(cantidad),v[0])
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def eliminarv(id):
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
                if v[0] != 'ID_Venta' and int(v[0]) == int(id):
                    file.write('')
                    suma(int(v[4]),v[1])
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el proveedor')
                else:
                    file.write(line)

def productos_menor_stock():
    with open("productos.csv", 'r') as file:
        lines = file.readlines()
        productos = []
        for line in lines[1:]:
            v = line.strip().split(',')
            productos.append((v[1], int(v[4])))
            
        for i in range(len(productos)):
            for j in range(i + 1, len(productos)):
                if productos[i][1] > productos[j][1]:
                    productos[i], productos[j] = productos[j], productos[i]

        for producto in productos[:3]:
            print(f"Producto: {producto[0]}, Stock: {producto[1]}")

def proveedores_por_frecuencia():
    proveedores = {}
    with open("compras.csv", 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            v = line.strip().split(',')
            idprove = v[2]
            if idprove in proveedores:
                proveedores[idprove] += 1
            else:
                proveedores[idprove] = 1
    proveedores_lista = list(proveedores.items())
    for i in range(len(proveedores_lista)):
        for j in range(i + 1, len(proveedores_lista)):
            if proveedores_lista[i][1] < proveedores_lista[j][1]:
                proveedores_lista[i], proveedores_lista[j] = proveedores_lista[j], proveedores_lista[i]
    
    listaprove = list(proveedores.items())

    with open("proveedores.csv", 'r') as file:
        lines = file.readlines()
        proveedores_diccionario = {line.split(',')[0]: line.split(',')[1] for line in lines[1:]}
    
    for proveedor in listaprove[:3]:
        proveedor_nombre = proveedores_diccionario.get(proveedor[0], "Desconocido")
        print(f"Proveedor: {proveedor_nombre}, Frecuencia: {proveedor[1]}")

def ventas_por_tiempo():
    with open("ventas.csv", 'r') as file:
        lines = file.readlines()
        ventas = []
        for line in lines[1:]:
            v = line.strip().split(',')
            ventas.append((v[1], v[3], int(v[4])))

        for i in range(len(ventas)):
            for j in range(i + 1, len(ventas)):
                fecha_i = ventas[i][1].split('-')
                fecha_j = ventas[j][1].split('-')
                if (fecha_i[0] < fecha_j[0]) or \
                   (fecha_i[0] == fecha_j[0] and fecha_i[1] < fecha_j[1]) or \
                   (fecha_i[0] == fecha_j[0] and fecha_i[1] == fecha_j[1] and fecha_i[2] < fecha_j[2]):
                    ventas[i], ventas[j] = ventas[j], ventas[i]

        for venta in ventas[:3]:
            print(f"Producto ID: {venta[0]}, Fecha: {venta[1]}, Cantidad: {venta[2]}")

def productos_por_ventas():
    with open("ventas.csv", 'r') as file:
        lines = file.readlines()
        productos = {}
        for line in lines[1:]:
            v = line.strip().split(',')
            idproduc = v[1]
            cantidad = int(v[4])
            if idproduc in productos:
                productos[idproduc] += cantidad
            else:
                productos[idproduc] = cantidad

        productos_ordenados = []
        for idproduc in productos:
            cantidad = productos[idproduc]
            productos_ordenados.append((idproduc, cantidad))

        for i in range(len(productos_ordenados)):
            for j in range(i + 1, len(productos_ordenados)):
                if productos_ordenados[i][1] < productos_ordenados[j][1]:
                    productos_ordenados[i], productos_ordenados[j] = productos_ordenados[j], productos_ordenados[i]

        for producto in productos_ordenados[:3]:
            print(f"Producto ID: {producto[0]}, Cantidad Vendida: {producto[1]}")

def mostrarc(id):
    with open("compras.csv", 'r') as file:
        lines = file.readlines()
        j=0
        k=0
        for line in lines:
            j=j+1
        for line in lines:
            k=k+1
            v =line.split(',')
            if v[0] != 'ID_Compra' and int(v[0]) == int(id):
                print('La id de la compra es es: '+v[0]+'\nLa id del producto es: '+ v[1] + '\nEl id del proveedor es: ' + v[2]+'\nLa fecha de la compra es: '+v[3]+'\nLa cantidad de la compra es: '+v[4])                    
def actualizarc(ids,compras):
    with open('compras.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('compras.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                v = line.strip().split(',')
                l=l+1
                if v[0] != 'ID_Compra' and int(v[0]) == int(ids):
                    for i in compras:
                        file.write(str(v[0]) + ',' + i['ID_Compra'] + ',' +i['ID_Producto'] + ',' + i['ID_Proveedor'] + ',' + i['Fecha_Compra'] + ',' + i['Cantidad'] + '\n')
                        if int(v[5]) < int(cantidad):
                            resta(int(cantidad) - int(v[5]))
                        elif int(v[5]) > int(cantidad):
                            suma(int(v[5]) - int(cantidad),v[0])
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el producto')
                else:
                    file.write(line)

def validarFecha(fecha):
    try:
        fecha_i = fecha.split('/')
        año = int(fecha_i[0])
        mes = int(fecha_i[1])
        dia = int(fecha_i[2])
        if (año < 2000 or año > 2026) or (mes < 1 or mes > 12):
            return False
        dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dias_en_mes[1] = 29
        if (mes == 1 and dia > 31) or\
        (mes == 2 and dia > dias_en_mes[1]) or\
        (mes == 3 and dia > 31) or\
        (mes == 4 and dia > 30) or\
        (mes == 5 and dia > 31) or\
        (mes == 6 and dia > 30) or\
        (mes == 7 and dia > 31) or\
        (mes == 8 and dia > 31) or\
        (mes == 9 and dia > 30) or\
        (mes == 10 and dia > 31) or\
        (mes == 11 and dia > 30) or\
        (mes == 12 and dia > 31):
            return False
        return True
    except:
        print('Digite en el formato establecido, por favor')
        return False

def eliminarc(id):
    with open('compras.csv', 'r') as file:
        lines = file.readlines()
        j=0
        for line in lines:
            j=j+1
        with open('compras.csv', 'w') as file:
           l=0
           k=1
           for line in lines:
                l=l+1
                v =line.split(',')
                if v[0] != 'ID_Compra' and int(v[0]) == int(id):
                    file.write('')
                    resta(int(v[4]),v[1])
                    k = 0
                elif k != 0 and l==j:
                    file.write(line)
                    print('No se encontro el proveedor')
                else:
                    file.write(line)
producto = [
    {"ID_Producto": 1, "Nombre": "Laptop", "Categoría": "Electrónica", "Precio": 2000000, "Stock": 50},
    {"ID_Producto": 2, "Nombre": "Zapatos", "Categoría": "Calzado", "Precio": 270000, "Stock": 10},
    {"ID_Producto": 3, "Nombre": "Camiseta", "Categoría": "Ropa", "Precio": 50000, "Stock": 30},
    {"ID_Producto": 4, "Nombre": "Cuadernos", "Categoría": "Útiles", "Precio": 5000, "Stock": 10}
]

proveedore = [
    {"id":1, "Nombre":"TecnoSuministros S.A.", "Contacto":"contacto@tecnosuministros.com", "Direccion":"Calle 123 #45-67, Bogotá, Colombia"},
    {"id":2, "Nombre":"Calzados y Más", "Contacto":"info@calzadosymas.com", "Direccion":"Avenida Principal #98-76, Medellín, Colombia"},
    {"id":3, "Nombre":"Textiles Modernos", "Contacto":"ventas@textilesmodernos.com", "Direccion":"Carrera 56 #12-34, Cali, Colombia"},
    {"id":4, "Nombre":"Papelería Educativa", "Contacto":"servicio@papeleriaeducativa.com", "Direccion":"Calle 89 #10-11, Barranquilla, Colombia"}
]

venta = [
    {"ID_Venta": 1, "ID_Producto": 1, "ID_Cliente": 1, "Fecha_Venta": "2023-10-01", "Cantidad": "2"},
    {"ID_Venta": 2, "ID_Producto": 2, "ID_Cliente": 2, "Fecha_Venta": "2023-10-02", "Cantidad": "1"},
    {"ID_Venta": 3, "ID_Producto": 3, "ID_Cliente": 3, "Fecha_Venta": "2023-10-03", "Cantidad": "5"},
    {"ID_Venta": 4, "ID_Producto": 4, "ID_Cliente": 4, "Fecha_Venta": "2023-10-04", "Cantidad": "3"}
]

compra = [
    {"ID_Compra": 1, "ID_Producto": 1, "ID_Proveedor": 1, "Fecha_Compra": "2023-09-25", "Cantidad": "10"},
    {"ID_Compra": 2, "ID_Producto": 2, "ID_Proveedor": 2, "Fecha_Compra": "2023-09-26", "Cantidad": "20"},
    {"ID_Compra": 3, "ID_Producto": 3, "ID_Proveedor": 3, "Fecha_Compra": "2023-09-27", "Cantidad": "15"},
    {"ID_Compra": 4, "ID_Producto": 4, "ID_Proveedor": 4, "Fecha_Compra": "2023-09-28", "Cantidad": "30"}
]

Crear_Archivo_Productos(producto)
Crear_Archivo_Proveedores(proveedore)
Crear_Archivo_Ventas(venta)
Crear_Archivo_Compras(compra)
create_indexp()
create_indexp2()
create_indexv()
create_indexc()
c=4
k=4
f=4
y=4
j=4
for i in range(0, 99):
    create_indexp()
    create_indexp2()
    create_indexv()
    create_indexc()
    h = True
    ñ = True
    idp = ''
    condicion= input('¿Que desea hacer? \n1. Gestión de Productos \n2. Gestión de Proveedores \n3. Gestión de Ventas \n4. Gestión de Compras \n5. Reportes \n6. Salir\n')
    while int(condicion)< 1 or int(condicion) > 6:
        print ('Opción Inválida, digite nuevamente')
        condicion = input('¿Que desea hacer? \n1. Gestión de Productos \n2. Gestión de Proveedores \n3. Gestión de Ventas \n4. Gestión de Compras \n5. Reportes \n6. Salir\n')

    if condicion == '1':
        co = input('\n1. Registrar Producto\n2. Buscar Producto\n3. Actualizar Producto\n4. Eliminar Producto\n5. Volver al menú principal\n')
        if co == '1':
            k=k+1
            nombre = input("Ingrese el nombre del producto: ")
            while nombre  == '':
                nombre=input ('Nombre inválido, Digitelo nuevamente')
            categoria = input("Ingrese la categoría del producto: ")
            while categoria =='':
                categpria=input ('Catagoria inválida, Digitelo nuevamente')
            while True:
                precio = input("Ingrese el precio del producto: ")
                try:
                    precio_num = float(precio)
                    if precio_num >= 0:
                        break
                    else:
                        print('El precio no puede ser negativo')
                except ValueError:
                    print('Por favor ingrese un número válido para el precio')
            while True:
                stock = input("Ingrese el stock del producto: ")
                try:
                    stock_num = int(stock)
                    if stock_num >= 0:
                        break
                    else:
                        print('El stock no puede ser negativo')
                except ValueError:
                    print('Por favor ingrese un número entero válido para el stock') 
            producto = Producto(k, nombre , categoria, precio, stock)
            escribir('productos.csv',producto)
            print(' \nAgregado con exito \n')
        elif co == '2':
            ids = input('¿Que producto quiere buscar?')
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        ids = input('Id no valida \n'
                        'Digite nuevamete su id: ')
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            mostrarp(ids)

        elif co == '3':
            ids = input('¿Que producto quiere actualizar?')
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            nombre = input("Ingrese el nombre del producto: ")
            while nombre == '':
                nombre = input("Ingrese nuevamente el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            while categoria == '':
                categoria = input("Ingrese nuevamente la categoría del producto: ")
            while True:
                precio = input("Ingrese el precio del producto: ")
                try:
                    precio_num = float(precio)
                    if precio_num >= 0:
                        break
                    else:
                        print('El precio no puede ser negativo')
                except ValueError:
                    print('Por favor ingrese un número válido para el precio')
            while True:
                stock = input("Ingrese el stock del producto: ")
                try:
                    stock_num = int(stock)
                    if stock_num >= 0:
                        break
                    else:
                        print('El stock no puede ser negativo')
                except ValueError:
                    print('Por favor ingrese un número entero válido para el stock') 
            productos = [{"Nombre":nombre ,"Categoría":categoria, "Precio":precio, "Stock":stock}]
            actualizarp(ids,productos)

        elif co == '4':
            ids = input('¿Que producto quiere eliminar?')
            while h:
                try:
                    while ids == '' or int(ids) >k:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= k:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            eliminarp(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '2':
        co = input('\n1. Registrar Proveedor\n2. Buscar Proveedor\n3. Actualizar Proveedor\n4. Eliminar Proveedor\n5. Volver al Menú Principal\n')

        if co == '1':
            c=c+1
            nombre = input("Ingrese el nombre del proveedor: ")
            while nombre == '':
                nombre = input("Ingrese nuevamente el nombre del proveedor: ")
            contacto = input("Ingrese el contacto del proveedor: ")
            conta = contacto
            while ñ:
                try:
                    while contacto == '':
                        contacto = input("Ingrese nuevamente el contacto del proveedor: ")
                    while conta != '':
                        cont = contacto.split('@')
                        concon = cont[1]
                        con = concon.split('.')
                        if len(con[1]) >= 1:
                            ñ = False
                            conta = ''
                        else:
                            print('Digite un correo valido')
                            contacto = input()
                except IndexError:
                    print('Digite un correo valido')
                    contacto = input()
            direccion = input("Ingrese la direccion del proveedor: ")
            while direccion == '':
                direccion = input("Ingrese nuevamente la direccion del proveedor: ")
            nuevopro = Proveedor(c,nombre ,contacto, direccion)
            escribir('proveedores.csv',nuevopro)
            print(' \nAgregado con exito \n')

        elif co == '2':
            print('¿Que producto quiere buscar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            mostrarp2(ids)

        elif co == '3':
            print('¿Que proveedor quiere actualizar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            nombre = input("Ingrese el nombre del proveedor: ")
            while nombre == '':
                nombre = input("Ingrese nuevamente el nombre del proveedor: ")
            contacto = input("Ingrese el contacto del proveedor: ")
            conta = contacto
            while ñ:
                try:
                    while contacto == '':
                        contacto = input("Ingrese nuevamente el contacto del proveedor: ")
                    while conta != '':
                        cont = contacto.split('@')
                        concon = cont[1]
                        con = concon.split('.')
                        if len(con[1]) >= 1:
                            ñ = False
                            conta = ''
                        else:
                            print('Digite un correo valido')
                            contacto = input()
                except IndexError:
                    print('Digite un correo valido')
                    contacto = input()
            direccion = input("Ingrese la direccion del proveedor: ")
            while direccion == '':
                direccion = input("Ingrese nuevamente la direccion del proveedor: ")
            productos = [{"Nombre":nombre ,"Contacto":contacto, "Direccion":direccion}]
            actualizarp2(ids,productos)

        elif co == '4':
            print('¿Que proveedor quiere eliminar?')
            ids = input()
            while h:
                try:
                    while ids == '' or int(ids) >c:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= c:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id: ')
            eliminarp2(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '3':
        sisi=False
        co = input('\n1. Registrar Venta\n2. Buscar Venta\n3. Actualizar Venta\n4. Eliminar Venta\n5. Volver al Menú Principal\n')
        if co == '1':
            f=f+1
            while True:
                idp = input('Digite el ID del producto: ').strip()
                try:
                    idp_num = int(idp)
                    if idp_num <= 0:
                        print("Error: El ID debe ser positivo.")
                    else:
                        break 
                except ValueError:
                    print("Error: Ingrese un número válido para el ID.")
            while True:
                idc = input("Ingrese el ID del cliente: ").strip()
                try:
                    idc_num = int(idc)
                    if idc_num <= 0:
                        print("Error: El ID debe ser positivo.")
                    else:
                        break 
                except ValueError:
                    print("Error: Ingrese un número válido para el ID.")
            fecha = input ("Ingrese la fecha en el forma de Año, Mes y Dia, separandolos por un /: ")
            sisi=validarFecha(fecha)
            while sisi == False:
                fecha = input("Fecha inválida\n"
                "recuerde que la fecha debe de estar en formato YYYY/MM/DD: ")
                sisi=validarFecha(fecha) 
            while True:
                cantidad = input('Ingrese la cantidad de venta: ').strip()
                try:
                    cantidad_num = int(cantidad)
                    if cantidad_num <= 0:
                        print('Error: La cantidad debe ser mayor a 0.')
                    else:
                        break
                except ValueError:
                    print('Error: Ingrese un número entero válido.')
            venta = Venta(f, idp, idc, fecha, cantidad)
            escribir('ventas.csv',venta)
            po=resta(cantidad,idp)
            if po == False:
                print(f"Error: No hay suficiente stock. Disponible")
            else:
                print(' \nAgregado con exito \n')

        elif co == '2':
            ids = input('¿Que venta quiere buscar?')
            while h:
                try:
                    while ids == '' or int(ids) >f:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= f:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            mostrarv(ids)

        elif co == '3':
            while True:
                idp = input('Digite el ID del producto: ').strip()
                try:
                    idp_num = int(idp)
                    if idp_num <= 0:
                        print("Error: El ID debe ser positivo.")
                    elif idp_num > c: 
                        print(f"Error: El ID debe ser menor o igual a {c}.")
                    else:
                        break 
                except ValueError:
                    print("Error: Ingrese un número válido para el ID.")
            while True:
                idc = input("Ingrese el ID del cliente: ").strip()
                try:
                    idc_num = int(idc)
                    if idc_num <= 0:
                        print("Error: El ID debe ser positivo.")
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese un número válido para el ID.")
            while sisi == False:
                fecha = input("Ingrese la fecha\n"
                "Recuerde que la fecha debe de estar en formato YYYY/MM/DD: ")
                sisi=validarFecha(fecha) 
            while True:
                cantidad = input('Ingrese la cantidad de venta: ').strip()
                try:
                    cantidad_num = int(cantidad)
                    if cantidad_num <= 0:
                        print('Error: La cantidad debe ser mayor a 0.')
                    else:
                        break
                except ValueError:
                    print('Error: Ingrese un número entero válido.')
            ventas = [{"ID_Producto":idp ,"ID_Cliente":idc, "Fecha_Venta":fecha, "Cantidad":cantidad}]
            actualizarv(ids,ventas)

        elif co == '4':
            ids = input('¿Que venta quiere eliminar?')
            while h:
                try:
                    while ids == '' or int(ids) >f:
                        ids=input('Ese numero no corresponde a ninguna id registrada\n'
                        'Digite nuevamente su id: ')
                    if int(ids) <= f:
                        h = False
                except ValueError:
                    ids=input('Por favor escriba un numero\n'
                    'Digite su id')
            eliminarv(ids)

        elif co == '5':
            condicion = 0

    elif condicion == '4':
        co = input('\n1. Registrar Compra\n2. Buscar Compra\n3. Actualizar Compra\n4. Eliminar Compra\n5. Volver al Menú Principal\n')
        if co == '1':
            j=j+1
            idp = input("Ingrese el id del producto ")
            while idp == '' or int(idp)<0:
                idp = input("Id del producto inválido, ingrese nuevamente el id del producto, \n"
                "Recuerde que no es válido ingresar ids negativos ")
            idpr = input("Ingrese el id del proveedor: ")
            while idpr == '' or int(idpr)<0:
                idpr = input("Id del proveedor inválido, ingrese nuevamente el id del cliente: \n"
                "Recuerde que el id debe ser positivio")
            fecha = input("Ingrese la fecha: ")
            while fecha == '':
                fecha = input("Fecha inválida. ingrese nuevamente la fecha: ")
            while True:
                cantidad = input('Ingrese la cantidad de venta: ').strip()
                try:
                    cantidad_num = int(cantidad)
                    if cantidad_num <= 0:
                        print('Error: La cantidad debe ser mayor a 0.')
                    else:
                        break
                except ValueError:
                    print('Error: Ingrese un número entero válido.')
            compras = Compra(j, idp , idpr, fecha, cantidad)
            escribir('compras.csv',compras)
            suma(cantidad,idp)
            print(' \nAgregado con exito \n')
        elif co == '2':
            print('¿Que compra quiere buscar?')
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
                    print('Por favor escriba un número')
                    print('¿Cúal es su id?')
                    ids = input()
            mostrarc(ids)    
        elif co == '3':
            print('¿Que compra quiere actualizar?')
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
                try:
                    idc = input("Ingrese el id de la compra ")
                    while idc == '' or int(idc)<0:
                        idc = input("Id de la compra inválido, ingrese nuevamente el id del producto, \n"
                        "Recuerde que no es válido ingresar ids negativos ")
                except ValueError:
                    idc = input("Id de la compra inválido, ingrese nuevamente el id del producto, \n"
                    "Recuerde que no es válido ingresar ids negativos ")
            idp = input("Ingrese el id del producto: ")
            while idp == '' or int(idp)<0:
                idp = input("Id del producto inválido, ingrese nuevamente el id del producto, \n"
                "Recuerde que no es válido ingresar ids negativos ")
            idpr = input("Ingrese el id del proveedor: ")
            while idpr == '' or int(idc)<0:
                idpr = input("Id del cliente inválido, ingrese nuevamente el id del cliente: \n"
                "Recuerde que el id debe ser positivio")
            fecha = input("Ingrese la fecha: ")
            while fecha == '':
                fecha = input("Fecha inválida. ingrese nuevamente la fecha: ")
            while True:
                cantidad = input('Ingrese la cantidad de venta: ').strip()
                try:
                    cantidad_num = int(cantidad)
                    if cantidad_num <= 0:
                        print('Error: La cantidad debe ser mayor a 0.')
                    else:
                        break
                except ValueError:
                    print('Error: Ingrese un número entero válido.')
            compras = [{"ID_Compra":idc,"ID_Producto":idp ,"ID_Proveedor":idpr, "Fecha_Compra":fecha, "Cantidad":cantidad}]
            actualizarc(ids,compras)   
        elif co == '4':
            print('¿Que Compra quiere eliminar?')
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
            eliminarc(ids)
        elif co == '5':
            condicion=0

    elif condicion == '5':
        co = input('\n1. Productos con menor stock\n2. Proveedores más frecuentes\n3. Ventas por período de tiempo\n4. Productos más vendidos\n')
        if co == '1':
            productos_menor_stock()
        elif co == '2':
            proveedores_por_frecuencia()

        elif co == '3':
            ventas_por_tiempo()

        elif co == '4':
            productos_por_ventas()
    elif condicion == '6':
        print('\nSaliendo del sistema...')
        break