import matplotlib.pyplot as plt

from .models import PlotterParams
from .settings import SaveGraphic

file_path = SaveGraphic()


class Plotter:
    @staticmethod
    def plot_spectral_content(f, P1):
        """
        Створює графік спектрального складу сигналу.

        Parameters:
            - f (array): Масив частот.
            - P1 (array): Масив амплітуд спектру.

        Returns:
            None
        """
        plt.figure()
        plt.plot(f, P1)
        plt.title("Cпектральний склад однотонального АМ коливання")
        plt.xlabel("f (Hz)")
        plt.ylabel("|P1(f)|")
        plt.savefig(file_path.path("графік_спектральний_склад"))

    @staticmethod
    def plot_comparison_signal(t, U0, Uinf, params: PlotterParams):
        """
        Створює графік порівняння опорного та інформаційного сигналів.

        Parameters:
            - t (array): Масив часових значень.
            - U0 (array): Масив опорного сигналу.
            - Uinf (array): Масив інформаційного сигналу.
            - params (PlotterParams): Параметри графіка.
        """
        new_t_range = (t >= params.t_range_start) & (t <= params.t_range_end)
        plt.figure()
        plt.plot(t[new_t_range], U0[new_t_range], label="Опорний сигнал")
        plt.title("Опорний сигнал з інформаційним (порівняння)")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid()
        plt.plot(t[new_t_range], Uinf[new_t_range], "r", label="Інформаційний сигнал")
        plt.legend()
        plt.savefig(file_path.path("графік_опорний_інформаційний"))

    @staticmethod
    def plot_information_signal(t, Uinf, params: PlotterParams):
        """
        Створює графік інформаційного сигналу.

        Parameters:
            - t (array): Масив часових значень.
            - Uinf (array): Масив інформаційного сигналу.
            - params (PlotterParams): Параметри графіка.

        Returns:
            None
        """
        new_t_range = (t >= params.t_range_start) & (t <= params.t_range_end)
        plt.figure()
        plt.plot(t[new_t_range], Uinf[new_t_range])
        plt.title("Інформаційний сигнал")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid()
        plt.savefig(file_path.path("графік_інформаційний"))

    @staticmethod
    def plot_modulated_signal(t, Uam, params: PlotterParams):
        """
        Створює графік модульованого сигналу.

        Parameters:
            - t (array): Масив часових значень.
            - Uam (array): Масив модульованого сигналу.
            - params (PlotterParams): Параметри графіка.

        Returns:
            None
        """

        new_t_range = (t >= params.t_range_start) & (t <= params.t_range_end)
        plt.figure()
        plt.plot(t[new_t_range], Uam[new_t_range])
        plt.title("Модульований сигнал")
        plt.xlabel("час")
        plt.ylabel("амплітуда")
        plt.grid()
        plt.savefig(file_path.path("графік_модульований"))
