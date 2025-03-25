class Compra:
    def __init__(self, id_compra, id_producto, id_proveedor, fecha_compra, cantidad):
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.id_proveedor = id_proveedor
        self.fecha_compra = fecha_compra
        self.cantidad = cantidad

    def __repr__(self):
        return f"Compra({self.id_compra}, {self.id_producto}, {self.id_proveedor}, {self.fecha_compra}, {self.cantidad})"

class Venta:
    def __init__(self, id_venta, id_producto, id_cliente, fecha_venta, cantidad):
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.fecha_venta = fecha_venta
        self.cantidad = cantidad

    def __repr__(self):
        return f"Venta({self.id_venta}, {self.id_producto}, {self.id_cliente}, {self.fecha_venta}, {self.cantidad})"

class Producto:
    def __init__(self, id_producto, nombre, categoria, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.id_producto}, {self.nombre}, {self.categoria}, {self.precio}, {self.stock})"

class Proveedor:
    def __init__(self, id, nombre, contacto, direccion):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    def __repr__(self):
        return f"Proveedor({self.id}, {self.nombre}, {self.contacto}, {self.direccion})"