time = int(input('Введите время в секундах: '))
minutes = time / 60 
hours = minutes / 60
print('Время в формате ч:м:с - ' + f'{hours} : {minutes} : {time}')