"""Показатели числовой последовательности."""

import math

MAX_COUNT = 20
MAX_ABS = 10000


def check_numbers(values):
    """Проверяет список чисел. При ошибке возбуждает ValueError."""
    if len(values) == 0:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError(f"чисел больше {MAX_COUNT}")
    for value in values:
        if not math.isfinite(value):
            raise ValueError(f"{value} не является конечным числом")
        if abs(value) > MAX_ABS:
            raise ValueError(f"{value} по модулю больше {MAX_ABS}")