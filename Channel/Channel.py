#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import threading
import pyaudio
import time
import heapq
sys.path.insert(0, '../GUI')
from ApiServer import *
from ApiClient import *
from RecordAudio import *

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class Channel(threading.Thread):

 #"""**************************************************
  #  Constructor de la clase
   # @param <str> contact_ip: Si no se trabaja de manera local
    #            representa la ip del contacto con el que se
     #           establecera la conexion
    #@param <int> my_port: De trabajar de manera local puerto
    #            de la instancia del cliente
    #@param <int> contact_port: De trabajar de manera local
    #            representa el puerto de la instancia del contacto
    #**************************************************"""
    def __init__(self, contact_ip = None, my_port = None, contact_port = None):
        if(my_port != None):
            threading.Thread.__init__(self)
            self.miservidor = MyApiServer(my_port)
        else:
            if(contact_ip != None):
                threading.Thread.__init__(self)
                self.miservidor = MyApiServer(5000)
            else:
                self.contact_port = contact_port

     #   """**************************************************
    #Metodo que se encarga de mandar texto al contacto con
    #el cual se estableció la conexion
    #**************************************************"""
    def send_text(self, text, local):
        if(local):
            threading.Thread.__init__(self)
            miMensaje = MyApiClient("localhost:"+str(self.contact_port), text, True)
        else:
            threading.Thread.__init__(self)
            a = str(self.contact_port)+ ":5000"
            miMensaje = MyApiClient(a, text, True)
     #   """**************************************************
    #Metodo que se encarga de llamar al contacto con
    #el cual se estableció la conexion
    #**************************************************"""

    def send_audio(self, local):
        
        if(local):
            threading.Thread.__init__(self)
            graba1 = recordAudio(self.contact_port)
            string = "localhost:"+str(self.contact_port)
            graba1.inicia(True, string)
            
        else:
            threading.Thread.__init__(self)
            graba1 = recordAudio(self.contact_port)
            string = str(self.contact_port)+ ":5000"
            graba1.inicia(False, string)