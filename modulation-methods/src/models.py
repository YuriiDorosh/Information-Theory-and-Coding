from pydantic import BaseModel


class SignalParams(BaseModel):
    """
    Параметри сигналу.

    dt: Крок часу
    t0: Початок часу
    tkinc: Кінець часу
    u0: Амплітуда опорного сигналу
    uinf: Амплітуда інформаційного сигналу
    M: Коефіцієнт амплітудної модуляції
    F1inf: Частота інформаційного сигналу
    fi1: Фаза інформаційного сигналу
    F2op: Частота опорного сигналу
    fi0: Фаза опорного сигналу
    """

    dt: float = 0.001
    t0: float = 0
    tkinc: float = 5
    u0: float = 5
    uinf: float = 1.5
    M: float = 0.3
    F1inf: float = 50
    fi1: float = 45
    F2op: float = 200
    fi0: float = 10


class SpectrumAnalyzerParams(BaseModel):
    """Параметри аналізатора спектра."""

    dt: float = 0.001
    tkinc: float = 5


class PlotterParams(BaseModel):
    """Параметри графіка."""

    t_range_start: float = 0
    t_range_end: float = 2
