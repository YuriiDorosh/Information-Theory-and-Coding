dt = 0.05;
t = [0:dt:2*pi]; % Час, на якому відбувається вибірка синусоїди
mp = 0.5;
L = 16; % = 2^4 - 4 біти
dp = 2 * mp / L;
sig = mp * sin(t); % Оригінальний сигнал - синусоїда
partition = [-mp:dp:mp]; % Діапазон значень для квантування
codebook = [-(mp):dp:(mp+dp)]; % Кодова книга для представлення інтервалів
[index, quants] = quantiz(sig, partition, codebook);
figure(1)
plot(t, sig, 'x')
hold on
stem(t, quants, 'r', 'Marker', '.')
legend('Оригінальний сигнал', 'Квантований сигнал');
xlabel('Час');
ylabel('Амплітуда');

% Обчислення та відображення графіку шуму квантування
q = quants - sig; % Помилка квантування
figure(2)
plot(t, q)
xlabel('Час');
ylabel('Помилка квантування');
title('Графік шуму квантування');



