#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:
	def __init__(self, your_port = None, msg = None):
# Create an object to represent our server.
		proxy = xmlrpclib.ServerProxy("http://localhost:"+str(your_port)+"/")
		proxy.sendMessage_wrapper(msg)
		print msg +"mandado al cliente del puerto "+str(your_port)



