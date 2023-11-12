from src.builders.builders import SignalBuilder


class SignalDirector:
    def __init__(self, signal_builder: SignalBuilder):
        self.signal_builder = signal_builder

    def construct_signal(self) -> tuple:
        oporniy_signal = self.signal_builder.build_oporniy_signal()
        informatsiyniy_signal = self.signal_builder.build_informatsiyniy_signal()
        modulovaniy_signal = self.signal_builder.build_modulovaniy_signal()
        return oporniy_signal, informatsiyniy_signal, modulovaniy_signal
