"""Численное интегрирование методом левых прямоугольников."""

import math

MAX_STEPS = 100000
DIGITS = 4


def func_ratio(x):
    """F(x) = x / (x + 1)."""
    return x / (x + 1)


def func_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


# Таблица функций: имя -> (функция, формула, нижняя граница, верхняя граница,
# признак «границы допустимы»)
FUNCTIONS = {
    "ratio": (func_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (func_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def check_params(func_name, start, stop, steps):
    """Проверяет пределы и число шагов. При ошибке возбуждает ValueError."""
    _, _, low, high, closed = FUNCTIONS[func_name]
    if not (math.isfinite(start) and math.isfinite(stop)):
        raise ValueError("предел не является конечным числом")
    if start >= stop:
        raise ValueError("начальный предел не меньше конечного")
    for value in (start, stop):
        if closed:
            outside = value < low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            raise ValueError("предел вне промежутка")
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


def integrate(function, start, stop, steps):
    """Интеграл методом левых прямоугольников; function — подынтегральная функция."""
    dx = (stop - start) / steps
    result = 0
    for i in range(steps):
        x = start + i * dx
        result = result + function(x) * dx
    return result