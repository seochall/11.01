# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 547)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reg_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label.setGeometry(QtCore.QRect(70, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.reg_label.setFont(font)
        self.reg_label.setObjectName("reg_label")
        self.reg_lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reg_lineEdit_2.setGeometry(QtCore.QRect(80, 160, 181, 31))
        self.reg_lineEdit_2.setObjectName("reg_lineEdit_2")
        self.reg_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label_2.setGeometry(QtCore.QRect(80, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_label_2.setFont(font)
        self.reg_label_2.setObjectName("reg_label_2")
        self.reg_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reg_pushButton.setGeometry(QtCore.QRect(80, 440, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.reg_pushButton.setFont(font)
        self.reg_pushButton.setObjectName("reg_pushButton")
        self.reg_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reg_lineEdit.setGeometry(QtCore.QRect(80, 96, 181, 31))
        self.reg_lineEdit.setObjectName("reg_lineEdit")
        self.reg_label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label_3.setGeometry(QtCore.QRect(80, 140, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_label_3.setFont(font)
        self.reg_label_3.setObjectName("reg_label_3")
        self.reg_lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reg_lineEdit_3.setGeometry(QtCore.QRect(80, 230, 181, 31))
        self.reg_lineEdit_3.setObjectName("reg_lineEdit_3")
        self.reg_label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label_4.setGeometry(QtCore.QRect(80, 210, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_label_4.setFont(font)
        self.reg_label_4.setObjectName("reg_label_4")
        self.reg_lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reg_lineEdit_4.setGeometry(QtCore.QRect(80, 300, 181, 31))
        self.reg_lineEdit_4.setObjectName("reg_lineEdit_4")
        self.reg_label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label_5.setGeometry(QtCore.QRect(80, 280, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_label_5.setFont(font)
        self.reg_label_5.setObjectName("reg_label_5")
        self.reg_label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.reg_label_6.setGeometry(QtCore.QRect(80, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_label_6.setFont(font)
        self.reg_label_6.setObjectName("reg_label_6")
        self.reg_lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reg_lineEdit_5.setGeometry(QtCore.QRect(80, 370, 181, 31))
        self.reg_lineEdit_5.setObjectName("reg_lineEdit_5")
        self.error_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_3.setGeometry(QtCore.QRect(30, 410, 291, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.error_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.error_3.setFont(font)
        self.error_3.setStyleSheet("color: rgb(202, 0, 0);")
        self.error_3.setObjectName("error_3")
        self.error_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_4.setGeometry(QtCore.QRect(60, 410, 211, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.error_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.error_4.setFont(font)
        self.error_4.setStyleSheet("color: rgb(202, 0, 0);")
        self.error_4.setObjectName("error_4")
        self.error_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_1.setGeometry(QtCore.QRect(100, 410, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.error_1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.error_1.setFont(font)
        self.error_1.setStyleSheet("color: rgb(202, 0, 0);")
        self.error_1.setObjectName("error_1")
        self.error_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_2.setGeometry(QtCore.QRect(110, 410, 131, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        self.error_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.error_2.setFont(font)
        self.error_2.setStyleSheet("color: rgb(202, 0, 0);")
        self.error_2.setObjectName("error_2")
        self.inlet_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.inlet_label.setGeometry(QtCore.QRect(100, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.inlet_label.setFont(font)
        self.inlet_label.setObjectName("inlet_label")
        self.inlet_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.inlet_label_2.setGeometry(QtCore.QRect(80, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inlet_label_2.setFont(font)
        self.inlet_label_2.setObjectName("inlet_label_2")
        self.inlet_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inlet_lineEdit.setEnabled(True)
        self.inlet_lineEdit.setGeometry(QtCore.QRect(80, 96, 181, 31))
        self.inlet_lineEdit.setObjectName("inlet_lineEdit")
        self.inlet_label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.inlet_label_3.setGeometry(QtCore.QRect(80, 140, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inlet_label_3.setFont(font)
        self.inlet_label_3.setObjectName("inlet_label_3")
        self.inlet_lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inlet_lineEdit_2.setGeometry(QtCore.QRect(80, 160, 181, 31))
        self.inlet_lineEdit_2.setObjectName("inlet_lineEdit_2")
        self.inlet_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inlet_pushButton.setGeometry(QtCore.QRect(80, 210, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.inlet_pushButton.setFont(font)
        self.inlet_pushButton.setObjectName("inlet_pushButton")
        self.inlet_pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inlet_pushButton_2.setGeometry(QtCore.QRect(120, 270, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inlet_pushButton_2.setFont(font)
        self.inlet_pushButton_2.setObjectName("inlet_pushButton_2")
        self.inlet_label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.inlet_label_4.setGeometry(QtCore.QRect(110, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.inlet_label_4.setFont(font)
        self.inlet_label_4.setObjectName("inlet_label_4")
        self.home_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.home_label.setGeometry(QtCore.QRect(80, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.home_label.setFont(font)
        self.home_label.setObjectName("home_label")
        self.home_calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.home_calendarWidget.setGeometry(QtCore.QRect(20, 100, 311, 211))
        self.home_calendarWidget.setObjectName("home_calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reg_label.setText(_translate("MainWindow", "Регистрация на сайте"))
        self.reg_label_2.setText(_translate("MainWindow", "Логин"))
        self.reg_pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.reg_label_3.setText(_translate("MainWindow", "Пароль"))
        self.reg_label_4.setText(_translate("MainWindow", "Повторите пароль"))
        self.reg_label_5.setText(_translate("MainWindow", "Номер телефона"))
        self.reg_label_6.setText(_translate("MainWindow", "Должность"))
        self.error_3.setText(_translate("MainWindow", "Данный номер телефона уже зарегистрирован"))
        self.error_4.setText(_translate("MainWindow", "Все поля должны быть заполнены"))
        self.error_1.setText(_translate("MainWindow", "Пароли не совпадают"))
        self.error_2.setText(_translate("MainWindow", "Данный логин занят"))
        self.inlet_label.setText(_translate("MainWindow", "Вход в систему"))
        self.inlet_label_2.setText(_translate("MainWindow", "Логин"))
        self.inlet_label_3.setText(_translate("MainWindow", "Пароль"))
        self.inlet_pushButton.setText(_translate("MainWindow", "Вход"))
        self.inlet_pushButton_2.setText(_translate("MainWindow", "Регистрация"))
        self.inlet_label_4.setText(_translate("MainWindow", "Впервые на сайте?"))
        self.home_label.setText(_translate("MainWindow", "Добро пожаловать!"))