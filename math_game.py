from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QGroupBox, QButtonGroup,)
from random import randint
import time

app = QApplication([])
window = QWidget()
window.setWindowTitle('Math game')
window.resize(400,200)

#Layouts (guide)
row1= QHBoxLayout()
row2 =QHBoxLayout()
column = QVBoxLayout()
sub_col_1 = QVBoxLayout()
sub_col_2 = QVBoxLayout()

#objects
title = QLabel()
title.setStyleSheet("font-size: 35px;")

btn1 = QPushButton('Yes')
btn2 = QPushButton('Yes')

q_group = QGroupBox()
question = QLabel()
question.setStyleSheet("font-size: 35px;")
input_ = QLineEdit()

result_group = QGroupBox()
cor_result = QLabel()
incor_result = QLabel()

#objects to layout
row1.addWidget(title, alignment = Qt.AlignCenter)
row2.addWidget(btn1)
row2.addWidget(btn2)
column.addLayout(row1)
column.addLayout(row2)

sub_col_1.addWidget(question, alignment = Qt.AlignCenter)
sub_col_1.addWidget(input_)
q_group.setLayout(sub_col_1)

sub_col_2.addWidget(cor_result, alignment = Qt.AlignCenter)
sub_col_2.addWidget(incor_result, alignment = Qt.AlignCenter)
result_group.setLayout(sub_col_2)

column.addWidget(result_group)
column.addWidget(q_group)

window.setLayout(column)

#variables
score = 0
incorrect = 0
q_num = 0
cor_ans = None

#functions
def start_game():
    global score, q_num, incorrect
    score = 0
    incorrect = 0
    q_num = 0
    title.setText('GO!')
    btn1.hide()
    btn2.hide()
    result_group.hide()
    q_group.show()
    set_question()
    
def set_question():
    global cor_ans, q_num
    q1 = randint(0,100)
    q2 = randint(0,100)
    cor_ans =  q1 + q2
    question.setText(f'{q1} + {q2}')

def check_ans():
    global score, incorrect, q_num
    cur_ans = int(input_.text())
    if q_num < 10:
        if cur_ans == cor_ans:
            score += 1
        if cur_ans != cor_ans:
            incorrect += 1
        input_.clear()
        q_num += 1
        set_question()
    else:
        show_result()

def show_result():
    global score, incorrect
    q_group.hide()
    result_group.show()
    title.setText('RESULTS:')
    cor_result.setText('Correct:'+ str(score))
    incor_result.setText('Incorrect:'+ str(incorrect))

''' TBD
def countdown():
    ans_time = 60
    while ans_time > 0:
        ans_time = str(ans_time)
        title.setText(ans_time+' seconds remaining')
        ans_time = int(ans_time)
        time.sleep(1)
        ans_time -= 1
'''

#main code
title.setText('Are you ready?')
btn1.show()
btn2.show()
q_group.hide()
btn1.clicked.connect(start_game)
btn2.clicked.connect(start_game)
input_.returnPressed.connect(check_ans)


window.show()
app.exec_()