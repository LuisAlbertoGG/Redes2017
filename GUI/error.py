#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel

#           Mis bibliotecas

import sys
LOGIN_WIDTH = 250
LOGIN_HEIGTH = 200
DEFAULT_POSTION_X =350
DEFAULT_POSTION_Y =350

#**************************************************
#Clase que representa la ventana de login, en donde
#se pide la ip del contacto con el que se mantendrá
#el chat.
#**************************************************
class LoginWindow(QtGui.QWidget):

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        mensaje = QtGui.QLabel('Error: no tienes acceso al sistema', self)
        m_widget = QtGui.QLineEdit()
        #Definimos el boton para llamar
        login_button = QtGui.QPushButton('Ok')
        login_button.clicked.connect(lambda: self.access(m_widget))
        grid = QtGui.QGridLayout()
        grid.addWidget(mensaje, 0, 0)
        grid.addWidget(m_widget, 1, 0)
        grid.addWidget(login_button, 2, 1)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Informacion')
        self.show()

    def access(self, m_widget=None):

        msj = m_widget.text()
        print msj
        #self.otro = OtroWidget

        #self.otro.show()
        self.close()


# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = LoginWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
