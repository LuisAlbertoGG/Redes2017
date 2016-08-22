#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
#from usuario import Registro
import sys
#sys.path.insert(0, '../')
#sys.path.insert(1, '../Constants')
sys.path.insert(0, '../Channel')
from Constants.Constants import *
from Channel.ApiServer import *
from Channel.ApiClient import *
from Channel.Channel import *
from chat import Chat






class LoginWindow(QtGui.QWidget):

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        mipuerto = QtGui.QLabel('Cual es mi puerto?', self)
        mipuerto1 = QtGui.QLineEdit()
	tupuerto = QtGui.QLabel('Cual es el puerto del contacto?', self)
        tupuerto1 = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Acceder')
        #register_button = QtGui.QPushButton('Registrarse')
        login_button.clicked.connect(lambda: self.access(mipuerto1, tupuerto1))
        #register_button.clicked.connect(self.registro)
        grid = QtGui.QGridLayout()
        grid.addWidget(mipuerto, 0, 0)
        grid.addWidget(mipuerto1, 1, 0)
        grid.addWidget(login_button, 5, 1)
        #grid.addWidget(register_button, 6, 1)
        grid.addWidget(tupuerto, 2, 0)
        grid.addWidget(tupuerto1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()

    def registro(self):
        chat = Chat()
        chat.exec_()

    def access(self, mipuerto1=None, tupuerto1=None):

        mipuertofinal1 = int(mipuerto1.text())
	tupuertofinal1 = int(tupuerto1.text())
        miservidor =  Channel(None, mipuertofinal1, tupuertofinal1)
        miservidor.start()
        chat = Chat(mipuertofinal1, tupuertofinal1)
        #chat.mipuertofinal = mipuertofinal1
        #chat.tupuertofinal = tupuertofinal1
        self.close()
        chat.show()

    