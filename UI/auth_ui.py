# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 264)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.login_label = QLabel(self.centralwidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(40, 40, 55, 16))
        self.pass_label = QLabel(self.centralwidget)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setGeometry(QRect(40, 94, 55, 16))
        self.auth_button = QPushButton(self.centralwidget)
        self.auth_button.setObjectName(u"auth_button")
        self.auth_button.setGeometry(QRect(80, 160, 93, 28))
        self.login_text_filed = QLineEdit(self.centralwidget)
        self.login_text_filed.setObjectName(u"login_text_filed")
        self.login_text_filed.setGeometry(QRect(140, 38, 181, 22))
        self.pass_text_filed = QLineEdit(self.centralwidget)
        self.pass_text_filed.setObjectName(u"pass_text_filed")
        self.pass_text_filed.setGeometry(QRect(140, 90, 181, 22))
        self.regestation_buttion = QPushButton(self.centralwidget)
        self.regestation_buttion.setObjectName(u"regestation_buttion")
        self.regestation_buttion.setGeometry(QRect(220, 160, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 481, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pass_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.auth_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.regestation_buttion.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

