import os
import random

# команды: clear, help, echo, question

def console():

    message = input('- ')

    if message.startswith('/'):

        command = message[1:]

        name = command.split()[:1][0]
        arguments = command.split()[1:]


        if name == 'help':
            print('* Список команд пока недоступен...')

        if name == 'echo':
            if len(arguments) != 2:
                print('* Используйте /echo [Сообщение] [Количество повторений]')
            else:
                try:
                    int(arguments[1])
                except ValueError:

                    print('* Используйте числа для указания количества повторений!')
                    return
                
                for i in range(int(arguments[1])):
                    print(arguments[0])

        if name == 'clear':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        if name == 'question':
            if len(arguments) == 0:
                print('* Задайте вопрос!')
            else:
                print('* ...')
                print(f'  {random.choice(['Да', 'Нет', 'Возможно', 'Спросите позже', 'Без сомнений', 'Не знаю'])}')




while True:
    console()