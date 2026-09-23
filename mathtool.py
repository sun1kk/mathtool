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
