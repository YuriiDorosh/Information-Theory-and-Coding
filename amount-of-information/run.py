from cube import Cube

if __name__ == "__main__":
    while True:
        try:
            sides_num = int(input("Введіть кількість граней кубиків: "))
            break
        except ValueError:
            print("Помилка: Введені дані повинні бути цілим числом. Спробуйте ще раз.")

    cube = Cube(sides=sides_num)
    cube.run()
