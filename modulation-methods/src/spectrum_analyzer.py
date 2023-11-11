import numpy as np

from .models import SpectrumAnalyzerParams


class SpectrumAnalyzer:
    def __init__(self, Uam, params: SpectrumAnalyzerParams):
        """
        Ініціалізує об'єкт аналізатора спектра з заданими параметрами.

        Parameters:
            - Uam (array): Масив модульованого сигналу.
            - params (SpectrumAnalyzerParams): Об'єкт, який містить параметри аналізатора спектра.
        """
        self.Uam = Uam
        self.f, self.P1 = self.analyze_spectrum(params)

    def analyze_spectrum(self, params: SpectrumAnalyzerParams):
        """
        Аналізує спектр модульованого сигналу.

        Parameters:
            - params (SpectrumAnalyzerParams): Параметри аналізатора спектра.

        Returns:
            - f (array): Масив частот.
            - P1 (array): Масив амплітуд спектру.
        """
        Fs = (
            1 / params.dt
        )  # Визначення частоти дискретизації (Fs) за допомогою обраного параметра часу дискретизації (params.dt).
        T = (
            1 / Fs
        )  # Визначення періоду дискретизації (T) на основі частоти дискретизації (Fs).
        L = (
            int(Fs * params.tkinc) + 1
        )  # Визначення довжини сигналу (L) на основі частоти дискретизації (Fs) та тривалості сигналу (params.tkinc).
        t = (
            np.arange(0, L) * T
        )  # Створення часового вектора (t) від 0 до тривалості сигналу (params.tkinc) з кроком дискретизації (T).
        Y = np.fft.fft(
            self.Uam
        )  # Застосування швидкого перетворення Фур'є до модульованого сигналу (self.Uam) та отримання спектру (Y).
        P2 = np.abs(
            Y / L
        )  # Визначення амплітуд спектру (P2) за допомогою модуля комплексних значень спектру.
        P1 = P2[: (L // 2) + 1]  # Вибір половини спектру (позитивної частини)
        P1[1:-1] = (
            2 * P1[1:-1]
        )  # та масштабування на 2 для врахування інверсії зворотнього спектра.
        f = (
            Fs * np.arange((L // 2) + 1) / L
        )  # Створення масиву частот (f) для відображення амплітудного спектру від 0 до Fs / 2.

        return f, P1
