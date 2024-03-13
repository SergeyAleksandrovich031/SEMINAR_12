from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f" В каком формате записать данные\n\n"
    f"1 Варинат: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Варинат: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:           # защита от не правильного ввода                   
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding= 'utf-8') as f:     #'a' - вводить
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding= 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():                                                          # вторая функция
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding= 'utf-8') as f:     # 'r' - читать
        data_first =  f.readlines()                                       # читаем строки с применением функции 
        data_first_list = []                                              # создаём пустой список 
        j = 0                                                             # переменная для нашего счетчика
        for i in range(len(data_first)):                                  # спрашиваем длину
            if data_first[i] == '\n' or i == len(data_first) - 1:         # если i элемент равен переходу на новую строку, или равна последней записи]
                data_first_list.append(''.join(data_first[j:i+1]))        # преобразовываем список в строку с помощью функции join
                j = i
        print(''.join(data_first_list))                                   # вывод с помощью функции join

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding= 'utf-8') as f:     # 'r' - читать
        data_second = f.readlines()
        print(*data_second)

print_data()