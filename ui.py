from loger import input_data, print_data           # из файла logger импортируем input_data и print_data


def interface():                                   # ввод 
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число '))

    while command != 1 and command != 2:           # защита от не правильного ввода                   
        print("Неправильный ввод")
        command = int(input('Введите число '))
# interface()                                        # запуск функции
    if command == 1:
        input_data()
    elif command == 2:
        print_data()