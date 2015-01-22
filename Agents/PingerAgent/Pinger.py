#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import os, subprocess
import time

''' the getAgent() method must be defined somewhere for all agents.
The Magi daemon invokes this method to get a reference to an
agent. It uses this reference to run and interact with an agent
instance. (The getAgent() call is generally the same for all agent
implementations: it just returns an instance of the agent.)'''

def getAgent():
    return Pinger()

''' The FileCreator agent implementation, derived from DispatchAgent.'''
class Pinger(DispatchAgent):
	def __init__(self):
		DispatchAgent.__init__(self)
		self.interval = 1
		self.address = '10.1.1.8'

	@agentmethod()
	def startPing(self,msg):
		self.builtcommand = 'ping -i ' + str(self.interval) + ' '  + self.address
		self.p = subprocess.Popen(self.builtcommand, shell=True)
		return True

	@agentmethod()
	def stopPing(self,msg):
		pid = self.p.pid+1
		theEnd = subprocess.Popen('kill -9 ' + str(pid), shell=True) 		
		os._exit(1)
		return True
