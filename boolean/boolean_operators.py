#example 1
x = 5
print(x > 3 and x < 10)  # True
# Оба условия True, поэтому результат True

#example 2
x = 5
print(x > 3 or x > 10)  # True
# Хотя бы одно условие True, поэтому результат True

#example 3
x = 5
print(not(x > 3))  # False
# x > 3 это True, но not меняет на False

#example 4
age = 25
print(age > 18 and age < 30)  # True
# Проверка диапазона

#example 5
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False