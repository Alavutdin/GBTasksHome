"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no """

numberOfTicket = int(input("Введите пожалуйста Ваш билет: "))
initialNumbers = int(numberOfTicket / 1000)
finiteNumbers = int(numberOfTicket % 1000)
resultA = int((initialNumbers / 100 % 10) + int(initialNumbers / 10 % 10) + int(initialNumbers % 10))
resultB = int((finiteNumbers / 100 % 10) + int(finiteNumbers / 10 % 10) + int(finiteNumbers % 10))

print("yes" if resultA == resultB else "no") # Тернарный оператор
