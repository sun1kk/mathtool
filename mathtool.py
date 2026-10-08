import sys
from calc import equation, stats
from cli import build_parser


def handle_solve(args):
    """Обработчик команды solve. Возвращает код завершения."""
    # Коэффициенты: либо все три, либо ни одного
    if args.a is None and args.b is None and args.c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif args.a is not None and args.b is not None and args.c is not None:
        a = args.a
        b = args.b
        c = args.c
    else:
        raise ValueError("укажите все три коэффициента либо ни одного")

    equation.check_coefficients({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)

    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
    else:
        print("Уравнение квадратное")
        print(f"D = {d}")
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")

    return 0


def read_numbers(source):
    """Читает числа из открытого источника (файл или стандартный ввод)."""
    values = []
    for line in source:
        for word in line.split():
            try:
                values.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    return values


def handle_stats(args):
    """Обработчик команды stats. Возвращает код завершения."""
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as handle:
            values = read_numbers(handle)
    else:
        values = read_numbers(sys.stdin)

    stats.check_numbers(values)
    return 0


HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
}


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))