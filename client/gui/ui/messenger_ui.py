# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
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
        MainWindow.resize(800, 600)
        self.action_add_friend = QAction(MainWindow)
        self.action_add_friend.setObjectName(u"action_add_friend")
        self.action_add_chat = QAction(MainWindow)
        self.action_add_chat.setObjectName(u"action_add_chat")
        self.action_addconversation = QAction(MainWindow)
        self.action_addconversation.setObjectName(u"action_addconversation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 0, 581, 571))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.LeftGroupBox = QGroupBox(self.centralwidget)
        self.LeftGroupBox.setObjectName(u"LeftGroupBox")
        self.LeftGroupBox.setGeometry(QRect(0, 0, 221, 571))
        self.searchField = QTextEdit(self.LeftGroupBox)
        self.searchField.setObjectName(u"searchField")
        self.searchField.setGeometry(QRect(10, 10, 201, 31))
        self.chat_area = QScrollArea(self.LeftGroupBox)
        self.chat_area.setObjectName(u"chat_area")
        self.chat_area.setGeometry(QRect(10, 50, 201, 521))
        self.chat_area.setAutoFillBackground(False)
        self.chat_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 199, 519))
        self.chat_area.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.button_add = QMenu(self.menubar)
        self.button_add.setObjectName(u"button_add")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.button_add.menuAction())
        self.button_add.addAction(self.action_add_friend)
        self.button_add.addAction(self.action_add_chat)
        self.button_add.addAction(self.action_addconversation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_add_friend.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u0430", None))
        self.action_add_chat.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0442", None))
        self.action_addconversation.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0441\u0435\u0434\u0443", None))
        self.LeftGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.button_add.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

