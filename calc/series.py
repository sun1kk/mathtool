"""Суммы знакочередующихся рядов."""

import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = math.ceil(-math.log10(MAX_EPS))


def sign(n):
    """Знак n-го слагаемого: плюс для нечётных, минус для чётных."""
    if n % 2 == 0:
        return -1
    return 1


def term_third(n):
    """n-е слагаемое ряда third: 1/(3n) со знаком."""
    return sign(n) / (3 * n)


def term_sqplus(n):
    """n-е слагаемое ряда sqplus: 1/(n^2+1) со знаком."""
    return sign(n) / (n * n + 1)


# Таблица рядов: имя -> (функция слагаемого, запись формулы)
FORMULAS = {
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - ..."),
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
}


def check_terms(terms):
    """Проверяет количество слагаемых. При ошибке возбуждает ValueError."""
    if not 1 <= terms <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")


def check_eps(eps):
    """Проверяет точность. При ошибке возбуждает ValueError."""
    if not (math.isfinite(eps) and 0 < eps <= MAX_EPS):
        raise ValueError("точность вне диапазона")


def sum_by_count(term, count):
    """Сумма первых count слагаемых; term — функция слагаемого."""
    result = 0
    for n in range(1, count + 1):
        result = result + term(n)
    return result


def sum_by_eps(term, eps):
    """Сумма до слагаемого, меньшего eps по модулю. Возвращает (сумма, число слагаемых)."""
    result = 0
    n = 0
    while True:
        n = n + 1
        value = term(n)
        result = result + value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")