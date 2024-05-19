from PyQt6.QtWidgets import QApplication, QMainWindow

from test1 import Ui_MainWindow1
from test2 import Ui_MainWindow2

import sys
import sqlite3

myConnection = sqlite3.connect("base.db")
myCursor = myConnection.cursor()
myCursor2 = myConnection.cursor()

app = QApplication(sys.argv)
window = QMainWindow()
ui1 = Ui_MainWindow1()
ui1.setupUi(window)


window.show()

ui1.reg_label.setVisible(False)
ui1.reg_pushButton.setVisible(False)
ui1.reg_lineEdit_2.setVisible(False)
ui1.reg_label_3.setVisible(False)
ui1.reg_label_2.setVisible(False)
ui1.reg_lineEdit.setVisible(False)
ui1.reg_label_4.setVisible(False)
ui1.reg_label_5.setVisible(False)
ui1.reg_label_6.setVisible(False)
ui1.reg_lineEdit_3.setVisible(False)
ui1.reg_lineEdit_4.setVisible(False)
ui1.reg_lineEdit_5.setVisible(False)

ui1.home_calendarWidget.setVisible(False)
ui1.home_label.setVisible(False)
ui1.home_pushButton.setVisible(False)

ui1.error_1.setVisible(False) #пароли не совпадают
ui1.error_2.setVisible(False) #логин занят
ui1.error_3.setVisible(False) #пароль занят
ui1.error_4.setVisible(False) #не все поля заполнены



def whod(): #авторизация
    n = 0
    myCursor.execute("select * from users ")
    myResult = myCursor.fetchall()
    for i in myResult:
        if str(ui1.inlet_lineEdit.text()) == str(i[1]) and str(ui1.inlet_lineEdit_2.text()) == str(i[2]):
            n += 1
    if n != 1:
        print("no")
        ui1.inlet_label.setText("Логин или пароль введены неверно")
        ui1.inlet_label.setGeometry(20, 20, 315, 41)
        n-=1


    else:
        print("ok")
        global profilelogin
        global profilepassword
        profilelogin=str(ui1.inlet_lineEdit.text())
        profilepassword=str(ui1.inlet_lineEdit_2.text())
        ui1.inlet_lineEdit.setVisible(False)
        ui1.inlet_lineEdit_2.setVisible(False)
        ui1.inlet_label.setVisible(False)
        ui1.inlet_label_2.setVisible(False)
        ui1.inlet_label_3.setVisible(False)
        ui1.inlet_label_4.setVisible(False)
        ui1.inlet_pushButton.setVisible(False)
        ui1.inlet_pushButton_2.setVisible(False)

        ui1.home_calendarWidget.setVisible(True)
        ui1.home_label.setVisible(True)
        ui1.home_pushButton.setVisible(True)


ui1.inlet_pushButton.clicked.connect(whod)


def registr(): #при нажатии на кнопку зарегистрироваться открывает форму регистрации
    ui1.inlet_lineEdit.setVisible(False)
    ui1.inlet_lineEdit_2.setVisible(False)
    ui1.inlet_label.setVisible(False)
    ui1.inlet_label_2.setVisible(False)
    ui1.inlet_label_3.setVisible(False)
    ui1.inlet_label_4.setVisible(False)
    ui1.inlet_pushButton.setVisible(False)
    ui1.inlet_pushButton_2.setVisible(False)

    ui1.reg_label.setVisible(True)
    ui1.reg_pushButton.setVisible(True)
    ui1.reg_lineEdit_2.setVisible(True)
    ui1.reg_label_3.setVisible(True)
    ui1.reg_label_2.setVisible(True)
    ui1.reg_lineEdit.setVisible(True)
    ui1.reg_label_4.setVisible(True)
    ui1.reg_label_5.setVisible(True)
    ui1.reg_label_6.setVisible(True)
    ui1.reg_lineEdit_3.setVisible(True)
    ui1.reg_lineEdit_4.setVisible(True)
    ui1.reg_lineEdit_5.setVisible(True)


ui1.inlet_pushButton_2.clicked.connect(registr)


def registr2(): #регистрация с добавлением в бд
    myCursor.execute("select login from users ")
    myCursor2.execute("select phone from users ")
    myResult = myCursor.fetchall()
    myResult2=myCursor2.fetchall()
    print(myResult, myResult2)
    login = str(ui1.reg_lineEdit.text())
    password = str(ui1.reg_lineEdit_2.text())
    password2=str(ui1.reg_lineEdit_3.text())
    phone= str(ui1.reg_lineEdit_4.text())
    post= str(ui1.reg_lineEdit_5.text())

    ph=[]
    lg=[]
    for i in myResult:
        lg.append(i[0])

    for d in myResult2:
        ph.append(d[0])


    print(lg, ph)

    if password!=password2:
        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)
        ui1.error_1.setVisible(True)
    elif login in lg:
        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)

        ui1.error_2.setVisible(True)
    elif phone in str(ph):
        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)

        ui1.error_3.setVisible(True)
    elif login==('') or password==('') or phone==('') or post==(''):
        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)

        ui1.error_4.setVisible(True)
    else:
        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)

        command = "INSERT INTO users (login, password, phone, post) VALUES (?, ?, ?, ?)"
        myCursor.execute(command, (login, password, phone, post))
        myConnection.commit()

        ui1.inlet_lineEdit.setVisible(True)
        ui1.inlet_lineEdit_2.setVisible(True)
        ui1.inlet_label.setVisible(True)
        ui1.inlet_label_2.setVisible(True)
        ui1.inlet_label_3.setVisible(True)
        ui1.inlet_label_4.setVisible(True)
        ui1.inlet_pushButton.setVisible(True)
        ui1.inlet_pushButton_2.setVisible(True)

        ui1.reg_label.setVisible(False)
        ui1.reg_pushButton.setVisible(False)
        ui1.reg_lineEdit_2.setVisible(False)
        ui1.reg_label_3.setVisible(False)
        ui1.reg_label_2.setVisible(False)
        ui1.reg_lineEdit.setVisible(False)
        ui1.reg_label_4.setVisible(False)
        ui1.reg_label_5.setVisible(False)
        ui1.reg_label_6.setVisible(False)
        ui1.reg_lineEdit_3.setVisible(False)
        ui1.reg_lineEdit_4.setVisible(False)
        ui1.reg_lineEdit_5.setVisible(False)

        ui1.error_1.setVisible(False)
        ui1.error_2.setVisible(False)
        ui1.error_3.setVisible(False)
        ui1.error_4.setVisible(False)

        ui1.inlet_label.setText("Вход в систему")
        ui1.inlet_label.setGeometry(110, 20, 141, 41)


ui1.reg_pushButton.clicked.connect(registr2)

def openprofile(): #открытие окна профиля
    global window2
    #global ui2
    window2 = QMainWindow()
    ui2 = Ui_MainWindow2()
    ui2.setupUi(window2)
    window.close()
    window2.show()

    ui2.prof_lineEdit.setVisible(False)
    ui2.prof_lineEdit_2.setVisible(False)
    ui2.prof_lineEdit_3.setVisible(False)
    ui2.prof_lineEdit_4.setVisible(False)
    ui2.errorprofile_1.setVisible(False)
    ui2.errorprofile_2.setVisible(False)
    ui2.changesave_pushButton.setVisible(False)

    myCursor.execute("select * from users ")
    myResult = myCursor.fetchall()
    for i in myResult:
        if profilelogin == str(i[1]) and profilepassword == str(i[2]):
            ui2.s_label_1.setText(str(i[1]))
            ui2.s_label_2.setText(str(i[2]))
            ui2.s_label_3.setText(str(i[3]))
            ui2.s_label_4.setText(str(i[4]))
            global profilephone
            profilephone=str(i[3])




    def openchangeinfo(): #открытие формы изменения
        ui2.s_label_1.setVisible(False)
        ui2.s_label_2.setVisible(False)
        ui2.s_label_3.setVisible(False)
        ui2.s_label_4.setVisible(False)
        ui2.changeopen_pushButton.setVisible(False)

        ui2.prof_lineEdit.setVisible(True)
        ui2.prof_lineEdit_2.setVisible(True)
        ui2.prof_lineEdit_3.setVisible(True)
        ui2.prof_lineEdit_4.setVisible(True)
        ui2.changesave_pushButton.setVisible(True)
        ui2.home_pushButton.setVisible(False)

        for i in myResult:
            if profilelogin == str(i[1]) and profilepassword == str(i[2]):
                ui2.prof_lineEdit.setText(str(i[1]))
                ui2.prof_lineEdit_2.setText(str(i[2]))
                ui2.prof_lineEdit_3.setText(str(i[3]))
                ui2.prof_lineEdit_4.setText(str(i[4]))

    ui2.changeopen_pushButton.clicked.connect(openchangeinfo)


    def changeinfo(): #изменение внесенных данных
        print(profilelogin,profilephone )
        myCursor.execute("select login from users ")
        myCursor2.execute("select phone from users ")
        myResult = myCursor.fetchall()
        myResult2 = myCursor2.fetchall()
        ph = []
        lg = []
        for i in myResult:
            lg.append(i[0])

        for d in myResult2:
            ph.append(d[0])                         #ВОТ ПОСЛЕ ЭТОГО МОМЕНТА НЕ РАБОТАЕТ:(((((

        # if profilelogin!=str(ui2.prof_lineEdit):
        #     if profilelogin in lg:
        #         ui2.errorprofile_1.setVisible(True)
        #         ui2.errorprofile_2.setVisible(False)
        #     else:
        #         login=str(ui2.prof_lineEdit)
        #         command = "INSERT INTO users (login) VALUES (?)"
        #         myCursor.execute(command, (login))
        #         myConnection.commit()
        #
        #
        # elif profilephone!=str(ui2.prof_lineEdit_3):
        #     if profilephone in ph:
        #         ui2.errorprofile_1.setVisible(False)
        #         ui2.errorprofile_2.setVisible(True)
        #     else:
        #         phone=str(ui2.prof_lineEdit_3)
        #         command = "INSERT INTO users (phone) VALUES (?)"
        #         myCursor.execute(command, (phone))
        #         myConnection.commit()
        # else:
            login = str(ui2.prof_lineEdit.text())
            password = str(ui2.prof_lineEdit_2.text())
            phone = str(ui2.prof_lineEdit_3.text())
            post = str(ui2.prof_lineEdit_4.text())
            command = """UPDATE users SET login=?, password=?, phone=?, post=? WHERE phone=?"""
            data = (login, password, phone, post, profilephone)
            myCursor.execute(command, data)
            myConnection.commit()


            # profilelogin=str(ui2.prof_lineEdit.text())
            # profilepassword=str(ui2.prof_lineEdit_2.text())

            ui2.s_label_1.setVisible(True)
            ui2.s_label_2.setVisible(True)
            ui2.s_label_3.setVisible(True)
            ui2.s_label_4.setVisible(True)
            ui2.changeopen_pushButton.setVisible(True)

            ui2.prof_lineEdit.setVisible(False)
            ui2.prof_lineEdit_2.setVisible(False)
            ui2.prof_lineEdit_3.setVisible(False)
            ui2.prof_lineEdit_4.setVisible(False)
            ui2.changesave_pushButton.setVisible(False)
            ui2.home_pushButton.setVisible(True)

        # for i in myResult:
        #     if str(ui2.prof_lineEdit.text()) == str(i[1]) and str(ui2.prof_lineEdit_2.text()) == str(i[2]):
        #         ui2.prof_lineEdit.setText(str(i[1]))
        #         ui2.prof_lineEdit_2.setText(str(i[2]))
        #         ui2.prof_lineEdit_3.setText(str(i[3]))
        #         ui2.prof_lineEdit_4.setText(str(i[4]))





    ui2.changesave_pushButton.clicked.connect(changeinfo)

    def ReturnToHome(): #возврат на главную страницу
        window2.close()
        window.show()

    ui2.home_pushButton.clicked.connect(ReturnToHome)


ui1.home_pushButton.clicked.connect(openprofile)

app.exec()
