dt=0.001;
t0 = 0;
tkinc = 5;
u0 = 5; % [Вольт]- амплітуда опорного сигналу
uinf = 1.5; % [Вольт]- амплітуда інформаційного сигналу

M = 0.3; % [безрозмірна] - коефіцієнт амплітудної модуляції
F1inf = 50;%  частота інформаційного сигналу
fi1 = 45; % [grad] - фаза інформаційного сигналу
F2op = 200;%  частота опорного сигналу
fi0=10; % [grad] -  фаза опорного сигналу


t=t0:dt:tkinc; %[c] - час передачі модульованого сигналу (частота опорного сигналу)
omega1=F1inf*2*pi;   % [Герц]  - частота інформаційного сигналу
omega0=F2op*2*pi; % [Герц] - частота опорного сигналу
rad=pi/180;
U0=u0*cos(omega0*t+fi0*rad); % опорний сигнал
Uinf=uinf*cos(omega1*t+fi1*rad); % інформаційний сигнал
A=1+M*Uinf;
Uam=A.*U0; % модульований сигнал
 Fs = 1/dt;            % частота дискретизації
 T = 1/Fs;             % період дискретизації
 L = Fs*tkinc+1;    % довжина сигналу
 t = (0:L-1)*T ;       % часовий вектор
 Y = fft(Uam); % швидке перетворення Фур"є сигналу
P2 = abs(Y/L);
P1 = P2(1:(L/2)+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;


figure(1)
plot(f,P1)
title('Cпектральний склад однотонального АМ коливання')
xlabel('f (Hz)')
ylabel('|P1(f)|')

figure(2)
plot(t,U0)
title('Опорний сигнал з інформаційним (порівняння)')
xlabel('час') 
ylabel('амплітуда')
grid 
hold on 
plot(t,Uinf,'r')

figure(3)
plot(t,Uinf)
title('Інформаційний сигнал')
xlabel('час')
ylabel('амплітуда')
grid
figure(4)

plot(t,Uam)
title('Модульований сигнал')
xlabel('час')
ylabel('амплітуда')
grid