"""Challenge 9 de Python.
    Reto a resolver
    Entrada: [1,0,2,3,0,4,5,0]
    Salida: None
    Why?: Después de llamar tu función, el arreglo de entrada es modificado para formar [1,0,0,2,3,0,0,4].
    Ejemplo 2:

    Entrada: [1, 2, 3]
    Salida: None
    Why?: Después de llamar tu función, el arreglo de entrada es modificado para formar [1,2,3].
"""
from typing import List


class Solution:
    """Clase de la solución."""

    def duplicate_zeros(self, arr: List[int]):
        """Función que duplica los 0s sin alterar la memoria utilizada."""
        indice = 0
        while indice < len(arr):
            if arr[indice] == 0:
                arr.pop()
                arr.insert(indice, 0)
                indice = indice + 1
            indice = indice + 1
