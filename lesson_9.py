import random
from utils import compare

"""
Задание 1:
Написать программу которая на любой вопрос отвечает "да" или "нет"

Задание 2:
Сделать так что бы она помнила отвеченные вопросы

Задание 3:
Даже переформулированные до известных пределов

"""

question_storage = {}


def get_answer_to_question(question):
    check_result = approximate_check_question_repeated(question)
    if check_result != None:
        return "Схожий вопрос [%s] уже был задан. Ответ %s" % (question, question_storage[check_result])

    answer = ""
    num = random.randrange(1, 100)

    if num % 2 > 0:
        answer = "Нет"
    else:
        answer = "Да"

    question_storage[question] = answer
    return answer


def approximate_check_question_repeated(new_question):
    if len(question_storage) == 0:
        return

    for question in question_storage:
        result = compare(new_question, question)
        if result > 0.6:
            return question

    return


if __name__ == '__main__':

    answers = [
        "Кто-то проживает на дне океана?",
        "Python лучше чем Java?",
        "Postgres лучше чем MySQL?",
        "Меня зовут Иван?",
        "Golang лучше чем Java?",
        "Меня зовут Ваня?"
    ]

    for answer in answers:
        print("Вопрос [%s]. Ответ [%s]" % (answer, get_answer_to_question(answer)))

    print("_____________________________")
    print(question_storage)
