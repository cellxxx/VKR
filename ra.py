# ##Пр уровень 4 задача
# from datetime import datetime

# def out_date(years):
#     if (years % 100 != 11) and (years % 10 == 1):
#         return f"{years} год"
#     elif (years % 100 < 15) and (years % 10 in [2, 3, 4]):
#         return f"{years} года"
#     else:
#         return f"{years} лет"

# first_date = input()
# sec_date = input()

# date_obj1 = datetime.strptime(first_date, "%Y-%m-%d")
# date_obj2 = datetime.strptime(sec_date, "%Y-%m-%d")

# years = date_obj2.year - date_obj1.year

# if (date_obj1.month > date_obj2.month) or (date_obj1.month == date_obj2.month and date_obj1.day > date_obj2.day):
#     years -= 1

# result = out_date(years)
# print(result)

# ##Пр ур 4 задача
# from datetime import datetime
# ru_lst = ["Понедельник", "Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
# en_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# date_input = input()
# lang = input()
# date_object = datetime.strptime(date_input, '%d-%m-%Y')
# day_of_the_week = date_object.strftime('%u')
# if lang == "ru":
#     print(f"День недели - {ru_list[day_of_the_week - 1]}")
# elif lang == "en":
#     print(f"Day of the week - {en_list[day_of_the_week - 1]}")
import numpy as np
import matplotlib.pyplot as plt

# Определение функции для ЛАЧХ
def L(w):
    return 40 + 20 * np.log10(w) + 10 * np.log10(100*w**2 + 1) - 10 * np.log10(0.0001*w**2 + 1) - 10 * np.log10(w**4 + w**2 + 1)

# Диапазон частот
omega = np.logspace(-5, 5, 100)  # Частоты от 0.1 до 1000 рад/с
L_omega = L(omega)

# Построение графика
plt.figure(figsize=(8, 6))
plt.semilogx(omega, L_omega)  # Логарифмическая шкала по оси X
plt.title("Логарифмическая амплитудно-частотная характеристика")
plt.xlabel("Частота (рад/с)")
plt.ylabel("Амплитуда (дБ)")
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Определение функции для ЛФЧХ
def phi(w):
    return 90 + np.arctan(10*w) - np.arctan(0.01*w) - np.arctan(5*w / (w**2 + 1))

# Диапазон частот
omega = np.logspace(-1, 3, 100)  # Частоты от 0.1 до 1000 рад/с
phi_omega = phi(omega)

# Построение графика
plt.figure(figsize=(8, 6))
plt.semilogx(omega, phi_omega)  # Логарифмическая шкала по оси X
plt.title("Фазовая характеристика (ЛФЧХ)")
plt.xlabel("Частота (рад/с)")
plt.ylabel("Фаза (градусы)")
plt.grid(True)
plt.show()

