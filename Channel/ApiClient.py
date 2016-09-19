#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:#Clase que crea una petición y envía un mensaje o audio
	def __init__(self, your_port = None, msg = None, text = None):
		if(text == "texto"):#Si lo que se manda es texto
			self.msg = msg
			url = "http://"+str(your_port)#A donde se va a mandar
			proxy = xmlrpclib.ServerProxy(url)#El proxy
			print url
			try:
				print proxy.sendMessage_wrapper(str(msg))#Se manda el mensaje
			except Exception as e:
				print e
		else:
			if(text == "audio"):#Si lo que se manda es audio
				self.msg = msg
				url = "http://"+str(your_port)#A donde se manda
				proxy = xmlrpclib.ServerProxy(url)#El proxy
				print url
				try:
					data = xmlrpclib.Binary(msg)
					print proxy.sendAudio_wrapper(data)#Se manda el audio
				except Exception as e:
					print e
			else:
				self.msg = msg
				url = "http://"+str(your_port)#A donde se manda
				proxy = xmlrpclib.ServerProxy(url)#El proxy
				print url
				try:
					data = xmlrpclib.Binary(msg)
					print proxy.sendVideo_wrapper(data)#Se manda el video
				except Exception as e:
					print e