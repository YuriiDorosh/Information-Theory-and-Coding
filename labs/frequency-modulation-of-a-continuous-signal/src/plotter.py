import matplotlib.pyplot as plt

from src.builders.builders import FourierBuilder
from src.signals import Signal

from .settings import SaveGraphic

file_path = SaveGraphic()


class Plotter:
    def __init__(self, fourier_builder: FourierBuilder) -> None:
        self.fourier_builder = fourier_builder

    def plot_signals(
        self,
        oporniy_signal: Signal,
        informatsiyniy_signal: Signal,
        modulovaniy_signal: Signal,
    ) -> None:
        # Графік 1
        plt.figure()
        f, P1 = self.fourier_builder.compute_fft(modulovaniy_signal)
        plt.plot(f, P1)
        plt.title("Спектральний склад ЧМ сигналу")
        plt.xlabel("f (Hz)")
        plt.ylabel("|P1(f)|")
        plt.savefig(file_path.path("графік_спектральний_склад"))

        # Графік 2
        plt.figure()
        plt.plot(oporniy_signal.t, oporniy_signal.values)
        plt.title("Опорний сигнал")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid(True)
        plt.plot(informatsiyniy_signal.t, informatsiyniy_signal.values, "r")
        plt.legend()
        plt.savefig(file_path.path("графік_опорний"))

        # Графік 3
        plt.figure()
        plt.plot(informatsiyniy_signal.t, informatsiyniy_signal.values)
        plt.title("Інформаційний сигнал")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid(True)
        plt.savefig(file_path.path("графік_інформаційний"))

        # Графік 4
        plt.figure()
        plt.plot(modulovaniy_signal.t, modulovaniy_signal.values)
        plt.title("Модульований сигнал")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid(True)
        plt.savefig(file_path.path("графік_модульований"))
