number = int(input())
# вводим длину послеовательности, которую хотим получить
array = [0]
temp = []
# temp это временный массив, который будет хранить инверсию списка array
while(len(array)<number):
# все приведенные ниже действия мы будем повторять столько раз, чтобы список array достиг необходимой длины
    for i in range(len(array)):
        # создаем вложенный цикл, в котором будем перебирать элементы списка array, инверсировать их и добавлять во временный массив
        symbol = (0,1)[array[i]==0]
        temp.append(symbol)
    array+=temp
    # по завершению цикла фор добавляем временный список в конец списка array
    temp = []
    # обнуляем временный список
print(*array[:number])
# выводим срез, в котором будет нужное количество элементов последовательности Туэ Морсе