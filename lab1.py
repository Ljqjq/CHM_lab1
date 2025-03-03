
def f(x):
    return x**3 - 0.4*x**2 + 3.2*x - 1.5

def f_der(x):
    return 6*x - 0,8

def dichotomi_method(a, b, E):
    if f(a) == 0:
        print(f"Точний корінь знайдено: {a}")
        return a
    if f(b) == 0:
        print(f"Точний корінь знайдено: {b}")
        return b
    if f(a) * f(b) >= 0:
        print("Невірний вибір відрізка [a, b]")
        return None
    
    it = 0

    while (b - a) / 2 > E:
        c = (a + b) / 2

        it = it + 1

        if f(c) == 0:
            print(f"Точний корінь знайдено: {c}")
            return c
        elif f(a) * f(c) < 0:
            b = c
            print(f"Міняєм верхню межу на середину {c}")
        else:
            a = c
            print(f"Міняєм нижню межу на середину {c}")
    
    print(f"кількість ітерацій: {it}")
    print(f"Значення функції в точці {(a + b)/2} = {f((a + b) / 2)}")

    return (a + b) / 2

def horda_method(a, b, E):
    if f(a) == 0:
        print(f"Точний корінь знайдено: {a}")
        return a
    if f(b) == 0:
        print(f"Точний корінь знайдено: {b}")
        return b   
    if f(a) * f(b) >= 0:
        print("Невірний вибір відрізка [a, b]")
        return None
    
    
    x1 = a - (f(a) * (b - a)) / (f(b) - f(a))
    if f(a) == f_der(a): 
        x1 = b - (f(b) * (b - a)) / (f(b) - f(a))
    x2 = x1 - (f(x1) * (b - x1)) / (f(b) - f(x1))

    it = 0

    while abs(x2 - x1) > E:
        it = it + 1

        x1 = x2
        x2 = x1 - (f(x1) * (b - x1)) / (f(b) - f(x1))

        print (f"координата x рухомого кінця: {x2}")
        
        if f(x2) == 0:
            print(f"Точний корінь знайдено: {x2}")
            return x2
        
    print(f"Кількість ітерацій: {it}")
    print(f"Значення функції в точці {x2} = {f(x2)}")
    return x2

# Приблизно визначимо інтервали для коренів графічно або аналітично і вводимо через консоль
a = int(input("\nВведіть нижню межу:"))
b = int(input("\nВведіть верхню межу:"))
#вводим похибку
E = float(input("\nВведіть похибку:"))

print("\n\n\nМетод дихотомії:")
root = dichotomi_method(a, b, E)

if root is not None:
    print(f"Корінь на [{a}, {b}]: {root:.6f}")

print("\nМетод хорд:")
root = horda_method(a, b, E)

if root is not None:
    print(f"Корінь на [{a}, {b}]: {root:.6f}")
