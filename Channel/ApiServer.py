#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '../Constatns')
sys.path.insert(1, '../GUI')
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
#from Constants.AuxiliarFunctions import *
from GUI.login import *



class MyApiServer:
    
    def __init__(self, my_port = None):
        self.server = SimpleXMLRPCServer(("localhost", my_port), logRequests=True) #allow_none=True)#SimpleXMLRPCRequestHandler)
        #self.server.register_instance(ServerTrial()) 
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()
        print "escuchando en el puerto "+ str(my_port)
        #self.server.register_introspection_functions();
        self.server.register_instance(FunctionWrapper())
        #self.run()
#        server.serve_forever()

    def run(self):
        #print "hice que corriera por siempre :D"
        self.server.serve_forever()
        
class FunctionWrapper:
    def __init__(self):
        #TODO

     """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        a = str(message)
        global chat
        print chat.local
        print a
        chat.mostar(a)
        print a
        return "mensaje entregado"






        



