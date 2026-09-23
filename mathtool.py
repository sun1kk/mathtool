import sys
import math

# Константа максимального значения
MAX_VALUE = 10000

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

# Если запустили просто "python mathtool.py solve"
if len(args) == 1:
    raw_a = input("Введите A: ")
    raw_b = input("Введите B: ")
    raw_c = input("Введите C: ")
# Если передали коэффициенты через флаги -a, -b, -c
elif len(args) == 7:
    if args[1] == "-a" and args[3] == "-b" and args[5] == "-c":
        raw_a = args[2]
        raw_b = args[4]
        raw_c = args[6]
