

def f(x):
    return x**3 - 0.4*x**2 + 3.2*x - 1.5

def dichotomi_method(a, b, E):
    if f(a) * f(b) >= 0:
        print("Невірний вибір відрізка [a, b]")
        return None
    while (b - a) / 2 > E:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2




def horda_method(a, b, E):
    x1 = 0
    x2 = 0

    x1 = a - (f(a) * (b - a)) / (f(b) - f(a))
    x2 = x1 - (f(x1) * (b - x1)) / (f(b) - f(x1))

    while (abs(x2 - x1) > E):
        x1 = x2

        x2 = x1 - (f(x1) * (b - x1)) / (f(b) - f(x1))

    return x2








# Приблизно визначимо інтервали для коренів графічно або аналітично з додачою пробних неправильних інтервалів де не існує кореня
intervals = [(-2, 0), (0, 1), (1, 2)]

E = 0.0001

print("\n\nМетод дихотомії:")
for a, b in intervals:
    root = dichotomi_method(a, b, E)
    if root is not None:
        print(f"Корінь на [{a}, {b}]: {root:.6f}")

print("\nМетод хорд:")
for a, b in intervals:
    root = horda_method(a, b, E)
    if root is not None:
        print(f"Корінь на [{a}, {b}]: {root:.6f}")

