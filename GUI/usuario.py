#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ..Constants.Constants import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
import sys


class Registro(QtGui.QWidget):

    def __init__(self):
        super(Registro, self).__init__()
        self.initUI()


    def initUI(self):
        n_usuario = QtGui.QLabel('Nombre de usuario:', self)
        n_usuario1 = QtGui.QLineEdit()
        n_contrasenha = QtGui.QLabel('Contraseña:', self)
        n_contrasenha1 = QtGui.QLineEdit()
        #n_contrasenha1 = QtGui.QLineEdit()
        #Definimos el boton para llamar

        login_button = QtGui.QPushButton('Agregar usuario')
        login_button.clicked.connect(lambda: self.access(n_usuario1, n_contrasenha1))
        grid = QtGui.QGridLayout()
        grid.addWidget(n_usuario, 0, 0)
        grid.addWidget(n_usuario1, 1, 0)
        grid.addWidget(login_button, 5, 1)
        grid.addWidget(n_contrasenha, 2, 0)
        grid.addWidget(n_contrasenha1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()

    def access(self, n_usuario1=None, n_contrasenha1=None):

        userName = n_usuario1.text()
        contra = n_contrasenha1.text()
        temp1 = str(userName)
        temp2 = str(contra)
        userAscii = [ord(c) for c in temp1]
        contraAscii = [ord(c) for c in temp2]
        for x in range(0,len(userAscii)):
            userAscii[x] = chr(userAscii[x] + 5)
        for x in range(0,len(contraAscii)):
            contraAscii[x] = chr(contraAscii[x] + 5)
        temp1 = ''.join(userAscii)
        temp2 = ''.join(contraAscii)
        

        print temp1
        print temp2
        #self.otro = OtroWidget

        #self.otro.show()
        self.close()