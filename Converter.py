#добавляем единицы измерения в словарь, разбиваем строку ввода.
mapping, inpt = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}, input().split()
#производим вычисления и собираем строку для вывода
result = ("Результат равен "+'%.5e' % (float(inpt[0]) * float(mapping[inpt[1]]) / float(mapping[inpt[3]]))+" "+str(inpt[3]))
#выводим результат
print(result)


