import random

qa_pairs = {
    "привет": ["Привет!", "Здравствуйте!", "Рад вас видеть!"],
    "как дела": ["У меня все хорошо, спасибо за спрос.", "Не могу жаловаться.", "Отлично!"],
    "что нового": ["Ничего особенного.", "Ничего, что могло бы вас заинтересовать."]
}


def get_response(question):
    # Приведение вопроса к нижнему регистру и удаление знаков препинания
    question = question.lower().rstrip("?!")
    # Поиск ответа в словаре qa_pairs

    if question in qa_pairs:
        answer = random.choice(qa_pairs[question])
    else:
        answer = "Извините, я не понимаю ваш вопрос."

    return answer


def add_new_response(new_question, new_answer):
    qa_pairs[new_question] = [new_answer]
    print(f'Обновлена конфигурация, на вопрос - {new_question} я буду отвечать - {new_answer}')