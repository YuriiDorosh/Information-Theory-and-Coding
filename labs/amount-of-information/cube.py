import math
import sys

from list import ListAction
from validator import check_integer


class Cube:
    information_quantity_x1x1: int | float = 0
    information_quantity_yy: int | float = 0
    information_quantity_x1y: int | float = 0

    def __init__(self, sides: int) -> None:
        """Елемент конструктура(ініціалізація) з вхідним параметром 'sides'(типу int) - сторони кубика"""

        if check_integer(sides):
            self._sides = sides

        self.matrix = ListAction.create_with_size(size_of_the_square_matrix=self._sides)

    def _calculate_probability_of_number(
        self,
    ) -> int:
        """Обчислення закону розподілу ймовірностей для дискретних випадкових величин x1 та x2"""

        return 1 / self._sides

    def _calculate_information_quantity_x1x1(self) -> float:
        """Обчислення I(x1, x1)"""

        self.print_line()
        self.print_method_name("I(x1, x1)")

        for i in range(1, self._sides + 1):
            pi = self._calculate_probability_of_number()
            print(f"Для x1 = {i} --- pi = {pi}")

            self.information_quantity_x1x1 -= pi * math.log2(pi)

        return self.information_quantity_x1x1

    def print_information_quantity_x1x1(self) -> print:
        """Вивід I(x1, x1)"""

        print(f"\nI(x1, x1): {self._calculate_information_quantity_x1x1()}\n")

    def _calculate_information_quantity_yy(self) -> float:
        """Обчислення I(y, y)"""

        yy_sides = self._sides * self._sides

        self.print_line()
        self.print_method_name("I(y, y)")

        square_matrix = self.matrix._create_square_multiply_array()
        unique_elements = self.matrix._extract_unique_elements()

        print(f"Елементи(без повторів): {unique_elements}")

        probabilities = []

        for x in unique_elements:
            count_x = sum(row.count(x) for row in square_matrix)
            prob_x = count_x / yy_sides
            probabilities.append(prob_x)

        for i in probabilities:
            self.information_quantity_yy -= i * math.log2(i)

        print(f"\nЙмовірності(кількість повторів / {yy_sides}): {probabilities}\n")
        print(
            f"\nСума ймовірностей(кількість повторів / {yy_sides}): {sum(probabilities)}\n"
        )

        if sum(probabilities) != 1:
            print("Виникла помилка в обрахунках!")
            sys.exit()

        return self.information_quantity_yy

    def print_information_quantity_yy(self) -> print:
        """Вивід I(y, y)"""

        print(f"\nI(y, y): {self._calculate_information_quantity_yy()}\n")

    def _calculate_information_quantity_x1y(self) -> int | float:
        """Обчислення I(x1, y)"""

        self.print_line()
        self.print_method_name("I(x1, y)")

        unique_elements = self.matrix._extract_unique_elements()

        matrix_x1y = []

        for y in unique_elements:
            row = []
            for x1 in range(1, self._sides + 1):
                y_over_3 = y / 3

                if y_over_3 - x1 != 0:
                    value = y / (y_over_3 - x1)
                else:
                    row.append(0)

                if 1 <= value <= self._sides and int(value) == value:
                    row.append(1 / self._sides)
                else:
                    row.append(0)
            matrix_x1y.append(row)

        print(
            f"Таблиця(x1, y) з умовою : x2 = y /((y / 3) / x1) у межах від 1 до {self._sides} ---> "
        )
        print("-" * 150)
        print(matrix_x1y)
        print("-" * 150)

        self.information_quantity_x1y = (
            self.information_quantity_yy - self.information_quantity_x1x1
        )

        return self.information_quantity_x1y

    def print_information_quantity_x1y(self) -> print:
        """Вивід I(x1, y)"""

        print(f"\nI(x1, y): {self._calculate_information_quantity_x1y()}\n")

    def print_data(self) -> print:
        print(
            f"Кубики:\n  грань = {self._sides},\n  m * n = {self._sides ** 2},\n  y = 3 * (x1 + x2) - 2 * x1"
        )

    def print_conclusion(self) -> print:
        self.print_line()
        print("Усі I: ")
        print(
            f"I(x1,x1) = {self.information_quantity_x1x1}\nI(y, y) = {self.information_quantity_yy}\nI(x1, y) = {self.information_quantity_x1y}"
        )

    @staticmethod
    def print_line() -> print:
        """Вивід стрічки зі зірочок для облегшення читаємості"""

        print("\n" + "*" * 150 + "\n")

    @staticmethod
    def print_method_name(method_name: str) -> print:
        """Вивід назви методу"""

        print(f"          Обчислення {method_name}:\n")

    def run(self) -> None:
        self.print_line()
        self.print_data()
        self.print_information_quantity_x1x1()
        self.print_information_quantity_yy()
        self.print_information_quantity_x1y()
        self.print_conclusion()
