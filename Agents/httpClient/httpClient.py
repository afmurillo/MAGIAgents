#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess, os
import time


def getAgent():
    return httpClient() 

class httpClient(DispatchAgent):

	def __init__(self):
		DispatchAgent.__init__(self)
		
		#self.server = '10.1.2.1' 
		self.url = 'http://10.1.2.1/file.html'
		self.rate = 10.0
		self.n_requests = 30
		self.log_file_name = 'http_output_1.txt'
		self.limit_rate = '1m'

	@agentmethod()
	def startHttp(self, msg):
		rate_ms = float(1/self.rate)
		logfile = open(self.log_file_name, "w")
		#dig @10.1.2.1 www.flowfence.com
		for i in range(self.n_requests):
			command = 'wget -q0 --no-cache --limit-rate=' + str(self.limit_rate) + ' ' + str(self.url) ' > /dev/null'
			print "Command: ", command
			pid = subprocess.Popen(command, shell=True, stdout=logfile)
			pid.wait()
			time.sleep(rate_ms)
		return True
