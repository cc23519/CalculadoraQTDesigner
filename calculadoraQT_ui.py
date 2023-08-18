# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadoraQT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import RecursosVisuais_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(285, 410)
        MainWindow.setMinimumSize(QSize(285, 410))
        MainWindow.setMaximumSize(QSize(285, 410))
        icon = QIcon()
        icon.addFile(u":/Icone/\u00cdcones/calculate_FILL0_wght400_GRAD200_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.calculadoraUI = QWidget(MainWindow)
        self.calculadoraUI.setObjectName(u"calculadoraUI")
        self.layoutWidget = QWidget(self.calculadoraUI)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 266, 387))
        self.painelCalculadoraUI = QVBoxLayout(self.layoutWidget)
        self.painelCalculadoraUI.setObjectName(u"painelCalculadoraUI")
        self.painelCalculadoraUI.setContentsMargins(0, 0, 0, 0)
        self.visor = QLineEdit(self.layoutWidget)
        self.visor.setObjectName(u"visor")
        self.visor.setMinimumSize(QSize(261, 51))
        self.visor.setMaximumSize(QSize(261, 51))
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(18)
        self.visor.setFont(font)
        self.visor.setStyleSheet(u"border-radius: 10px;border-width: 1px;color: black;\n"
"background-color: rgb(229, 229, 229);")

        self.painelCalculadoraUI.addWidget(self.visor)

        self.tecladoCalculadoraUI = QHBoxLayout()
        self.tecladoCalculadoraUI.setObjectName(u"tecladoCalculadoraUI")
        self.tecladoNumCalculadoraUI = QGridLayout()
        self.tecladoNumCalculadoraUI.setObjectName(u"tecladoNumCalculadoraUI")
        self.buttonX2 = QPushButton(self.layoutWidget)
        self.buttonX2.setObjectName(u"buttonX2")
        self.buttonX2.setMinimumSize(QSize(60, 60))
        self.buttonX2.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Terminal"])
        font1.setPointSize(14)
        self.buttonX2.setFont(font1)
        self.buttonX2.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.buttonX2, 0, 1, 1, 1)

        self.buttonDiv1 = QPushButton(self.layoutWidget)
        self.buttonDiv1.setObjectName(u"buttonDiv1")
        self.buttonDiv1.setMinimumSize(QSize(60, 60))
        self.buttonDiv1.setMaximumSize(QSize(60, 60))
        self.buttonDiv1.setFont(font1)
        self.buttonDiv1.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.buttonDiv1, 0, 0, 1, 1)

        self.buttonCE = QPushButton(self.layoutWidget)
        self.buttonCE.setObjectName(u"buttonCE")
        self.buttonCE.setMinimumSize(QSize(60, 60))
        self.buttonCE.setMaximumSize(QSize(60, 60))
        self.buttonCE.setFont(font1)
        self.buttonCE.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.buttonCE, 0, 2, 1, 1)

        self.button9 = QPushButton(self.layoutWidget)
        self.button9.setObjectName(u"button9")
        self.button9.setMinimumSize(QSize(60, 60))
        self.button9.setMaximumSize(QSize(60, 60))
        self.button9.setFont(font1)
        self.button9.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button9, 1, 2, 1, 1)

        self.button6 = QPushButton(self.layoutWidget)
        self.button6.setObjectName(u"button6")
        self.button6.setMinimumSize(QSize(60, 60))
        self.button6.setMaximumSize(QSize(60, 60))
        self.button6.setFont(font1)
        self.button6.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button6, 2, 2, 1, 1)

        self.button4 = QPushButton(self.layoutWidget)
        self.button4.setObjectName(u"button4")
        self.button4.setMinimumSize(QSize(60, 60))
        self.button4.setMaximumSize(QSize(60, 60))
        self.button4.setFont(font1)
        self.button4.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button4, 2, 0, 1, 1)

        self.button8 = QPushButton(self.layoutWidget)
        self.button8.setObjectName(u"button8")
        self.button8.setMinimumSize(QSize(60, 60))
        self.button8.setMaximumSize(QSize(60, 60))
        self.button8.setFont(font1)
        self.button8.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button8, 1, 1, 1, 1)

        self.button7 = QPushButton(self.layoutWidget)
        self.button7.setObjectName(u"button7")
        self.button7.setMinimumSize(QSize(60, 60))
        self.button7.setMaximumSize(QSize(60, 60))
        self.button7.setFont(font1)
        self.button7.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button7, 1, 0, 1, 1)

        self.button5 = QPushButton(self.layoutWidget)
        self.button5.setObjectName(u"button5")
        self.button5.setMinimumSize(QSize(60, 60))
        self.button5.setMaximumSize(QSize(60, 60))
        self.button5.setFont(font1)
        self.button5.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button5, 2, 1, 1, 1)

        self.button2 = QPushButton(self.layoutWidget)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(60, 60))
        self.button2.setMaximumSize(QSize(60, 60))
        self.button2.setFont(font1)
        self.button2.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button2, 3, 1, 1, 1)

        self.button1 = QPushButton(self.layoutWidget)
        self.button1.setObjectName(u"button1")
        self.button1.setMinimumSize(QSize(60, 60))
        self.button1.setMaximumSize(QSize(60, 60))
        self.button1.setFont(font1)
        self.button1.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button1, 3, 0, 1, 1)

        self.button3 = QPushButton(self.layoutWidget)
        self.button3.setObjectName(u"button3")
        self.button3.setMinimumSize(QSize(60, 60))
        self.button3.setMaximumSize(QSize(60, 60))
        self.button3.setFont(font1)
        self.button3.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button3, 3, 2, 1, 1)

        self.buttonVirgula = QPushButton(self.layoutWidget)
        self.buttonVirgula.setObjectName(u"buttonVirgula")
        self.buttonVirgula.setMinimumSize(QSize(60, 60))
        self.buttonVirgula.setMaximumSize(QSize(60, 60))
        self.buttonVirgula.setFont(font1)
        self.buttonVirgula.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.buttonVirgula, 4, 2, 1, 1)

        self.button0 = QPushButton(self.layoutWidget)
        self.button0.setObjectName(u"button0")
        self.button0.setMinimumSize(QSize(60, 60))
        self.button0.setMaximumSize(QSize(60, 60))
        self.button0.setFont(font1)
        self.button0.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.button0, 4, 1, 1, 1)

        self.buttonMaiseMenos = QPushButton(self.layoutWidget)
        self.buttonMaiseMenos.setObjectName(u"buttonMaiseMenos")
        self.buttonMaiseMenos.setMinimumSize(QSize(60, 60))
        self.buttonMaiseMenos.setMaximumSize(QSize(60, 60))
        self.buttonMaiseMenos.setFont(font1)
        self.buttonMaiseMenos.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoNumCalculadoraUI.addWidget(self.buttonMaiseMenos, 4, 0, 1, 1)


        self.tecladoCalculadoraUI.addLayout(self.tecladoNumCalculadoraUI)

        self.tecladoOpeCalculadoraUI = QGridLayout()
        self.tecladoOpeCalculadoraUI.setObjectName(u"tecladoOpeCalculadoraUI")
        self.buttonDiv = QPushButton(self.layoutWidget)
        self.buttonDiv.setObjectName(u"buttonDiv")
        self.buttonDiv.setMinimumSize(QSize(60, 60))
        self.buttonDiv.setMaximumSize(QSize(60, 60))
        self.buttonDiv.setFont(font1)
        self.buttonDiv.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoOpeCalculadoraUI.addWidget(self.buttonDiv, 0, 0, 1, 1)

        self.buttonMulti = QPushButton(self.layoutWidget)
        self.buttonMulti.setObjectName(u"buttonMulti")
        self.buttonMulti.setMinimumSize(QSize(60, 60))
        self.buttonMulti.setMaximumSize(QSize(60, 60))
        self.buttonMulti.setFont(font1)
        self.buttonMulti.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoOpeCalculadoraUI.addWidget(self.buttonMulti, 1, 0, 1, 1)

        self.buttonMen = QPushButton(self.layoutWidget)
        self.buttonMen.setObjectName(u"buttonMen")
        self.buttonMen.setMinimumSize(QSize(60, 60))
        self.buttonMen.setMaximumSize(QSize(60, 60))
        self.buttonMen.setFont(font1)
        self.buttonMen.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoOpeCalculadoraUI.addWidget(self.buttonMen, 2, 0, 1, 1)

        self.buttonMai = QPushButton(self.layoutWidget)
        self.buttonMai.setObjectName(u"buttonMai")
        self.buttonMai.setMinimumSize(QSize(60, 60))
        self.buttonMai.setMaximumSize(QSize(60, 60))
        self.buttonMai.setFont(font1)
        self.buttonMai.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoOpeCalculadoraUI.addWidget(self.buttonMai, 3, 0, 1, 1)

        self.buttonIgual = QPushButton(self.layoutWidget)
        self.buttonIgual.setObjectName(u"buttonIgual")
        self.buttonIgual.setMinimumSize(QSize(60, 60))
        self.buttonIgual.setMaximumSize(QSize(60, 60))
        self.buttonIgual.setFont(font1)
        self.buttonIgual.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 10px;border-width: 1px;color: black;")

        self.tecladoOpeCalculadoraUI.addWidget(self.buttonIgual, 4, 0, 1, 1)


        self.tecladoCalculadoraUI.addLayout(self.tecladoOpeCalculadoraUI)


        self.painelCalculadoraUI.addLayout(self.tecladoCalculadoraUI)

        MainWindow.setCentralWidget(self.calculadoraUI)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.visor.setText("")
        self.buttonX2.setText(QCoreApplication.translate("MainWindow", u"X2", None))
        self.buttonDiv1.setText(QCoreApplication.translate("MainWindow", u"X/1", None))
        self.buttonCE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.button9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.buttonVirgula.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.button0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.buttonMaiseMenos.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.buttonDiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.buttonMulti.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.buttonMen.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.buttonMai.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.buttonIgual.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

