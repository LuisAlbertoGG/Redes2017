#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:
# Create an object to represent our server.
	server_url = 'http://baba';
	server = xmlrpclib.Server(server_url);

# Call the server and get our result.
	result = server.sample.sumAndDifference(5, 3)
	print "Sum:", result['sum']
	print "Difference:", result['difference']
