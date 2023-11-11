import sys
from typing import List

from validator import check_integer


class ListAction:
    def __init__(
        self,
        size_of_the_square_matrix: int = None,
        width: int = None,
        length: int = None,
    ) -> None:
        """Елемент конструктура(ініціалізація) з вхідними параметрами:

        'size_of_the_square_matrix'(необов`язковий, типу int) - розмірність квадратної матриці,
        'width'(необов`язковий, типу int) - ширина матриці,
        'length' (необов`язковий, типу int) - довжина матриці
        """

        if width and length:
            if check_integer(width):
                if check_integer(length):
                    self.width = width
                    self.length = length
        elif size_of_the_square_matrix:
            if check_integer(size_of_the_square_matrix):
                self.N = size_of_the_square_matrix
        else:
            print(
                "Ви повинні передати параметрами, або 'size_of_the_square_matrix', або 'width' та 'length'."
            )
            sys.exit()

    @classmethod
    def create_with_size(cls, size_of_the_square_matrix: int) -> "ListAction":
        """Фабричний метод для створення об'єкту з розміром квадратної матриці."""

        return cls(size_of_the_square_matrix=size_of_the_square_matrix)

    @classmethod
    def create_with_dimensions(cls, width: int, length: int) -> "ListAction":
        """Фабричний метод для створення об'єкту з шириною і довжиною матриці."""

        return cls(width=width, length=length)

    def _create_square_multiply_array(self) -> List[int]:
        """Метод, який строрює масив розміром N на N та заповнює його добутками рядків та стовпців"""

        N = self.N

        multiply_array = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                multiply_array[i][j] = 3 * ((i + 1) + (j + 1) - 2 * (i + 1))

        multiply_array[N - 1][N - 1] = N * N
        return multiply_array

    def _create_multiply_array(self) -> List[int]:
        """Тут має бути метод, який НЕ квадратну матрицю"""
        pass

    def _extract_unique_elements(self) -> List[int]:
        """Метод, який 'фільтрує' матрицю та залишає тільки унікальні значення у вигляді списку int."""

        input_matrix = self._create_square_multiply_array()

        input_list = [item for row in input_matrix for item in row]

        unique_list = list(set(input_list))

        return unique_list
