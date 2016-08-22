#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class MyApiServer:
    def __init__(self, my_port = None):
        self.server = SimpleXMLRPCServer(("localhost", my_port), SimpleXMLRPCRequestHandler)
        print "escuchando en el puerto "+ str(my_port)
        self.server.register_introspection_functions();
        self.server.register_instance(FunctionWrapper())
#        server.serve_forever()

    def run(self):
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
        print "ya"





        



