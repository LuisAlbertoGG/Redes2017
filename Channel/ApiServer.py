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
#from Constants.AuxiliarFunctions import *
from GUI.login import *

CHUNK = 1024
CHANNELS = 1 
RATE = 44100
DELAY_SECONDS = 5 

frames = []
from cStringIO import StringIO
from numpy.lib import format
def toArray(s):
    f=StringIO(s)
    arr=format.read_array(f)
    return arr 

def reproduce():
        while True:
            if len(frames) > 0:
                cv2.imshow('Servidor',frames.pop(0))
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
        cv2.destroyAllWindows()


class MyApiServer:
    
    def __init__(self, my_port = None):
        self.server = SimpleXMLRPCServer(("localhost", my_port), logRequests=True)
        #allow_none=True)#SimpleXMLRPCRequestHandler)
        playVThread = threading.Thread(target=reproduce)
        playVThread.setDaemon(True)
        playVThread.start()
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

    def stop(self):
        self.server.server_close()

        
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
        #print chat.localhost
        print a
        chat.mostar(a)
        print a
        return "mensaje entregado"

    def sendAudio_wrapper(self, audio):
        #a = str(audio)
        print "me está llegando audio"
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
        #CHUNK = 1024
        #wf = wave.open(audio, 'rb')
        #p = pyaudio.PyAudio()

        # open stream (2)
        #stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
         #       channels=wf.getnchannels(),
          #      rate=wf.getframerate(),
           #     output=True)

            # read data
        #data = wf.readframes(CHUNK)

        # play stream (3)
        #while len(data) > 0:
        #    stream.write(data)
        #    data = wf.readframes(CHUNK)

        # stop stream (4)
        #stream.stop_stream()
        #stream.close()

        # close PyAudio (5)
        #p.terminate()
        return "Audio recibido"





        



