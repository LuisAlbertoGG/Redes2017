#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class MyApiServer:
    def __init__(self, my_port = None):
        server = SimpleXMLRPCServer(("localhost", my_port), requestHandler=RequestHandler)
        server.register_introspection_functions();
        
class FunctionWrapper:
    def __init__(self):
        #TODO

     """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        



