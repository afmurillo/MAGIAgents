#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess, os
import time


def getAgent():
    return dig() 

class dig(DispatchAgent):

	def __init__(self):
		DispatchAgent.__init__(self)
		
		self.server = '10.1.2.1' 
		self.host = 'www.flowfence.com'
		self.rate = 0.5
		self.n_requests = 30
		self.log_file_name = '/share/magi/modules/MAGIAgents/Agents/digAgent/dig_output_1.txt'

	@agentmethod()
	def startDig(self, msg):
		rate_ms = float(1/self.rate)
		logfile = open(self.log_file_name, "w")
		#dig @10.1.2.1 www.flowfence.com
		for i in range(self.n_requests):
			command = 'dig @' + str(self.server) + ' ' + str(self.host)
			print "Command: ", command
			pid = subprocess.Popen(command, shell=True, stdout=logfile)
			pid.wait()
			time.sleep(rate_ms)
		return True
