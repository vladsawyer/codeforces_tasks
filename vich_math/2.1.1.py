import math


def value_in_point(var):
    """
    Вычисление значения в точке
    :param var: float
    :return: value: float
    """
    return 8 * math.sin(6.18 * var) - (6.25 * var)


def bisection(a, b, eps):
    """
    Вычисление корня уравнения методом бисекци.
    fa,fc,fb - значения функций в точке.
    :param a: начало интервала
    :param b: конец интервала
    :param eps: точность, задаётся пользователем
    :return: result
    """
    global c
    fa = value_in_point(a)

    while math.fabs(b - a) >= eps:
        c = (a + b) / 2
        fb = value_in_point(b)
        fc = value_in_point(c)

        print(f'a: {a}', f'b: {b}', f'c: {c}', f'fa*fb: {fa * fb}',
              f'|b-a|: {math.fabs(b - a)}', f'fc: {fc}')

        # если нет пересечения с осью Х, то передвигаем левый конец интервала
        # в точку полуинтервала, иначе правый конец интервала передвигаем
        # в точку полуинтервала
        if fa * fc > 0:
            a = c
            fa = fc
        else:
            b = c

    else:
        return c


def go():
    eps = float(input("Введите eps(в виде 0.0...1): "))
    a, b = map(float, input("Введите интервал a и b через пробел: ").split())
    value = bisection(a=0.001, b=1, eps=0.0001)
    print(f'Корень уравнения: {value}')


if __name__ == '__main__':
    go()