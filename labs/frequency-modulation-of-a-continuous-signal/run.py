from src.builders.concrete_builders import (ConcreteFourierBuilder,
                                            ConcreteSignalBuilder)
from src.plotter import Plotter
from src.signals.directors import SignalDirector


def main() -> None:
    """
    Основна функція для обчислення та відображення сигналів.
    """

    # Параметри сигналу
    dt = 0.001  # Інтервал дискретизації (час між вимірами сигналу)
    t0 = 0  # Початковий момент часу
    tkinc = 0.5  # Кінцевий момент часу
    U0 = 4  # Амплітуда опорного сигналу
    Uinf = 2  # Амплітуда інформаційного сигналу
    beta = 1  # Коефіцієнт частотної модуляції
    F1inf = 5  # Частота інформаційного сигналу
    fi1 = 0  # Фаза інформаційного сигналу
    F2op = 10**2  # Частота опорного сигналу
    fi0 = 0  #  Фаза опорного сигналу

    # Створення будівельника сигналу
    signal_builder = ConcreteSignalBuilder(
        dt, t0, tkinc, U0, Uinf, beta, F1inf, fi1, F2op, fi0
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
