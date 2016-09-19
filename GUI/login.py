#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
import sys
sys.path.insert(0, '../Channel')
sys.path.insert(0, '../Constants')
from Constants.Constants import *
from Constants.AuxiliarFunctions import get_ip_address
from Channel.ApiServer import *
from Channel.ApiClient import *
from Channel.Channel import *
from chat import Chat






class LoginWindow(QtGui.QWidget):#interfaz que pide los puertos

    global chat

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):#La creación de botones ventanas y demás de la interfaz
        mipuerto = QtGui.QLabel('Cual es mi puerto?', self)
        mipuerto1 = QtGui.QLineEdit()
        tupuerto = QtGui.QLabel('Cual es el puerto del contacto?', self)
        tupuerto1 = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Acceder')
        login_button.clicked.connect(lambda: self.access(mipuerto1, tupuerto1))
        grid = QtGui.QGridLayout()
        grid.addWidget(mipuerto, 0, 0)
        grid.addWidget(mipuerto1, 1, 0)
        grid.addWidget(login_button, 5, 1)
        grid.addWidget(tupuerto, 2, 0)
        grid.addWidget(tupuerto1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()


    def access(self, mipuerto1=None, tupuerto1=None):#Método que define las acciones a realizar cuando se presiona el botón acceder

        mipuertofinal1 = int(mipuerto1.text())
        tupuertofinal1 = int(tupuerto1.text())
        miservidor =  Channel(None, mipuertofinal1, tupuertofinal1)
        self.chat = Chat(mipuertofinal1, tupuertofinal1, True)
        self.close()
        import __builtin__
        __builtin__.chat = self.chat
        self.chat.show()

class LoginWindowIP(QtGui.QWidget):#Interfaz que pide las ip's

    chat = None

    def __init__(self ):
        super(LoginWindowIP, self).__init__()
        self.initUI()


    def initUI(self):#interfaz que pide los puertos
        tupuerto = QtGui.QLabel('Cual es la IP del contacto?', self)
        tupuerto1 = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Acceder')
        login_button.clicked.connect(lambda: self.access(tupuerto1))
        grid = QtGui.QGridLayout()
        grid.addWidget(login_button, 5, 1)
        grid.addWidget(tupuerto, 0, 0)
        grid.addWidget(tupuerto1, 1, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()

   

    def access(self,tupuerto1=None):#Método que define las acciones a realizar cuando se presiona el botón acceder

        tupuertofinal1 = str(tupuerto1.text())
        a = get_ip_address()
        self.chat = Chat(a, tupuertofinal1, False)
        miservidor =  Channel(tupuerto1, None, None)
        self.close()
        import __builtin__
        __builtin__.chat = self.chat
        chat.show()

    