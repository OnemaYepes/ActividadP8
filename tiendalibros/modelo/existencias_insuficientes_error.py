from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro import Libro


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro: Libro, cantidad_a_comprar: int):
        super().__init__(libro)
        self.cantidad_a_comprar = cantidad_a_comprar


    def __str__(self) -> str:
        return f"El libro con título {self.libro.titulo} e isbn {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}"
