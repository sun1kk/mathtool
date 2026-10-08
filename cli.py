import argparse

from calc.series import FORMULAS

def build_parser():
    """Создаёт и возвращает разборщик параметров командной строки."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    # Команда solve
    solve = subparsers.add_parser(
        "solve", help="решение уравнения A*x^2 + B*x + C = 0", allow_abbrev=False
    )
    solve.add_argument("-a", type=int, help="коэффициент A (целое, по модулю не более 10000)")
    solve.add_argument("-b", type=int, help="коэффициент B (целое, по модулю не более 10000)")
    solve.add_argument("-c", type=int, help="коэффициент C (целое, по модулю не более 10000)")

    # Команда stats
    stats = subparsers.add_parser(
        "stats", help="показатели последовательности чисел", allow_abbrev=False
    )
    stats.add_argument(
        "--input",
        help="имя файла с числами; без него числа читаются со стандартного ввода",
    )

    # Команда series
    series = subparsers.add_parser(
        "series", help="сумма числового ряда", allow_abbrev=False
    )
    series.add_argument("--func", required=True, help="какой ряд суммировать")
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--terms", type=int, help="сколько слагаемых сложить (остановка по количеству)"
    )
    group.add_argument(
        "--eps", type=float, help="до какой величины слагаемого считать (остановка по точности)"
    )

    # Команда integrate
    integrate = subparsers.add_parser(
        "integrate", help="численное интегрирование", allow_abbrev=False
    )
    integrate.add_argument("--func", required=True, help="какую функцию интегрировать")
    integrate.add_argument(
        "--from", dest="start", type=float, required=True, help="нижний предел интегрирования"
    )
    integrate.add_argument(
        "--to", type=float, required=True, help="верхний предел интегрирования"
    )
    integrate.add_argument(
        "--steps", type=int, required=True, help="на сколько прямоугольников делится отрезок"
    )

    return parser