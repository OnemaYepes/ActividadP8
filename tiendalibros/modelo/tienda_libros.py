from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError


class TiendaLibros:

    def __init__(self):
        self.catalogo: dict [Libro.isbn, Libro] = {}
        self.carrito: CarroCompras = CarroCompras()        

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int)->Libro:
        if isbn in self.catalogo.keys():
            raise LibroExistenteError("Este libro ya se encuentra en el catálogo...")
        else:
            libro = Libro(isbn, titulo, precio, existencias)
            self.catalogo[isbn] = libro
            return libro
        

    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        if libro.existencias == 0:
            raise LibroAgotadoError("Este libro se encuentra agotado...")
        elif libro.existencias < cantidad:
            raise ExistenciasInsuficientesError("Este libro tiene poca existencia...")
        else:
            self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)