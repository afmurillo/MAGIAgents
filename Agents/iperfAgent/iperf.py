#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess

def getAgent():
    return iperf() 

class iperf(DispatchAgent):
	def __init__(self):
		DispatchAgent.__init__(self)
		self.connect= '10.1.2.2'

		# Only used in UDP mode
		self.bw = '20m'
		self.format = 'm'
		self.duration_time = '60'
		self.report_time = '1'
		self.mode = 'TCP'
		self.logfile = 'reply_time_1.txt'

	@agentmethod()
	def startPerf(self, msg):
		#logfile = open(self.file, "w")
		if self.mode == 'TCP':
			self.builtcommand = 'iperf -c ' + self.connect + ' -f ' + self.format + ' -t ' + str(self.duration_time) + ' -i ' + str(self.report_time)
		elif self.mode == 'UDP':
			self.builtcommand = 'iperf -c ' + self.connect + ' -f ' + self.format + ' -t ' + str(self.duration_time) + ' -i ' + str(self.report_time) + ' -b ' + self.bw

		else:
			print "Invalid mode!"
			return False

		with open(self.logfile,"w+") as f:
		        self.p = subprocess.Popen(self.builtcommand, shell=True, stdout=f)		
			ret_code = self.p.wait()
		return True

