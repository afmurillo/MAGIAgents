#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess, os

def getAgent():
    return httpPerf()

class httpPerf(DispatchAgent):
	def __init__(self):
		DispatchAgent.__init__(self)
		self.port= 80
		self.numconns = 600
		self.rate = 100
		self.server = 'servernode'
		self.url = 'http://servernode/index.html'
		self.timeout = 7
		self.file = '/share/magi/modules/Agents/httperfAgent/httpPerf2.txt'

	@agentmethod()
	def startPerf(self, msg):
		logfile = open(self.file, "w")
		self.builtcommand = 'httperf --server ' + self.server + ' --port ' + str(self.port) + ' --num-conns ' + str(self.numconns) + ' --rate ' + str(self.rate) + ' --hog ' + '--uri=' + self.url + ' --timeout ' + str(self.timeout)
		#print self.builtcommand
		#print self.file
                self.p = subprocess.Popen(self.builtcommand, shell=True, stdout=logfile)
		#self.returnValue = os.popen(self.builtcommand).read()
		#print self.returnValue

		#logfile.write(self.returnValue)
		
		ret_code = self.p.wait()
		#print 'Codigo retorno ' + str(ret_code)
		#logfile.flush()
		logfile.close()
		return True

