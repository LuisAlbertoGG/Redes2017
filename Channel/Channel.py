#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import threading
#import SocketServer
sys.path.insert(0, '../GUI')
#from Gui.chat import Chat
from ApiServer import *
from ApiClient import *

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
                #threading.Thread.__init__(self)
                #miMensaje = MyApiClient(self.contact_port)
                self.contact_port = contact_port

    #def run(self):
    #    self.miservidor.serve_forever()




        #TODO

     #   """**************************************************
    #Metodo que se encarga de mandar texto al contacto con
    #el cual se estableció la conexion
    #**************************************************"""
    def send_text(self, text):
        threading.Thread.__init__(self)
        miMensaje = MyApiClient(self.contact_port, text)
        #Chat.self.conversacion1.append(self.mipuertofinal+' dice: '+mensaje)
        #TODO

