import sys
from calc import equation
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

    equation.check_coefficients(a, b, c)
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


HANDLERS = {
    "solve": handle_solve,
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