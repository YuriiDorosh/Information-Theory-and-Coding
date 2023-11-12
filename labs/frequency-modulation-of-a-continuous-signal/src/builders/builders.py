from abc import ABC, abstractmethod

from src.signals import Signal


class SignalBuilder(ABC):
    @abstractmethod
    def build_oporniy_signal(self) -> Signal:
        pass

    @abstractmethod
    def build_informatsiyniy_signal(self) -> Signal:
        pass

    @abstractmethod
    def build_modulovaniy_signal(self) -> Signal:
        pass


class FourierBuilder(ABC):
    @abstractmethod
    def compute_fft(self, signal: Signal) -> tuple:
        pass
