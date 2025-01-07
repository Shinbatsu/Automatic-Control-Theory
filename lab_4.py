import numpy as np
import matplotlib.pyplot as plt
from control.matlab import tf, pole, zero, impulse
from control import step_response

def analyze_system(num, den, k_range, freq_range, mikhailov_xlim, mikhailov_ylim):
    """
    Анализ системы управления:
    - Вывод передаточной функции, полюсов и нулей
    - Построение корневого годографа
    - Импульсная и переходная характеристики
    - Годограф Михайлова
    """

    system = tf(num, den)
    print('Передаточная функция САУ:\n', system)
    print("Полюса:\n", pole(system))
    print("Нули:\n", zero(system), '\n')

    # Корневой годограф
    K_values = np.linspace(*k_range)
    roots_list = []

    for K in K_values:
        closed_loop_den = np.polyadd(den, np.polymul(num, [K]))
        roots = np.roots(closed_loop_den)
        roots_list.append(roots)

    roots_array = np.array(roots_list)

    plt.figure()
    for i in range(len(roots_array[0])):
        plt.plot(np.real(roots_array[:, i]), np.imag(roots_array[:, i]), label=f'Корень {i+1}')
    plt.title('Корневой годограф')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()

    # Импульсная характеристика
    y, t = impulse(system)
    plt.plot(t, y, "b")
    plt.title('Импульсная характеристика')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время (сек)')
    plt.grid(True)
    plt.show()

    # Переходная характеристика
    time = np.linspace(0, 50, 100)
    y, t = step_response(system, T=time)
    plt.plot(t, y, "b")
    plt.title('Переходная характеристика')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время (сек)')
    plt.grid(True)
    plt.show()

    # Годограф Михайлова
    omega = 1j * np.logspace(*freq_range)
    poly_values = np.polyval(den, omega)

    plt.figure()
    plt.plot(np.real(poly_values), np.imag(poly_values), label='Годограф Михайлова')
    plt.xlim(*mikhailov_xlim)
    plt.ylim(*mikhailov_ylim)
    plt.title('Годограф Михайлова')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Первая система
    num1 = [1.]
    den1 = [8., 4., 5., 1., 0]
    analyze_system(num1, den1, k_range=(0, 100, 1000), freq_range=(-2, 2, 1000), mikhailov_xlim=(-5.0, 5.0), mikhailov_ylim=(-5.0, 2.0))

    # Вторая система
    num2 = [1.]
    den2 = [8., 15., 5., 1., 0]
    analyze_system(num2, den2, k_range=(0, 100, 1000), freq_range=(-2, 2, 1000), mikhailov_xlim=(-10.0, 5.0), mikhailov_ylim=(-5.0, 1.0))
