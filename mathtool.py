import sys
from calc import equation
from cli import build_parser

# 1. Разбор параметров командной строки
parser = build_parser()
args = parser.parse_args(sys.argv[1:])

# Команда не указана — справка и код 0
if args.command is None:
    parser.print_help()
    sys.exit(0)

if args.command == "solve":
    # 2. Получение коэффициентов: либо все три, либо ни одного
    if args.a is None and args.b is None and args.c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
            sys.exit(1)
    elif args.a is not None and args.b is not None and args.c is not None:
        a = args.a
        b = args.b
        c = args.c
    else:
        print("ОШИБКА: укажите все три коэффициента либо ни одного", file=sys.stderr)
        sys.exit(1)

    # 3. Проверка и 4. Расчёт — через модуль calc
    try:
        equation.check_coefficients(a, b, c)
        kind, d, roots = equation.solve(a, b, c)
    except ValueError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        sys.exit(1)

    # 5. Печать результата
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

    sys.exit(0)