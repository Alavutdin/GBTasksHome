""""Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |"""

numberStart = int(input("Введите трехзначное число: "))
numberA= int(numberStart/100)%10
numberB=int(numberStart/10)%10
numberC = numberStart%10
print(numberA+numberB+numberC)
