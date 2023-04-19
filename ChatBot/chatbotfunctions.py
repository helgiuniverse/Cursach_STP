import random
import json

with open('pairs.json', 'r', encoding='utf-8') as pairs_read:
    qa_pairs = json.load(pairs_read)


# Функция ответа на вопрос
def get_response(question):
    # Приведение вопроса к нижнему регистру и удаление знаков препинания
    question = question.lower().rstrip("?!")
    # Поиск ответа в словаре qa_pairs
    if question in qa_pairs:
        answer = random.choice(qa_pairs[question])
    elif question == 'cfg':
        answer = 'Режим отделки'
    elif question == 'q':
        answer = 'Завершение работы'
    else:
        answer = "Извините, я не понимаю ваш вопрос."
    return answer


# Получение доступа к правам одмэна
def get_god_mod(password):
    is_admin = False
    if password == 'kavoisho':
        is_admin = True
    return is_admin


# Добавление новых пар вопрос - ответ
def add_new_response(new_question, new_answer):
    new_question = new_question.lower().rstrip("?!")
    qa_pairs[new_question] = new_answer.split(',')
    with open('pairs.json', 'w', encoding='utf-8') as pairs_write:
        pairs_write.write(json.dumps(qa_pairs))
    print(f'Обновлена конфигурация, на вопрос - {new_question} я буду отвечать - {new_answer}')
