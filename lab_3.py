import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def define_systems(T, T2, K, eps):
    """Определение трёх различных передаточных функций."""
    return {
        'K/(Ts+1)': signal.TransferFunction([K], [T, 1]),
        'K/((Ts+1)(T2s+1))': signal.TransferFunction([K], [T*T2, T+T2, 1]),
        'K/(T^2s^2 + 2T2(eps)s + 1)': signal.TransferFunction([K], [T**2, 2*T2*eps, 1])
    }


def plot_bode_magnitude(systems, w):
    """Построение АЧХ."""
    plt.figure()
    for name, sys in systems.items():
        _, mag, _ = signal.bode(sys, w=w)
        plt.semilogx(w, mag, label=name)
    plt.title('АЧХ (Amplitude-Frequency Response)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)


def plot_bode_phase(systems, w):
    """Построение ФЧХ."""
    plt.figure()
    for name, sys in systems.items():
        _, _, phase = signal.bode(sys, w=w)
        plt.semilogx(w, phase, label=name)
    plt.title('ФЧХ (Phase-Frequency Response)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.legend()
    plt.grid(True)


def plot_log_bode(systems, w):
    """Построение логарифмической АЧХ и ФЧХ."""
    plt.figure()
    for name, sys in systems.items():
        _, mag, _ = signal.bode(sys, w=w)
        plt.semilogx(w, mag, label=name)
    plt.title('ЛАЧХ (Logarithmic Amplitude-Frequency Response)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Log Magnitude (dB)')
    plt.legend()
    plt.grid(True)

    plt.figure()
    for name, sys in systems.items():
        _, _, phase = signal.bode(sys, w=w)
        plt.semilogx(w, phase, label=name)
    plt.title('ЛФЧХ (Logarithmic Phase-Frequency Response)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Log Phase (degrees)')
    plt.legend()
    plt.grid(True)


def plot_amplitude_phase(systems, w):
    """Построение АФЧХ (Амплитуда-Фаза)."""
    plt.figure()
    for name, sys in systems.items():
        _, mag, phase = signal.bode(sys, w=w)
        plt.plot(mag, phase, label=name)
    plt.title('АФЧХ (Amplitude-Phase Response)')
    plt.xlabel('Magnitude (dB)')
    plt.ylabel('Phase (degrees)')
    plt.legend()
    plt.grid(True)


def main():
    # Задание параметров
    T = 0.01 * 4
    T2 = T * 2
    K = 4.0
    eps = 0.4
    w = np.logspace(-2, 2, 500)

    systems = define_systems(T, T2, K, eps)

    # Построение графиков
    plot_bode_magnitude(systems, w)
    plot_bode_phase(systems, w)
    plot_log_bode(systems, w)
    plot_amplitude_phase(systems, w)

    plt.show()


if __name__ == "__main__":
    main()
