#! /usr/bin/env python
# -*- coding: utf-8 -*-

#from .. import *
#from ..Constants.Constants import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
import sys
sys.path.insert(0, '../Constants')
from Constants.Constants import *
from login import *


class Chat(QtGui.QWidget):

    def __init__(self):
        super(Chat, self).__init__()
        mipuertofinal = 0
        tupuertofinal = 0
        self.initUI()


    def initUI(self):
        self.conversacion = QtGui.QLabel('Conversacion', self)
        self.conversacion1 = QtGui.QTextEdit()
        self.conversacion2 = QtGui.QLineEdit()
        self.conversacion1.setReadOnly(True)
        #n_contrasenha = QtGui.QLabel('Contraseña:', self)
        #n_contrasenha1 = QtGui.QLineEdit()
        #n_contrasenha1 = QtGui.QLineEdit()
        #Definimos el boton para llamar

        self.enviar = QtGui.QPushButton('Enviar')
        self.enviar.clicked.connect(lambda: self.access(self.conversacion2))
        grid = QtGui.QGridLayout()
        grid.addWidget(self.conversacion, 0, 0)
        grid.addWidget(self.conversacion1, 1, 0)
        grid.addWidget(self.conversacion2, 6, 0)
        grid.addWidget(self.enviar, 6, 6)
        #grid.addWidget(n_contrasenha, 2, 0)
        #grid.addWidget(n_contrasenha1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, CHAT_WIDTH, CHAT_HEIGTH)
        self.setWindowTitle('Chat')
        self.show()

    def access(self, conversacion2=None):

        mensaje = conversacion2.text()
        #conversacion1.insertPlainText (self, mensaje)
        self.conversacion1.append(self.mipuertofinal+' dice: '+mensaje)
        #temp1 = str(mensaje)
        #userAscii = [ord(c) for c in temp1]
        #contraAscii = [ord(c) for c in temp2]
        #for x in range(0,len(userAscii)):
        #    userAscii[x] = chr(userAscii[x] + 5)
        #for x in range(0,len(contraAscii)):
        #    contraAscii[x] = chr(contraAscii[x] + 5)
        #temp1 = ''.join(userAscii)
        #temp2 = ''.join(contraAscii)
        

        print mensaje
        #self.otro = OtroWidget

        #self.otro.show()
        