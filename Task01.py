# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N
# ЧЕРЕЗ РЕКУРСИЮ и без циклов

n = int(input("Enter number:  "))


def factoral1(n):
    if n == 1:
        return n

    else:
        return n * factoral1(n - 1)


print(factoral1(n))

# n = int(input("Enter number:  "))

def factorial2(n):
    if n == 1:
        return n

    else:
        return n + factorial2(n - 1)


print(factorial2(n))
