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

	def encolarAudio(self, q):
		CHUNK = 1024
		CHANNELS = 1
		RATE = 44100
		RECORD_SECONDS = 2
		p = pyaudio.PyAudio()
		FORMAT = p.get_format_from_width(2)
		#def callback(in_data, frame_count, time_info, status):
		#	return (in_data, pyaudio.paContinue)
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
			#heappush(q, data_ar)

	def inicia(self, local, string):
		if(local):
			queue = mp.Queue()
			p = mp.Process(target=self.encolarAudio, args=(queue,))
			p.start()
			while True:
				d = queue.get()	
				miMensaje = MyApiClient(string, d, False)
				
			#d = heappop(queue)
		else:
			queue = mp.Queue()
			p = mp.Process(target=self.encolarAudio, args=(queue,))
			p.start()
			while True:
				d = queue.get()	
				miMensaje = MyApiClient(string, d, False)
				
		
		#stream = p.open(format=p.get_format_from_width(WIDTH),
         #   channels=CHANNELS,
          #  rate=RATE,
           # input=True,
            #output=False,
            #stream_callback=callback)

		
		#stream.start_stream()
		
		#while stream.is_active():
#
#			miMensaje = MyApiClient("localhost:"+str(self.contact_port), stream, False)
#			print "estoy escuchando"
#			time.sleep(0.1)
#
#		stream.stop_stream()
#		stream.close()
#		p.terminate()
