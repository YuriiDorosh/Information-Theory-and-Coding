import numpy as np

from src.builders.builders import FourierBuilder, SignalBuilder
from src.signals import Signal


class ConcreteSignalBuilder(SignalBuilder):
    def __init__(
        self,
        dt: float,
        t0: float,
        tkinc: float,
        U0: float,
        Uinf: float,
        beta: float,
        F1inf: float,
        fi1: float,
        F2op: float,
        fi0: float,
    ):
        self.dt = dt
        self.t0 = t0
        self.tkinc = tkinc
        self.U0 = U0
        self.Uinf = Uinf
        self.beta = beta
        self.F1inf = F1inf
        self.fi1 = fi1
        self.F2op = F2op
        self.fi0 = fi0

    def build_oporniy_signal(self) -> Signal:
        t = np.arange(self.t0, self.tkinc + self.dt, self.dt)
        values = self.U0 * np.cos(2 * np.pi * self.F2op * t + np.radians(self.fi0))
        return Signal(t, values)

    def build_informatsiyniy_signal(self) -> Signal:
        t = np.arange(self.t0, self.tkinc + self.dt, self.dt)
        values = self.Uinf * np.cos(2 * np.pi * self.F1inf * t + np.radians(self.fi1))
        return Signal(t, values)

    def build_modulovaniy_signal(self) -> Signal:
        t = np.arange(self.t0, self.tkinc + self.dt, self.dt)
        omega1 = 2 * np.pi * self.F1inf
        omega0 = 2 * np.pi * self.F2op
        values = self.U0 * np.cos(
            omega0 * t
            + self.beta * omega0 / omega1 * np.sin(omega1 * t + np.radians(self.fi1))
        )
        return Signal(t, values)


class ConcreteFourierBuilder(FourierBuilder):
    def compute_fft(self, signal: Signal) -> tuple:
        Fs = 1 / (signal.t[1] - signal.t[0])
        L = len(signal.t)
        Y = np.fft.fft(signal.values)
        P2 = np.abs(Y / L)
        P1 = P2[: (L // 2) + 1]
        P1[1:-1] = 2 * P1[1:-1]
        f = Fs * np.arange((L // 2) + 1) / L
        return f, P1
