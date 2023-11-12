from src.builders.concrete_builders import ConcreteFourierBuilder, ConcreteSignalBuilder
from src.plotter import Plotter
from src.signals.directors import SignalDirector


def get_user_input() -> dict[float]:
    """
    Функція для отримання введених користувачем параметрів сигналу.
    Повертає словник із введеними значеннями або значеннями за замовчуванням.
    """
    user_input = input(
        "Введіть 'y' для введення параметрів або будь-яку іншу клавішу для використання значень за замовчуванням: "
    )

    if user_input.lower() == "y":
        # Параметри сигналу
        dt = float(input("Інтервал дискретизації (час між вимірами сигналу): "))
        t0 = float(input("Початковий момент часу: "))
        tkinc = float(input("Кінцевий момент часу: "))
        U0 = float(input("Амплітуда опорного сигналу: "))
        Uinf = float(input("Амплітуда інформаційного сигналу: "))
        beta = float(input("Коефіцієнт частотної модуляції: "))
        F1inf = float(input("Частота інформаційного сигналу: "))
        fi1 = float(input("Фаза інформаційного сигналу: "))
        F2op = float(input("Частота опорного сигналу: "))
        fi0 = float(input("Фаза опорного сигналу: "))
    else:
        # Значення за замовчуванням
        dt = 0.001
        t0 = 0
        tkinc = 0.5
        U0 = 4
        Uinf = 2
        beta = 1
        F1inf = 5
        fi1 = 0
        F2op = 10**2
        fi0 = 0

    return {
        "dt": dt,
        "t0": t0,
        "tkinc": tkinc,
        "U0": U0,
        "Uinf": Uinf,
        "beta": beta,
        "F1inf": F1inf,
        "fi1": fi1,
        "F2op": F2op,
        "fi0": fi0,
    }


def main() -> None:
    """
    Основна функція для обчислення та відображення сигналів.
    """
    # Отримання параметрів від користувача або використання значень за замовчуванням
    user_params = get_user_input()

    # Створення будівельника сигналу
    signal_builder = ConcreteSignalBuilder(
        user_params["dt"],
        user_params["t0"],
        user_params["tkinc"],
        user_params["U0"],
        user_params["Uinf"],
        user_params["beta"],
        user_params["F1inf"],
        user_params["fi1"],
        user_params["F2op"],
        user_params["fi0"],
    )

    # Створення будівельника для обчислення Фур'є
    fourier_builder = ConcreteFourierBuilder()

    # Створення директора сигналу
    director = SignalDirector(signal_builder)

    # Створення сигналів
    (
        oporniy_signal,
        informatsiyniy_signal,
        modulovaniy_signal,
    ) = director.construct_signal()

    # Створення плотера
    plotter = Plotter(fourier_builder)

    # Побудова графіків
    plotter.plot_signals(oporniy_signal, informatsiyniy_signal, modulovaniy_signal)


if __name__ == "__main__":
    main()
