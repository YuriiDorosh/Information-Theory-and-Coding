import sys


def check_integer(value) -> bool | None:
    """Функція для перевірки, чи значення є цілим числом."""

    try:
        int(value)
        return True
    except ValueError as e:
        print(e)
        sys.exit()
