# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PPT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(691, 506)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 671, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 52, 671, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.win1 = QLabel(self.horizontalLayoutWidget_2)
        self.win1.setObjectName(u"win1")
        self.win1.setMinimumSize(QSize(50, 0))
        self.win1.setStyleSheet(u"background-color: rgb(88, 144, 94);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.win1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.win1)

        self.lose1 = QLabel(self.horizontalLayoutWidget_2)
        self.lose1.setObjectName(u"lose1")
        self.lose1.setMinimumSize(QSize(50, 0))
        self.lose1.setStyleSheet(u"background-color: rgb(189, 99, 87);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.lose1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lose1)

        self.tie1 = QLabel(self.horizontalLayoutWidget_2)
        self.tie1.setObjectName(u"tie1")
        self.tie1.setMinimumSize(QSize(50, 0))
        self.tie1.setStyleSheet(u"background-color: rgb(103, 134, 199);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.tie1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.tie1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.win2 = QLabel(self.horizontalLayoutWidget_2)
        self.win2.setObjectName(u"win2")
        self.win2.setMinimumSize(QSize(50, 0))
        self.win2.setStyleSheet(u"background-color: rgb(88, 144, 94);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.win2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.win2)

        self.lose2 = QLabel(self.horizontalLayoutWidget_2)
        self.lose2.setObjectName(u"lose2")
        self.lose2.setMinimumSize(QSize(50, 0))
        self.lose2.setStyleSheet(u"background-color: rgb(189, 99, 87);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.lose2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lose2)

        self.tie2 = QLabel(self.horizontalLayoutWidget_2)
        self.tie2.setObjectName(u"tie2")
        self.tie2.setMinimumSize(QSize(50, 0))
        self.tie2.setStyleSheet(u"background-color: rgb(103, 134, 199);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.tie2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.tie2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 100, 671, 211))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.groupBox = QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.img1 = QLabel(self.groupBox)
        self.img1.setObjectName(u"img1")
        self.img1.setGeometry(QRect(9, 29, 231, 171))
        self.img1.setStyleSheet(u"background-color: rgb(207, 178, 0);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;")
        self.img1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.groupBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(250, 0))
        self.img2 = QLabel(self.groupBox_2)
        self.img2.setObjectName(u"img2")
        self.img2.setGeometry(QRect(9, 29, 231, 171))
        self.img2.setStyleSheet(u"background-color: rgb(207, 178, 0);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;")
        self.img2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.horizontalLayoutWidget_4 = QWidget(Form)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 320, 671, 80))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.seleccion = QComboBox(self.horizontalLayoutWidget_4)
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.setObjectName(u"seleccion")
        self.seleccion.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.seleccion)

        self.groupBox_3 = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"color: gray;")
        self.msg1 = QLabel(self.groupBox_3)
        self.msg1.setObjectName(u"msg1")
        self.msg1.setGeometry(QRect(10, 20, 191, 51))
        self.msg1.setStyleSheet(u"color: black;")
        self.msg1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"color: gray;")
        self.msg2 = QLabel(self.groupBox_4)
        self.msg2.setObjectName(u"msg2")
        self.msg2.setGeometry(QRect(10, 20, 191, 51))
        self.msg2.setStyleSheet(u"color: black;")
        self.msg2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.groupBox_4)

        self.horizontalLayoutWidget_5 = QWidget(Form)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 410, 221, 22))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_17 = QLabel(self.horizontalLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 0))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_17)

        self.label_18 = QLabel(self.horizontalLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(50, 0))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.label_19 = QLabel(self.horizontalLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.horizontalLayoutWidget_6 = QWidget(Form)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 430, 221, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.win3 = QLabel(self.horizontalLayoutWidget_6)
        self.win3.setObjectName(u"win3")
        self.win3.setMinimumSize(QSize(50, 0))
        self.win3.setStyleSheet(u"background-color: rgb(88, 144, 94);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.win3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.win3)

        self.lose3 = QLabel(self.horizontalLayoutWidget_6)
        self.lose3.setObjectName(u"lose3")
        self.lose3.setMinimumSize(QSize(50, 0))
        self.lose3.setStyleSheet(u"background-color: rgb(189, 99, 87);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.lose3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lose3)

        self.tie3 = QLabel(self.horizontalLayoutWidget_6)
        self.tie3.setObjectName(u"tie3")
        self.tie3.setMinimumSize(QSize(50, 0))
        self.tie3.setStyleSheet(u"background-color: rgb(103, 134, 199);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"font: bold 14px;")
        self.tie3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.tie3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.horizontalLayoutWidget_7 = QWidget(Form)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(290, 410, 351, 81))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.jugar = QPushButton(self.horizontalLayoutWidget_7)
        self.jugar.setObjectName(u"jugar")
        self.jugar.setMinimumSize(QSize(0, 0))
        self.jugar.setBaseSize(QSize(0, 0))
        self.jugar.setStyleSheet(u"background-color: green;\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"	height: 40px;")

        self.horizontalLayout_10.addWidget(self.jugar)

        self.cerrar = QPushButton(self.horizontalLayoutWidget_7)
        self.cerrar.setObjectName(u"cerrar")
        self.cerrar.setStyleSheet(u"background-color: red;\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"	height: 40px;")

        self.horizontalLayout_10.addWidget(self.cerrar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Win", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Lose", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tie", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Win", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Lose", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tie", None))
        self.win1.setText(QCoreApplication.translate("Form", u"0", None))
        self.lose1.setText(QCoreApplication.translate("Form", u"0", None))
        self.tie1.setText(QCoreApplication.translate("Form", u"0", None))
        self.win2.setText(QCoreApplication.translate("Form", u"0", None))
        self.lose2.setText(QCoreApplication.translate("Form", u"0", None))
        self.tie2.setText(QCoreApplication.translate("Form", u"0", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Jugador", None))
        self.img1.setText(QCoreApplication.translate("Form", u"IMG", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Oponente", None))
        self.img2.setText(QCoreApplication.translate("Form", u"IMG", None))
        self.seleccion.setItemText(0, QCoreApplication.translate("Form", u"Seleccione una opci\u00f3n", None))
        self.seleccion.setItemText(1, QCoreApplication.translate("Form", u"Piedra", None))
        self.seleccion.setItemText(2, QCoreApplication.translate("Form", u"Papel", None))
        self.seleccion.setItemText(3, QCoreApplication.translate("Form", u"Tijera", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Mensajes Juego", None))
        self.msg1.setText(QCoreApplication.translate("Form", u"MSG", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Mensajes Sistema", None))
        self.msg2.setText(QCoreApplication.translate("Form", u"MSG", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Win", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Lose", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Tie", None))
        self.win3.setText(QCoreApplication.translate("Form", u"0", None))
        self.lose3.setText(QCoreApplication.translate("Form", u"0", None))
        self.tie3.setText(QCoreApplication.translate("Form", u"0", None))
        self.jugar.setText(QCoreApplication.translate("Form", u"Jugar", None))
        self.cerrar.setText(QCoreApplication.translate("Form", u"Cerrar", None))
    # retranslateUi

