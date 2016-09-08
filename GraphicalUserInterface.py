#! /usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# PURPOSE:Interfaz grafica de un cliente en PyQt4    #
#                                                    #
# Vilchis Dominguez Miguel Alonso                    #
#       <mvilchis@ciencias.unam.mx>                  #
#                                                    #
# Notes: El alumno tiene que implementar la parte    #
#       comentada como TODO(Instalar python-qt)      #
#                                                    #
# Copyright   16-08-2015                             #
#                                                    #
# Distributed under terms of the MIT license.        #
#################################################### #
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from GUI.login import LoginWindow
from GUI.login import LoginWindowIP
import sys, getopt



# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(argv):
	#Revisa los argumentos con los que es llamado
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
    except getopt.GetoptError:
        print getopt.GetoptError.msg
        sys.exit(2)
    if opts: #Si el usuario mandó alguna bandera
        local = False if '-l' in opts[0] else True
    else: #Si el usuario no mandó ninguna bandera
        local = True
    if(local):#Cuando es local se llama a la interfaz que pide los puertos
        app = QtGui.QApplication(sys.argv)
        mainWindow = LoginWindow()
        sys.exit(app.exec_())
    else:#Cuando no a la que pide las ip's
        app = QtGui.QApplication(sys.argv)
        mainWindow = LoginWindowIP()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv[1:])
