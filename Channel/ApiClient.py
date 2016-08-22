#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:
	def __init__(self, your_port = None, msg = None):
# Create an object to represent our server.
		self.msg = msg
		url = "http://"+str(your_port)+":5000"#+"/"
		proxy = xmlrpclib.ServerProxy(url)
		print url
		try:
			print proxy.sendMessage_wrapper(str(msg))
			#print msg +" mandado al cliente del puerto "+str(your_port)
		except Exception as e:
			print e
			print url



