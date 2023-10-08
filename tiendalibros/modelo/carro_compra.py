from tiendalibros.modelo.item_compra import ItemCompra
from tiendalibros.modelo.libro import Libro

class CarroCompras:

    def __init__(self):
        self.item: list[ItemCompra] = []

    def agregar_item(self, libro: Libro, cantidad: int):
        item: ItemCompra = ItemCompra(libro, cantidad)
        self.item.append(item)
        return item
    

    def calcular_total(self)-> float:
        total = 0
        for item in self.item:
            total += item.calcular_subtotal()
        return total


    def quitar_item(self, isbn: str):
        self.item = [i for i in self.item if i.libro.isbn != isbn]
        return self.item
    