import numpy as np

from .models import SignalParams


class SignalGenerator:
    def __init__(self, params: SignalParams):
        """
        Ініціалізує об'єкт генератора сигналу з заданими параметрами.

        Parameters:
            - params (SignalParams): Об'єкт, який містить параметри сигналу.
        """
        self.params = params
        self.t = np.arange(
            self.params.t0, self.params.tkinc + self.params.dt, self.params.dt
        )
        self.omega1 = self.params.F1inf * 2 * np.pi
        self.omega0 = self.params.F2op * 2 * np.pi
        self.rad = np.pi / 180

    def generate_signals(self):
        """
        Генерує опорний, інформаційний та модульований сигнали.

        Returns:
            - U0 (array): Опорний сигнал.
            - Uinf (array): Інформаційний сигнал.
            - Uam (array): Модульований сигнал.
        """
        U0 = self.generate_base_signal()
        Uinf = self.generate_information_signal()
        Uam = self.modulate_signal(U0, Uinf)

        return U0, Uinf, Uam

    def generate_base_signal(self):
        """
        Генерує опорний сигнал.

        Returns:
            - U0 (array): Опорний сигнал.
        """
        return self.params.u0 * np.cos(
            self.omega0 * self.t + self.params.fi0 * self.rad
        )

    def generate_information_signal(self):
        """
        Генерує інформаційний сигнал.

        Returns:
            - Uinf (array): Інформаційний сигнал.
        """
        return self.params.uinf * np.cos(
            self.omega1 * self.t + self.params.fi1 * self.rad
        )

    def modulate_signal(self, U0, Uinf):
        """
        Модулює сигнал.

        Parameters:
            - U0 (array): Опорний сигнал.
            - Uinf (array): Інформаційний сигнал.

        Returns:
            - Uam (array): Модульований сигнал.
        """
        A = 1 + self.params.M * Uinf
        return A * U0
