#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:
	def __init__(self, your_port = None, msg = None, text = None):
# Create an object to represent our server.
		if(text):
			self.msg = msg
			url = "http://"+str(your_port)#+"/"
			proxy = xmlrpclib.ServerProxy(url)
			print url
			try:
				print proxy.sendMessage_wrapper(str(msg))
				#print msg +" mandado al cliente del puerto "+str(your_port)
			except Exception as e:
				print e
		else:
			self.msg = msg
			url = "http://"+str(your_port)#+"/"
			proxy = xmlrpclib.ServerProxy(url)
			print url
			try:
				data = xmlrpclib.Binary(msg)
				#print msg +" mandado al cliente del puerto "+str(your_port)
				print proxy.sendAudio_wrapper(data)
			except Exception as e:
				print e