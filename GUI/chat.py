#! /usr/bin/env python
# -*- coding: utf-8 -*-


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



class Chat(QtGui.QWidget):#Clase de la ventana de chat

    def __init__(self, mipuertofinal, tupuertofinal, local):#Método que inicia el chat usando los valores de la conexión
        super(Chat, self).__init__()
        self.mipuertofinal = mipuertofinal
        self.tupuertofinal = tupuertofinal
        self.local = local
        self.initUI()


    def initUI(self):#Método que crea la interfaz
        self.conversacion = QtGui.QLabel('Conversacion el puerto '+str(self.mipuertofinal)+' con el puerto '+str(self.tupuertofinal), self)
        self.conversacion1 = QtGui.QTextEdit()
        self.conversacion2 = QtGui.QLineEdit()
        self.conversacion1.setReadOnly(True)
        self.llamada = QtGui.QPushButton('Llamar')#Definimos el boton para llamar
        self.enviar = QtGui.QPushButton('Enviar')
        self.llamada.clicked.connect(lambda: self.llama())
        self.enviar.clicked.connect(lambda: self.access(self.conversacion2))
        grid = QtGui.QGridLayout()
        grid.addWidget(self.conversacion, 0, 0)
        grid.addWidget(self.conversacion1, 1, 0)
        grid.addWidget(self.conversacion2, 6, 0)
        grid.addWidget(self.llamada, 6,6)
        grid.addWidget(self.enviar, 6, 5)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, CHAT_WIDTH, CHAT_HEIGTH)
        self.setWindowTitle('Chat')
        self.show()

    def access(self, conversacion2=None):#Método que define las acciones a realizar cuando se presiona el botón acceder

        mensaje = conversacion2.text()
        msg = str(self.mipuertofinal)+' dice: '+mensaje
        envia_mensaje = Channel(None, None, self.tupuertofinal)
        envia_mensaje.send_text(msg, self.local)
        self.conversacion1.append(msg)
        
    def llama(self):#Método que define las acciones a realizar cuando se presiona el botón llamar
        print "llamando"
        self.conversacion1.append("Llamando a "+str(self.tupuertofinal))
        envia_audio = Channel(None, None, self.tupuertofinal)
        envia_audio.send_audio(self.local)

    def mostar(self, msg):#Método que escribe en el chat los mensajes recibidos
        print "intentando"
        self.conversacion1.append(msg)

