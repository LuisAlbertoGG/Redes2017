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
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
    except getopt.GetoptError:
        print getopt.GetoptError.msg
        sys.exit(2)
    if opts: #Si el usuario mandó alguna bandera
        local = True if '-l' in opts[0] else False
    else:
        local = False
    if(local==False):
        app = QtGui.QApplication(sys.argv)
        mainWindow = LoginWindow()
        sys.exit(app.exec_())
    else:
        app = QtGui.QApplication(sys.argv)
        mainWindow = LoginWindowIP()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv[1:])
