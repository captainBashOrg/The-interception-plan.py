
def personal_sum(numbers):
    rezult = 0
    incorrect_data = 0
    try:
        for num in numbers:
            try:
                rezult += num
            except TypeError:
                incorrect_data += 1
                print( "incorrect_data", num )
            #print(num)
        return (rezult, incorrect_data)
    except TypeError:
        return (None, 1) # передана не коллекция


def calculate_average(numbers):
    sum = personal_sum(numbers) [0]
    try:
        qTy = len (numbers)
    except TypeError:
        qTy = 1

    try:
        return sum / qTy
    except ZeroDivisionError :
        print(f'В numbers записан некорректный тип данных + {numbers}')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print()
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print()
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print()
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать