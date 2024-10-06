from PyQt6.QtWidgets import QApplication
from random import choice
from random import shuffle
app = QApplication([])
from main_window import *
class Question():
    def __init__(self, question_text, answer_text, wrong:tuple) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong_answers = wrong
    def got_right(self):
        ...
    def got_wrong(self):
        ... 
q1 = Question("Що впало на Ньютона?", "Баклажан", ("Малина", "Банан", "Інжир", "Полуниця"))
q2 = Question("Продукт яки не портится це?", "Мід", ("Масло", "Олія", "Хліб", "Борошно"))
q3 = Question("", "", ("", "", "", ""))
q4 = Question("", "", ("", "", "", ""))
q5 = Question("", "", ("", "", "", ""))
q6 = Question("", "", ("", "", "", ""))
q7 = Question("", "", ("", "", "", ""))
q8 = Question("", "", ("", "", "", ""))
q9 = Question("", "", ("", "", "", ""))

question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
radio_button_list = [rb_answer1, rb_answer2, rb_answer3, rb_answer4]

def new_question():
    random_question = choice(question_list)

    shuffle(radio_button_list)

    question_1b.setText(random_question.question_text)
    radio_button_list[0].setText(random_question.answer_text)
    for i in range(3):   
        radio_button_list[i+1].setText(random_question.wrong_answers[i])





new_question()

def change_box():
    if btn_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("Наступне питання")
    elif btn_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Відповісти")
    
btn_next.clicked.connect(change_box)

window.show()
app.exec()
