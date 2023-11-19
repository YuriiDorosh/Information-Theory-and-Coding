import numpy as np


class SignalQuantizer:
    def __init__(self, mp: float, L: int) -> None:
        self.mp = mp
        self.L = L

    def quantize_signal(self, sig: np.ndarray) -> np.ndarray:
        dp = 2 * self.mp / self.L
        partition = np.arange(-self.mp - dp / 2, self.mp + dp * 1.5, dp)
        codebook = np.arange(-self.mp, self.mp + dp + dp, dp)
        index = np.digitize(sig, partition) - 1
        quants = codebook[index]
        return quants
