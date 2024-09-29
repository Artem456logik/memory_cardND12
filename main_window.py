from PyQt6.QtWidgets import (QWhatsThis, QWidget, QLabel,
                              QRadioButton, QPushButton, QGroupBox, 
                              QButtonGroup, QVBoxLayout, QHBoxLayout)
card_width, card_height = 600, 500

window = QWidget()
window.resize(card_width, card_height)
window.setWindowTitle("Memory Car. Автор кто ти такой ктооо тиии такооой белять У АВТОРА ПРОБЛЕМ НЕТ ОН ДУДЖУЙ У КОГО ДЕД ГИТЛЕР ГИТЛЕР ГИТЛЕР НЕГРИ БЕЗРАБОТНИЕ ДАУНИ")

question_1b = QLabel()

rb_answer1 = QRadioButton()
rb_answer2 = QRadioButton()
rb_answer3 = QRadioButton()
rb_answer4 = QRadioButton()

btn_next = QPushButton("Відповісти")

radio_button_box = QGroupBox("Варіанти відповідей")

radio_button_group = QButtonGroup()

radio_button_group.addButton(rb_answer1)
radio_button_group.addButton(rb_answer2)
radio_button_group.addButton(rb_answer3)
radio_button_group.addButton(rb_answer4)

answer_box = QGroupBox("Результат")
result_lb = QLabel("Правильно/Неправильно")
correct_answer_lb = QLabel("right answer")

main_v_line = QVBoxLayout()

radio_button_box_v_line = QVBoxLayout()
radio_button_box_h_line_1 = QHBoxLayout()
radio_button_box_h_line_2 = QHBoxLayout()

radio_button_box_h_line_1.addWidget(rb_answer1)
radio_button_box_h_line_1.addWidget(rb_answer2)

radio_button_box_h_line_2.addWidget(rb_answer3)
radio_button_box_h_line_2.addWidget(rb_answer4)

radio_button_box_v_line.addLayout(radio_button_box_h_line_1)
radio_button_box_v_line.addLayout(radio_button_box_h_line_2)

radio_button_box.setLayout(radio_button_box_v_line)

main_v_line.addWidget(question_1b)
main_v_line.addWidget(radio_button_box)


answer_box_v_line = QVBoxLayout()
answer_box_v_line.addWidget(result_lb)
answer_box_v_line.addWidget(correct_answer_lb)

answer_box.setLayout(answer_box_v_line)

main_v_line.addWidget(answer_box)

main_v_line.addWidget(btn_next)

answer_box.hide()
window.setLayout(main_v_line)



































