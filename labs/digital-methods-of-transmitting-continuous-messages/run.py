import numpy as np
from src.SignalQuantizer import SignalQuantizer
from src.SignalPlotter import SignalPlotter


def main() -> None:
    # Параметри сигналу
    dt: float = 0.05
    t: np.ndarray = np.arange(0, 2 * np.pi, dt)
    mp: float = 0.5
    L: int = 16

    # Створення об'єкту квантування
    quantizer: SignalQuantizer = SignalQuantizer(mp, L)

    # Створення об'єкту для відображення сигналу
    plotter: SignalPlotter = SignalPlotter()

    # Створення оригінального сигналу
    sig: np.ndarray = mp * np.sin(t)

    # Квантування сигналу
    quants: np.ndarray = quantizer.quantize_signal(sig)

    # Зберігання графіка оригінального та квантованого сигналу
    plotter.plot_original_and_quantized(t, sig, quants)

    # Зберігання графіка шуму квантування
    quantization_noise: np.ndarray = quants - sig
    plotter.plot_quantization_noise(t, quantization_noise)


if __name__ == "__main__":
    main()
