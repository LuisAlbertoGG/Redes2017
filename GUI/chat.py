#! /usr/bin/env python
# -*- coding: utf-8 -*-

#from .. import *
#from ..Constants.Constants import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
import sys
import  pyaudio
sys.path.insert(0, '../Constants')
sys.path.insert(0, '../Channel')
sys.path.insert(0, '..')
from Channel.ApiClient import *
from Channel.ApiServer import *
from Constants.Constants import *
from login import *
from Channel.Channel import *
#from GraphicalUserInterface import local


class Chat(QtGui.QWidget):

    def __init__(self, mipuertofinal, tupuertofinal, local):
        super(Chat, self).__init__()
        self.mipuertofinal = mipuertofinal
        self.tupuertofinal = tupuertofinal
        self.local = local
        #self.local = local
        self.initUI()


    def initUI(self):
        self.conversacion = QtGui.QLabel('Conversacion el puerto '+str(self.mipuertofinal)+' con el puerto '+str(self.tupuertofinal), self)
        self.conversacion1 = QtGui.QTextEdit()
        self.conversacion2 = QtGui.QLineEdit()
        self.conversacion1.setReadOnly(True)
        #n_contrasenha = QtGui.QLabel('Contraseña:', self)
        #n_contrasenha1 = QtGui.QLineEdit()
        #n_contrasenha1 = QtGui.QLineEdit()
        #Definimos el boton para llamar
        self.llamada = QtGui.QPushButton('Llamar')
        self.enviar = QtGui.QPushButton('Enviar')
        self.llamada.clicked.connect(lambda: self.llama())
        self.enviar.clicked.connect(lambda: self.access(self.conversacion2))
        grid = QtGui.QGridLayout()
        grid.addWidget(self.conversacion, 0, 0)
        grid.addWidget(self.conversacion1, 1, 0)
        grid.addWidget(self.conversacion2, 6, 0)
        grid.addWidget(self.llamada, 6,6)
        grid.addWidget(self.enviar, 6, 5)
        #grid.addWidget(n_contrasenha, 2, 0)
        #grid.addWidget(n_contrasenha1, 3, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, CHAT_WIDTH, CHAT_HEIGTH)
        self.setWindowTitle('Chat')
        self.show()

    def access(self, conversacion2=None):

        mensaje = conversacion2.text()
        msg = str(self.mipuertofinal)+' dice: '+mensaje
        envia_mensaje = Channel(None, None, self.tupuertofinal)
        envia_mensaje.send_text(msg, self.local)
        self.conversacion1.append(msg)
        #temp1 = str(mensaje)
        #userAscii = [ord(c) for c in temp1]
        #contraAscii = [ord(c) for c in temp2]
        #for x in range(0,len(userAscii)):
        #    userAscii[x] = chr(userAscii[x] + 5)
        #for x in range(0,len(contraAscii)):
        #    contraAscii[x] = chr(contraAscii[x] + 5)
        #temp1 = ''.join(userAscii)
        #temp2 = ''.join(contraAscii)
    def llama(self):
        print "llamando"
        self.conversacion1.append("Llamando a "+str(self.tupuertofinal))
        envia_audio = Channel(None, None, self.tupuertofinal)
        envia_audio.send_audio(self.local)

        #print mensaje
        #self.otro = OtroWidget

        #self.otro.show()
    def mostar(self, msg):
        print "intentando"
        self.conversacion1.append(msg)

    #self.btnExit.clicked.connect(self.close)
    #self.actionExit.triggered.connect(self.close)        

     #def closeEvent(self,event):
      #  result = QtGui.QMessageBox.question(self,"Confirm Exit...","Are you sure you want to exit ?",QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
       # event.ignore()
        #if result == QtGui.QMessageBox.Yes:
         #   event.accept()
