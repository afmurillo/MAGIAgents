#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess, os, time, sys
#import getopt

def getAgent():
    return PacketCounter()

class PacketCounter(DispatchAgent):
	def __init__(self):
		DispatchAgent.__init__(self)
		print "initializing"
		self.delay = 1
		self.totalTime = 10
		self.interface = 'eth0'
		self.direction = 'TX'
		self.aFile = '/home/out.txt'

	@agentmethod()
	def startCount(self, msg):
	        self.dump = open(self.aFile,'w')

	        for i in range(int(self.totalTime/self.delay)):
		    	self.initialRxPackets = int(os.popen("ifconfig %s | grep '%s packets' | awk '{print $2}' | awk -F: '{print $2}'" % (self.interface, self.direction)).read())
			time.sleep(self.delay)
			self.rxPackets = int(os.popen("ifconfig %s | grep '%s packets' | awk '{print $2}' | awk -F: '{print $2}'" % (self.interface, self.direction) ).read() )
			#print "%.5f\t%u" % (time.time(), rxPackets - initialRxPackets)
			self.pkts=self.rxPackets - self.initialRxPackets
			self.dump.write(str(self.pkts)+'\n')
		self.dump.close()
		return True
