import sys
from calc import equation

# 1. Получаем аргументы из командной строки
args = sys.argv[1:]

# Проверка на справку
if len(args) == 0 or (len(args) == 1 and args[0] == "--help"):
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    sys.exit(0)

# Проверка команды solve
if args[0] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

raw_a = ""
raw_b = ""
raw_c = ""

if len(args) == 1:
    raw_a = input("Введите A: ")
    raw_b = input("Введите B: ")
    raw_c = input("Введите C: ")
elif len(args) == 7:
    if args[1] == "-a" and args[3] == "-b" and args[5] == "-c":
        raw_a = args[2]
        raw_b = args[4]
        raw_c = args[6]
    else:
        print("ОШИБКА: неверные параметры", file=sys.stderr)
        sys.exit(1)
else:
    print("ОШИБКА: неверное количество параметров", file=sys.stderr)
    sys.exit(1)

# 2. Переводим строки в целые числа
try:
    a = int(raw_a)
    b = int(raw_b)
    c = int(raw_c)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

# 3. Проверка и 4. Расчёт — через модуль calc
try:
    equation.check_coefficients(a, b, c)
    kind, d, roots = equation.solve(a, b, c)
except ValueError as error:
    print(f"ОШИБКА: {error}", file=sys.stderr)
    sys.exit(1)

# 5. Печатаем результат
if kind == "линейное":
    print("Уравнение линейное")
    print(f"x = {roots[0]:.3f}")
else:
    print("Уравнение квадратное")
    print(f"D = {d}")
    if len(roots) == 2:S
        print(f"x1={roots[0]:.3f}")
        print(f"x2={roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x={roots[0]:.3f}")
    else:
        print("Действительных корней нет")

sys.exit(0)