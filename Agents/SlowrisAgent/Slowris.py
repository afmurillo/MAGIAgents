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
    return Slowris()

''' The FileCreator agent implementation, derived from DispatchAgent.'''
class Slowris(DispatchAgent):
	def __init__(self):
		DispatchAgent.__init__(self)
		self.host = 'servernode'
		self.port = 80
		self.timeout = 2000
		self.num = 500
		self.tcptimeout=5
		

	@agentmethod()
	def startSlowris(self, msg):
		self.builtcommand = './slowloris.pl -dns servernode -port 80 -timeout 2000 -num 500 -tcpto 5'
		self.p = subprocess.Popen(self.builtcommand, shell=True)			
		return True

	@agentmethod()
	def stopSlowris(self, msg):
		pid = self.p.pid+1
		theEnd = subprocess.Popen('kill -9 ' + str(pid), shell=True) 		
		return True
