import sys
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

class recordAudio():
	
	def __init__(self, contact_port = None):
		self.cola = []
	 	self.contact_port = contact_port

	def encolarAudio(self, q):#Metodo que encola el audio en el queue
		p = pyaudio.PyAudio()
		FORMAT = p.get_format_from_width(2)
		stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
		while True:
			frame = []
			for i in range(0,int(RATE/CHUNK *RECORD_SECONDS)):
				frame.append(stream.read(CHUNK))
			data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
			q.put(data_ar)

	def inicia(self, local, string):#Método que inicia la grabación de audio
		if(local):#Si es local
			queue = mp.Queue()
			p = mp.Process(target=self.encolarAudio, args=(queue,))#Se llama al método encolarAudio
			p.start()
			while True:
				d = queue.get()	
				miMensaje = MyApiClient(string, d, False)#Se crea el hilo
				
		else:#Si no lo es
			queue = mp.Queue()
			p = mp.Process(target=self.encolarAudio, args=(queue,))#Se llama al método encolarAudio
			p.start()
			while True:
				d = queue.get()	
				miMensaje = MyApiClient(string, d, False)#Se crea el hilo