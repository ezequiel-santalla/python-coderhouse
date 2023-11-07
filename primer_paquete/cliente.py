class Cliente:
  def __init__(self, nombre, edad, direccion, email):
    self.nombre = nombre
    self.edad = edad
    self.direccion = direccion
    self.email = email
    self.carrito_compras = []

  def agregar_producto_al_carrito(self, producto):
    self.carrito_compras.append(producto)
    print(f"{producto} agregado al carrito de {self.nombre}.")

  def realizar_compra(self):
    if len(self.carrito_compras) > 0:
      print(f"{self.nombre} ha realizado la compra de los siguientes productos:")
      for producto in self.carrito_compras:
        print(f"- {producto}")
      print("¡Compra realizada con éxito!")
      self.carrito_compras = []
    else:
      print(f"{self.nombre}, el carrito de compras está vacío. ¡Agrega productos primero!")

  def __str__(self):
    return f"Cliente: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Email: {self.email}"
