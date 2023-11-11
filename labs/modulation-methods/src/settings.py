class SaveGraphic:
    """
    Клас для збереження графіків у визначену теку.

    Attributes:
        path_to_graphics (str): Шлях до теки для збереження графіків.
        files_type (str): Тип файлів графіків.
    """

    path_to_graphics: str = "graphs/"
    files_type: str = ".png"

    def path(self, name_of_graph: str) -> str:
        """
        Генерує повний шлях до файла графіку з вказаним ім'ям.

        Args:
            name_of_graph (str): Ім'я графіку.

        Returns:
            str: Повний шлях до файла графіку.
        """
        return self.path_to_graphics + name_of_graph + self.files_type
