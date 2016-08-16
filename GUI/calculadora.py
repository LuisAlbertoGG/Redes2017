# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
 
class calculadora(QtGui.QWidget):
    def __init__(self, parent=None):
	QtGui.QWidget.__init__(self, parent)
	self.setWindowTitle("Calculadora")
	self.resize(119, 145)
	self.temp=""
	self.igual = QtGui.QPushButton("=",self)
        self.igual.setGeometry(90, 120, 31, 24)
	self.multiplica = QtGui.QPushButton("*",self)
	self.multiplica.setGeometry(0, 120, 31, 24)
        self.connect(self.multiplica,QtCore.SIGNAL("clicked()"),self.multiplicar)
	self.clean = QtGui.QPushButton("AC",self)
	self.clean.setGeometry(30, 120, 31, 24)
        self.connect(self.clean,QtCore.SIGNAL("clicked()"),self.clear)
	self.divide = QtGui.QPushButton("/",self)
        self.connect(self.divide,QtCore.SIGNAL("clicked()"),self.dividir)
        self.divide.setGeometry(0, 90, 31, 24)
        self.connect(self.igual,QtCore.SIGNAL("clicked()"),self.resultado)
	self.resta = QtGui.QPushButton("-",self)
        self.resta.setGeometry(0, 60, 31, 24)
        self.connect(self.resta,QtCore.SIGNAL("clicked()"),self.restar)
	self.suma = QtGui.QPushButton("+",self)
	self.suma.setGeometry(0, 30, 31, 24)
        self.connect(self.suma,QtCore.SIGNAL("clicked()"),self.sumar)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 121, 25))
        self.uno = QtGui.QPushButton("1",self)
        self.connect(self.uno,QtCore.SIGNAL("clicked()"),self.inu)
        self.uno.setGeometry(QtCore.QRect(30, 30, 31, 24))
        self.dos = QtGui.QPushButton("2",self)
        self.connect(self.dos,QtCore.SIGNAL("clicked()"),self.ind)
        self.dos.setGeometry(QtCore.QRect(60, 30, 31, 24))
        self.tres = QtGui.QPushButton("3",self)
        self.connect(self.tres,QtCore.SIGNAL("clicked()"),self.intr)
        self.tres.setGeometry(QtCore.QRect(90, 30, 31, 24))
        self.cuatro = QtGui.QPushButton("4",self)
        self.connect(self.cuatro,QtCore.SIGNAL("clicked()"),self.inc)
        self.cuatro.setGeometry(QtCore.QRect(30, 60, 31, 24))
        self.cinco = QtGui.QPushButton("5",self)
        self.connect(self.cinco,QtCore.SIGNAL("clicked()"),self.inci)
        self.cinco.setGeometry(QtCore.QRect(60, 60, 31, 24))
        self.seis = QtGui.QPushButton("6",self)
        self.connect(self.seis,QtCore.SIGNAL("clicked()"),self.ins)
        self.seis.setGeometry(QtCore.QRect(90, 60, 31, 24))
        self.nueve = QtGui.QPushButton("9",self)
        self.connect(self.nueve,QtCore.SIGNAL("clicked()"),self.inn)
        self.nueve.setGeometry(QtCore.QRect(90, 90, 31, 24))
        self.ocho = QtGui.QPushButton("8",self)
        self.connect(self.ocho,QtCore.SIGNAL("clicked()"),self.ino)
        self.ocho.setGeometry(QtCore.QRect(60, 90, 31, 24))
        self.siete = QtGui.QPushButton("7",self)
        self.connect(self.siete,QtCore.SIGNAL("clicked()"),self.insi)
        self.siete.setGeometry(QtCore.QRect(30, 90, 31, 24))
        self.cero = QtGui.QPushButton("0",self)
        self.cero.setGeometry(QtCore.QRect(60, 120, 31, 24))
        self.connect(self.cero,QtCore.SIGNAL("clicked()"),self.ince)
    def clear(self):
      self.temp=""
      self.lineEdit.setText("")
    def restar(self):
      self.temp+="-"
      self.lineEdit.setText(self.temp)
    def dividir(self):
      self.temp+="/"
      self.lineEdit.setText(self.temp)
    def multiplicar(self):
      self.temp+="*"
      self.lineEdit.setText(self.temp)
    def sumar(self):
	self.temp+="+"
	self.lineEdit.setText(self.temp)
 
    def resultado(self):
	if len(self.temp)>0:
	  final=eval(self.temp)
	  self.lineEdit.setText(str(final))
	  self.temp=str(final)
	else:
	  final=eval(str(self.lineEdit.text()))
	  print final
	  self.lineEdit.setText(str(final))
	  self.temp=str(final)
    def inu(self):
	self.temp+="1"
	self.lineEdit.setText(self.temp)
    def ind(self):
	self.temp+="2"
	self.lineEdit.setText(self.temp)
    def intr(self):
	self.temp+="3"
	self.lineEdit.setText(self.temp)
    def inc(self):
	self.temp+="4"
	self.lineEdit.setText(self.temp)
 
    def inci(self):
	self.temp+="5"
	self.lineEdit.setText(self.temp)
 
    def ins(self):
	self.temp+="6"
	self.lineEdit.setText(self.temp)
 
    def insi(self):
	self.temp+="7"
	self.lineEdit.setText(self.temp)
 
    def ino(self):
	self.temp+="8"
	self.lineEdit.setText(self.temp)
 
    def inn(self):
	self.temp+="9"
	self.lineEdit.setText(self.temp)
 
    def ince(self):
	self.temp+="0"
	self.lineEdit.setText(self.temp)
 
calc=QtGui.QApplication(sys.argv)
dialogo=calculadora()
dialogo.show()
calc.exec_()
