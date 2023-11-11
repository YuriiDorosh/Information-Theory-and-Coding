import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
t0 = 0
tkinc = 5
u0 = 5  # [Вольт] - амплітуда опорного сигналу
uinf = 1.5  # [Вольт] - амплітуда інформаційного сигналу

M = 0.3  # [безрозмірна] - коефіцієнт амплітудної модуляції
F1inf = 50  # частота інформаційного сигналу
fi1 = 45  # [grad] - фаза інформаційного сигналу
F2op = 200  # частота опорного сигналу
fi0 = 10  # [grad] -  фаза опорного сигналу

t = np.arange(t0, tkinc + dt, dt)  # [c] - час передачі модульованого сигналу (частота опорного сигналу)
omega1 = F1inf * 2 * np.pi  # [Герц]  - частота інформаційного сигналу
omega0 = F2op * 2 * np.pi  # [Герц] - частота опорного сигналу
rad = np.pi / 180
U0 = u0 * np.cos(omega0 * t + fi0 * rad)  # опорний сигнал
Uinf = uinf * np.cos(omega1 * t + fi1 * rad)  # інформаційний сигнал
A = 1 + M * Uinf
Uam = A * U0  # модульований сигнал
Fs = 1 / dt  # частота дискретизації
T = 1 / Fs  # період дискретизації
L = int(Fs * tkinc) + 1  # довжина сигналу
t = np.arange(0, L) * T  # часовий вектор
Y = np.fft.fft(Uam)  # швидке перетворення Фур'є сигналу
P2 = np.abs(Y / L)
P1 = P2[:(L // 2) + 1]
P1[1:-1] = 2 * P1[1:-1]
f = Fs * np.arange((L // 2) + 1) / L

plt.figure(1)
plt.plot(f, P1)
plt.title('Cпектральний склад однотонального АМ коливання')
plt.xlabel('f (Hz)')
plt.ylabel('|P1(f)|')

plt.figure(2)
plt.plot(t, U0, label='Опорний сигнал')
plt.title('Опорний сигнал з інформаційним (порівняння)')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid()
plt.plot(t, Uinf, 'r', label='Інформаційний сигнал')
plt.legend()

plt.figure(3)
plt.plot(t, Uinf)
plt.title('Інформаційний сигнал')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid()

plt.figure(4)
plt.plot(t, Uam)
plt.title('Модульований сигнал')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid()

plt.show()
