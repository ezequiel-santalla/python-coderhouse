from primer_paquete.cliente import Cliente

cliente1 = Cliente("Juan", 25, "Juan 5000", "juan@gmail.com")
cliente1.agregar_producto_al_carrito("Producto1")
cliente1.agregar_producto_al_carrito("Producto2")
cliente1.realizar_compra()

print(cliente1)