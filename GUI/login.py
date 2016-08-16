#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from usuario import Registro
from ..Constants.Constants import *
import sys






class LoginWindow(QtGui.QWidget):

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        n_usuario = QtGui.QLabel('Nombre de usuario:', self)
        n_usuario1 = QtGui.QLineEdit()
	n_contrasenha = QtGui.QLabel('Contraseña:', self)
        n_contrasenha1 = QtGui.QLineEdit()
        login_button = QtGui.QPushButton('Acceder')
        register_button = QtGui.QPushButton('Registrarse')
        login_button.clicked.connect(lambda: self.access(n_usuario1, n_contrasenha1))
        register_button.clicked.connect(self.registro)
        grid = QtGui.QGridLayout()
        grid.addWidget(n_usuario, 0, 0)
        grid.addWidget(n_usuario1, 1, 0)
        grid.addWidget(login_button, 5, 1)
        grid.addWidget(register_button, 6, 1)
        grid.addWidget(n_contrasenha, 2, 0)
        grid.addWidget(n_contrasenha1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()

    def access(self, n_usuario1=None, n_contrasenha1=None):

        userName = n_usuario1.text()
	contra = n_contrasenha1.text()
        print userName
        print contra
        self.close()

    def registro(self):
        registro = Registro()
        #registro.exec_()