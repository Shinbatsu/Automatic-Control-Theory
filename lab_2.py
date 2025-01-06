import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, freqresp


def plot_bode(system, frequencies):
    """Строит амплитудно-фазовую характеристику системы."""
    w, H = freqresp(system, frequencies)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(w, 20 * np.log10(np.abs(H)))
    plt.title('АФЧХ')
    plt.xlabel('Частота (рад/с)')
    plt.ylabel('Амплитуда (дБ)')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, np.angle(H))
    plt.title('Фазочастотная характеристика')
    plt.xlabel('Частота (рад/с)')
    plt.ylabel('Фаза (рад)')
    plt.grid()


def plot_nyquist(H):
    """Строит годограф Найквиста."""
    plt.figure(figsize=(6, 6))
    plt.plot(np.real(H), np.imag(H))
    plt.title('Годограф Найквиста')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid()


def plot_mikhailov(denominator, frequencies):
    """Строит годограф Михайлова."""
    omega = 1j * frequencies
    poly_values = np.polyval(denominator, omega)

    plt.figure(figsize=(6, 6))
    plt.plot(np.real(poly_values), np.imag(poly_values), label='Годограф Михайлова')
    plt.axis([-10.0, 100.0, -80.0, 15.0])  # Подогнать под ваш случай
    plt.title('Годограф Михайлова')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid()
    plt.legend()


def plot_root_locus(numerator, denominator, K_range):
    """Строит корневой годограф (локус корней)."""
    roots_list = []

    for K in K_range:
        closed_loop_den = np.polyadd(denominator, np.polymul(numerator, [K]))
        roots = np.roots(closed_loop_den)
        roots_list.append(roots)

    roots_array = np.array(roots_list)

    plt.figure(figsize=(8, 6))
    for i in range(roots_array.shape[1]):
        plt.plot(np.real(roots_array[:, i]), np.imag(roots_array[:, i]), label=f'Корень {i+1}')
    plt.title('Корневой годограф')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()


def main():
    numerator = [1]
    denominator = [1, 3, 4, 3, 1]
    system = TransferFunction(numerator, denominator)

    frequencies = np.logspace(-2, 2, 1000)
    _, H = freqresp(system, frequencies)

    plot_bode(system, frequencies)
    plot_nyquist(H)
    plot_mikhailov(denominator, frequencies)
    plot_root_locus(numerator, denominator, np.linspace(0, 100, 1000))

    plt.show()


if __name__ == "__main__":
    main()
