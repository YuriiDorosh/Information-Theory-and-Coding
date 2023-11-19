import matplotlib.pyplot as plt
import numpy as np
from .settings import SaveGraphic

file_path = SaveGraphic()


class SignalPlotter:
    def plot_original_and_quantized(
        self, t: np.ndarray, sig: np.ndarray, quants: np.ndarray
    ) -> None:
        plt.figure()
        plt.plot(t, sig, "x", label="Оригінальний сигнал")
        plt.stem(t, quants, "r", markerfmt="r.", label="Квантований сигнал")
        plt.legend()
        plt.xlabel("Час")
        plt.ylabel("Амплітуда")
        plt.title("Графік оригінального та квантованого сигналу")
        plt.savefig(file_path.path("Графік_оригінального_та_квантованого_сигналу.png"))

    def plot_quantization_noise(
        self, t: np.ndarray, quantization_noise: np.ndarray
    ) -> None:
        plt.figure()
        plt.plot(t, quantization_noise)
        plt.xlabel("Час")
        plt.ylabel("Помилка квантування")
        plt.title("Графік шуму квантування")
        plt.savefig(file_path.path("Графік_шуму_квантування.png"))
