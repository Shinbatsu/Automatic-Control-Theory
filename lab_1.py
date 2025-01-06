import matplotlib.pyplot as plt
from math import log10, sqrt, atan, degrees


def calculate_values(w_list, k, T):
    """Вычисляет значения амплитуд и фаз для заданных частот."""
    l_1 = round(20 * log10(k), 2)
    L_values, phases, table = [], [], []
    table.append(["#", "w", "lg(w)", "l_1", "l_2", "L", "-arctg(Tw)", "ф(w)"])

    for i, w in enumerate(w_list):
        lg_w = round(log10(w), 2)
        l_2 = round(20 * log10(sqrt(1 + (T * w) ** 2)), 2)
        L = round(l_1 - l_2, 2)
        phase_rad = round(-atan(T * w), 2)
        phase_deg = round(degrees(phase_rad), 2)

        print(f"l_2 = 20 * log10(sqrt(1 + ({T} * {w}) ** 2)) = {l_2}")
        print(f"L = {l_1} - {l_2} = {L}")
        print(f"phase_rad = -atan({T} * {w}) = {phase_rad}")
        print(f"phase_deg = degrees({phase_rad}) = {phase_deg}\n")

        L_values.append(L)
        phases.append(phase_deg)
        table.append([i + 1, w, lg_w, l_1, l_2, L, phase_rad, phase_deg])

    return l_1, L_values, phases, table


def print_table(table):
    """Выводит таблицу в консоль."""
    print("\nТаблица:")
    for row in table:
        print(" | ".join(f"{str(col):<10}" for col in row))


def plot_graphs(w_list, L_values, phases):
    """Строит графики ЛАЧХ и ЛФЧХ."""
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    axs[0].semilogx(w_list, L_values, marker='o', color='blue')
    axs[0].set_title("ЛАЧХ (Амплитудно-частотная характеристика)")
    axs[0].set_xlabel("ω (рад/с)")
    axs[0].set_ylabel("L (дБ)")
    axs[0].grid(True, which='both', ls='--')

    axs[1].semilogx(w_list, phases, marker='s', color='green')
    axs[1].set_title("ЛФЧХ (Фазо-частотная характеристика)")
    axs[1].set_xlabel("ω (рад/с)")
    axs[1].set_ylabel("Фаза (°)")
    axs[1].grid(True, which='both', ls='--')

    plt.tight_layout()
    plt.show()


# Основной блок выполнения
if __name__ == "__main__":
    w = [0.05, 0.3, 1, 3, 10, 20]
    k = 4
    T = 0.2

    l_1, L_values, phases, table = calculate_values(w, k, T)
    print(f"\nl_1 = 20 * log10({k}) = {l_1}")
    print_table(table)
    plot_graphs(w, L_values, phases)
