#сложение
def add (x, y):
    return x + y

#вычитание
def subtract(x, y):
    return x - y

#умножение
def multiply(x, y):
    return x * y

#делим
def divide(x, y):
    return x / y

print("Выберите операцию:")
print("1-сложить")
print("2-вычесть")
print("3-умножить")
print("4-делить")

while True:
    choice = input("Выберите действие: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("НЕПРАВИЛЬНЫЙ ВВОД")