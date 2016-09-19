#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pyaudio
import cv2 
import numpy as np
import numpy 
sys.path.insert(1, '../Constatns')
sys.path.insert(1, '../GUI')
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
from GUI.login import *


class MyApiServer:#Método que crea el servidor
    
    def __init__(self, my_port = None):
        self.server = SimpleXMLRPCServer(("localhost", my_port), logRequests=True)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()
        print "escuchando en el puerto "+ str(my_port)
        self.server.register_instance(FunctionWrapper())#Registra todas las funciones que se encuentran en la clase FunctionWrapper

    def run(self):
        self.server.serve_forever()

    def stop(self):
        self.server.server_close()

frames = []
reproduciendo = False
from cStringIO import StringIO
from numpy.lib import format
def toArray(s):
    f=StringIO(s)
    arr=format.read_array(f)
    return arr 

        
class FunctionWrapper:
    def __init__(self):
     """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        a = str(message)
        global chat
        print a
        chat.mostar(a)
        print a
        return "mensaje entregado"

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, recibe el audio y lo 
    reproduce
    ************************************************** """
    def sendAudio_wrapper(self, audio):
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()
        return "Audio recibido"

    def sendVideo_wrapper(video):
        frames.append(toArray(video.data))
        return "Video recibido"
        if(reproduciendo == False):
            playVThread = threading.Thread(target=reproduce)
            playVThread.setDaemon(True)
            playVThread.start()
            reproduciendo = True
        


    def reproduce():
        while True:
            if len(frames) > 0:
                cv2.imshow('Servidor',frames.pop(0))
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
        cv2.destroyAllWindows()





        



