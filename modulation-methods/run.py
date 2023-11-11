from src.models import PlotterParams, SignalParams, SpectrumAnalyzerParams
from src.plotter import Plotter
from src.signal_generator import SignalGenerator
from src.spectrum_analyzer import SpectrumAnalyzer


def main() -> None:
    # Параметри сигналу
    signal_params = SignalParams()
    spectrum_analyzer_params = SpectrumAnalyzerParams()
    plotter_params = PlotterParams()

    # Створення об'єкта генератора сигналу
    signal_generator = SignalGenerator(signal_params)
    U0, Uinf, Uam = signal_generator.generate_signals()

    # Створення об'єкта аналізатора спектра
    spectrum_analyzer = SpectrumAnalyzer(Uam, spectrum_analyzer_params)

    # Створення об'єкта для побудови графіків
    plotter = Plotter()

    # Побудова графіків
    plotter.plot_spectral_content(spectrum_analyzer.f, spectrum_analyzer.P1)
    plotter.plot_comparison_signal(signal_generator.t, U0, Uinf, plotter_params)
    plotter.plot_information_signal(signal_generator.t, Uinf, plotter_params)
    plotter.plot_modulated_signal(signal_generator.t, Uam, plotter_params)


if __name__ == "__main__":
    main()
