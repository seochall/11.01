from PyQt6.QtWidgets import QApplication, QMainWindow

from form import Ui_MainWindow

import sys
import sqlite3

myConnection = sqlite3.connect("base.db")
myCursor = myConnection.cursor()
myCursor2 = myConnection.cursor()

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()

ui.reg_label.setVisible(False)
ui.reg_pushButton.setVisible(False)
ui.reg_lineEdit_2.setVisible(False)
ui.reg_label_3.setVisible(False)
ui.reg_label_2.setVisible(False)
ui.reg_lineEdit.setVisible(False)
ui.reg_label_4.setVisible(False)
ui.reg_label_5.setVisible(False)
ui.reg_label_6.setVisible(False)
ui.reg_lineEdit_3.setVisible(False)
ui.reg_lineEdit_4.setVisible(False)
ui.reg_lineEdit_5.setVisible(False)

ui.home_calendarWidget.setVisible(False)
ui.home_label.setVisible(False)

ui.error_1.setVisible(False) #пароли не совпадают
ui.error_2.setVisible(False) #логин занят
ui.error_3.setVisible(False) #пароль занят
ui.error_4.setVisible(False) #не все поля заполнены



def whod(): #авторизация
    n = 0
    myCursor.execute("select * from users ")
    myResult = myCursor.fetchall()
    for i in myResult:
        if str(ui.inlet_lineEdit.text()) == str(i[1]) and str(ui.inlet_lineEdit_2.text()) == str(i[2]):
            n += 1
    if n != 1:
        print("no")
        ui.inlet_label.setText("Логин или пароль введены неверно")
        ui.inlet_label.setGeometry(20, 20, 315, 41)
        n-=1


    else:
        print("ok")
        ui.inlet_lineEdit.setVisible(False)
        ui.inlet_lineEdit_2.setVisible(False)
        ui.inlet_label.setVisible(False)
        ui.inlet_label_2.setVisible(False)
        ui.inlet_label_3.setVisible(False)
        ui.inlet_label_4.setVisible(False)
        ui.inlet_pushButton.setVisible(False)
        ui.inlet_pushButton_2.setVisible(False)

        ui.home_calendarWidget.setVisible(True)
        ui.home_label.setVisible(True)


ui.inlet_pushButton.clicked.connect(whod)


def registr(): #при нажатии на кнопку зарегистрироваться открывает форму регистрации
    ui.inlet_lineEdit.setVisible(False)
    ui.inlet_lineEdit_2.setVisible(False)
    ui.inlet_label.setVisible(False)
    ui.inlet_label_2.setVisible(False)
    ui.inlet_label_3.setVisible(False)
    ui.inlet_label_4.setVisible(False)
    ui.inlet_pushButton.setVisible(False)
    ui.inlet_pushButton_2.setVisible(False)

    ui.reg_label.setVisible(True)
    ui.reg_pushButton.setVisible(True)
    ui.reg_lineEdit_2.setVisible(True)
    ui.reg_label_3.setVisible(True)
    ui.reg_label_2.setVisible(True)
    ui.reg_lineEdit.setVisible(True)
    ui.reg_label_4.setVisible(True)
    ui.reg_label_5.setVisible(True)
    ui.reg_label_6.setVisible(True)
    ui.reg_lineEdit_3.setVisible(True)
    ui.reg_lineEdit_4.setVisible(True)
    ui.reg_lineEdit_5.setVisible(True)


ui.inlet_pushButton_2.clicked.connect(registr)


def registr2(): #регистрация с добавлением в бд
    myCursor.execute("select login from users ")
    myCursor2.execute("select phone from users ")
    myResult = myCursor.fetchall()
    myResult2=myCursor2.fetchall()
    print(myResult, myResult2)
    login = str(ui.reg_lineEdit.text())
    password = str(ui.reg_lineEdit_2.text())
    password2=str(ui.reg_lineEdit_3.text())
    phone= str(ui.reg_lineEdit_4.text())
    post= str(ui.reg_lineEdit_5.text())

    p=[]
    l=[]
    for i in myResult:
        l.append(i[0])

    for d in myResult2:
        p.append(d[0])

    print(l, p)

    if password!=password2:
        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)
        ui.error_1.setVisible(True)
    elif login in l:
        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)

        ui.error_2.setVisible(True)
    elif phone in str(p):                    #НЕ РАБОТАЕТ
        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)

        ui.error_3.setVisible(True)
    elif login==('') or password==('') or phone==('') or post==(''):
        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)

        ui.error_4.setVisible(True)
    else:
        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)

        command = "INSERT INTO users (login, password, phone, post) VALUES (?, ?, ?, ?)"
        myCursor.execute(command, (login, password, phone, post))
        myConnection.commit()

        ui.inlet_lineEdit.setVisible(True)
        ui.inlet_lineEdit_2.setVisible(True)
        ui.inlet_label.setVisible(True)
        ui.inlet_label_2.setVisible(True)
        ui.inlet_label_3.setVisible(True)
        ui.inlet_label_4.setVisible(True)
        ui.inlet_pushButton.setVisible(True)
        ui.inlet_pushButton_2.setVisible(True)

        ui.reg_label.setVisible(False)
        ui.reg_pushButton.setVisible(False)
        ui.reg_lineEdit_2.setVisible(False)
        ui.reg_label_3.setVisible(False)
        ui.reg_label_2.setVisible(False)
        ui.reg_lineEdit.setVisible(False)
        ui.reg_label_4.setVisible(False)
        ui.reg_label_5.setVisible(False)
        ui.reg_label_6.setVisible(False)
        ui.reg_lineEdit_3.setVisible(False)
        ui.reg_lineEdit_4.setVisible(False)
        ui.reg_lineEdit_5.setVisible(False)

        ui.error_1.setVisible(False)
        ui.error_2.setVisible(False)
        ui.error_3.setVisible(False)
        ui.error_4.setVisible(False)

        ui.inlet_label.setText("Вход в систему")
        ui.inlet_label.setGeometry(110, 20, 141, 41)


ui.reg_pushButton.clicked.connect(registr2)

app.exec()
