import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


# Функция для расчета коэффициента усиления
def erbium_amplifier(input_power, gain, pump_power):
    output_power = input_power * gain + pump_power * 0.01  # Примерная модель
    return output_power


def dBm_to_mW(dBm):
    return 10 ** ((dBm + 30) / 10)


def mW_to_dBm(mW):
    return 10 * np.log10(mW) - 30


def calculate_output():
    try:
        input_power_dBm = float(input_power_entry.get())
        gain = 15  # Усиление (дБ)
        pump_power_dBm = 20  # Мощность насоса в dBm

        input_power_mW = dBm_to_mW(input_power_dBm)
        pump_power_mW = dBm_to_mW(pump_power_dBm)

        output_power_mW = erbium_amplifier(input_power_mW, gain, pump_power_mW)
        output_power_dBm = mW_to_dBm(output_power_mW)

        messagebox.showinfo("Результат", f"Выходная мощность: {output_power_dBm:.2f} dBm")

        # Визуализация
        plot_power(input_power_dBm, output_power_dBm)

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное значение мощности.")


def plot_power(input_power_dBm, output_power_dBm):
    powers = [input_power_dBm, output_power_dBm]
    labels = ['Input Power', 'Output Power']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, powers, color=['blue', 'green'])
    plt.title('Эрбиевый усилитель: Входная и выходная мощность')
    plt.ylabel('Мощность (dBm)')
    plt.ylim(-20, 30)
    plt.show()


# Создание главного окна
root = tk.Tk()
root.title("Симуляция Эрбиевого Усилителя")

# Элементы интерфейса
input_power_label = tk.Label(root, text="Введите входную мощность (dBm):")
input_power_label.pack()

input_power_entry = tk.Entry(root)
input_power_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать выходную мощность", command=calculate_output)
calculate_button.pack()

exit_button = tk.Button(root, text="Выход", command=root.quit)
exit_button.pack()

# Запуск главного цикла
root.mainloop()