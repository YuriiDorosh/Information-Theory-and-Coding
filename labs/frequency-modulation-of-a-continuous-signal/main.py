import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
t0 = 0
tkinc = 0.5
U0 = 4  # [Вольт] - амплітуда опорного сигналу
Uinf = 2  # [Вольт] - амплітуда інформаційного сигналу
beta = 1  # [безрозмірна] - коефіцієнт частотної модуляції
F1inf = 5  # частота інформаційного сигналу
fi1 = 0  # 45; % [grad] - фаза інформаційного сигналу
F2op = 10 ** 2  # частота опорного сигналу
fi0 = 0  # 10; % [grad] - фаза опорного сигналу

# Розрахунок
t = np.arange(t0, tkinc + dt, dt)  # [c] - час передачі модульованого сигналу (частота опорного сигналу)
omega1 = F1inf * 2 * np.pi  # [Герц] - частота інформаційного сигналу ;
omega0 = F2op * 2 * np.pi  # [Герц] - частота опорного сигналу
rad = np.pi / 180
St = U0 * np.cos(omega0 * t + fi0 * rad)  # опорний сигнал
U1 = Uinf * np.cos(omega1 * t + fi1 * rad)  # інформаційний сигнал
ModSignal = U0 * np.cos(omega0 * t + beta * omega0 / omega1 * np.sin(omega1 * t + fi1 * rad))  # модульований сигнал

Fs = 1 / dt  # 10000; % частота дискретизації
T = 1 / Fs  # період дискретизації
L = int(Fs * tkinc) + 1  # 100001; % довжина сигналу
t_fft = np.arange(0, L) * T  # часовий вектор для швидкого перетворення Фур'є
Y = np.fft.fft(ModSignal)  # швидке перетворення Фур'є сигналу
P2 = np.abs(Y / L)
P1 = P2[:(L // 2) + 1]
P1[1:-1] = 2 * P1[1:-1]
f = Fs * np.arange((L // 2) + 1) / L

# Графік 1
plt.figure()
plt.plot(f, P1)
plt.title('Спектральний склад ЧМ сигналу')
plt.xlabel('f (Hz)')
plt.ylabel('|P1(f)|')
plt.savefig("графік_спектральний.png")

# Графік 2
plt.figure()
plt.plot(t, St) 
plt.title('Опорний сигнал')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid(True)
plt.plot(t, U1, 'r') 
plt.legend()
plt.savefig("графік_опорний.png")



# Графік 3
plt.figure()
plt.plot(t, U1)
plt.title('Інформаційний сигнал')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid(True)
plt.savefig("графік_information.png")

# Графік 4
plt.figure()
plt.plot(t, ModSignal)
plt.title('Модульований сигнал')
plt.xlabel('час')
plt.ylabel('амплітуда')
plt.grid(True)
plt.savefig("графік_модульований.png")
