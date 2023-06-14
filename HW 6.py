# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
from random import randint

# firstElement = int(input('Введите первый элемент арифмитической прогрессии: '))
# difference = int(input('Введите разность для арифмитической прогрессии: '))
# elements = int(input('Введите количество элементов: '))

# def arithmeticProgression (firstEl, dif, el):
#   resultList = []
#   i = 0
#   while el > i:
#     if i == 0:
#       resultList.append(firstEl)
#     else:
#       resultList.append(resultList[0] + (i - 1) * dif)
#     i += 1
#   return resultList
# print(arithmeticProgression (firstElement, difference, elements))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

checkList = [randint(-10,10) for i in range(int(input('Введите длину первого массива: ')))]
minimumRange = int(input('Введите минимальное значение диапазона поиска: '))
maximumRange = int(input('Введите максимальное значение диапазона поиска: '))

def checkingList (chList, minRange, maxRange):
  resultList = []
  for i in range(len(chList)):
    if chList[i] > minRange & chList[i] < maxRange:
      resultList.append(i)
  return resultList
print(checkList)
print(checkingList(checkList, minimumRange, maximumRange))
