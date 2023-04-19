from chatbotfunctions import *

is_going = True
while is_going:
    user_input = input("Вы: ")
    response = get_response(user_input)
    print("Бот: ", response)
    if user_input == 'q':
        is_going = False
    elif user_input == 'cfg':
        password = input('Введите пароль администратора: \n')
        if get_god_mod(password):
            print('Привет одмэн, введите вопрос, затем ответы через запятую: \n')
            question = input()
            answer = input()
            add_new_response(question, answer)
        else:
            print('У вас недостаточно прав')
