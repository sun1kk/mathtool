"""Решение уравнения A*x^2 + B*x + C = 0."""

import math

MAX_VALUE = 10000


def check_coefficients(coefficients):
    """Проверяет коэффициенты (словарь имя -> значение). При ошибке возбуждает ValueError."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if coefficients["A"] == 0 and coefficients["B"] == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")


def solve(a, b, c):
    """Решает уравнение. Возвращает (вид, дискриминант, список корней)."""
    if a == 0:
        x = -c / b
        return "линейное", None, [x]

    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        return "квадратное", d, []