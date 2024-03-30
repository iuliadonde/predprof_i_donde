import csv

def timeNew(alist):
    '''Описание функции:
    функция для подсчета актуального времени в каюте и создания нового текстового файла с актуальным временем'''
    with open('astronaut_time.csv', 'r', encoding = 'UTF-8') as file:
        alist = {}
        count = 0
        header = file.readline()
        for line in file:
            data = line.split(",")
            numb_st = data[1]
            numb_cabin = data[2]
            now = data[3].split(':')
            new_time = str(int(now[0]) + int(data[4])) + ':' + now[1] + ':' + now[2]


    with open('new_time.txt', 'w', encoding='utf8') as f:
         for keys in alist:
           f.write(f'На станции  {numb_st} в каюте {numb_cabin} восстановлено время. Актуальное время: {now_time}\n')


'''Вывод первых трех записей в файле'''
with open('new_time.txt') as f:
    print(f.readline)
    print(f.readline)
    print(f.readline)
