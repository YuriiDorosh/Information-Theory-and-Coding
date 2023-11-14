import numpy as np 
import matplotlib.pyplot as plt 
 
# Функція для квантування 
def quantize_signal(sig, mp, L): 
    dp = 2 * mp / L 
    partition = np.arange(-mp-dp/2, mp+dp*1.5, dp) 
    codebook = np.arange(-mp, mp + dp + dp, dp) 
    index = np.digitize(sig, partition) -1
    quants = codebook[index] 
    return quants 
 
# Параметри сигналу 
dt = 0.05 
t = np.arange(0, 2 * np.pi, dt) 
mp = 0.5 
L = 16 
 
# Створення оригінального сигналу 
sig = mp * np.sin(t) 
 
# Квантування сигналу 
quants = quantize_signal(sig, mp, L) 
 
# Зберігання графіка оригінального та квантованого сигналу 
plt.figure() 
plt.plot(t, sig, 'x', label='Оригінальний сигнал') 
plt.stem(t, quants, 'r', markerfmt='r.', label='Квантований сигнал') 
plt.legend() 
plt.xlabel('Час') 
plt.ylabel('Амплітуда') 
plt.title('Графік оригінального та квантованого сигналу') 
plt.savefig('original_and_quantized_signal.png') 
 
# Зберігання графіка шуму квантування 
q = quants - sig 
plt.figure() 
plt.plot(t, q) 
plt.xlabel('Час') 
plt.ylabel('Помилка квантування') 
plt.title('Графік шуму квантування') 
plt.savefig('quantization_noise.png')