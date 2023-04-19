from chatbotfunctions import *

is_going = True
while is_going:
    user_input = input("Вы: ")
    response = get_response(user_input)
    print("Бот: ", response)
    if user_input == 'пака':
        is_going = False
