import csv


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


    """
    Функция для получения списка кают и сортировки их в алфавитном порядке
    Выводит на экран первые пять кают по алфавиту
    """
    with open("new_time.txt", 'r', encoding='utf-8') as file:
        alist = []
        for line in file:
            data = line.split(" ")
            alist.append([data[5], data[2], data[10]])
        insertion_sort(alist)
        for i in range(3):
            print(f'На станции  {alist[i][1]} в каюте {alist[i][0]} восстановлено время. Актуальное время: {alist[i][2]}\n')

