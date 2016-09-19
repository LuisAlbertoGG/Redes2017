import sys
import numpy as np
import cv2
import time
from cStringIO import StringIO
import threading
import pyaudio
import numpy
import multiprocessing as mp
import time
import heapq
sys.path.insert(0, '../Constants')
from Constants.Constants import *
from ApiServer import *
from ApiClient import *
from numpy.lib import format


cap = cv2.VideoCapture(0)
#proxy = xmlrpclib.ServerProxy("http://localhost:9080/",allow_none = False)
class recordVideo():

	def __init__(self, contact_port = None):
		self.cola = []
	 	self.contact_port = contact_port

	def inicia(self, local, string):#Inicia la grabacion de video
		if(local):#Si es local
			queue = mp.Queue()
			p = mp.Process(target=self.encolarVideo, args=(queue, string,))#Se llama al metodo encolarVideo
			p.start()
			#while True:
			#	d = queue.get()	
			#	miMensaje = MyApiClient(string, d, False)#Se crea el hilo
				
		else:#Si no lo es
			queue = mp.Queue()
			p = mp.Process(target=self.encolarVideo, args=(queue, string,))#Se llama al metodo encolarVideo
			p.start()
			#while True:
			#	d = queue.get()	
			#	miMensaje = MyApiClient(string, d, False)#Se crea el hilo


	def toString(data):
	    f= StringIO()
	    format.write_array(f,data)
	    return f.getvalue()

	def encolarVideo(q, string):
	    while(True):
	        ret, frame = cap.read()
	        cv2.imshow('Cliente',frame) 
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	        data = toString(frame)
	        miVideo = MyApiClient(string, data, "video")
	        #proxy.playVideo(data) 
	    cap.release()
	    cv2.destroyAllWindows()