#!/usr/bin/python

from magi.util.agent import DispatchAgent, agentmethod
import subprocess, os

def getAgent():
    return hPing() 

class hPing(DispatchAgent):

	def __init__(self):
		DispatchAgent.__init__(self)
		#nping --udp -p 80 -g 1010 -c 100 --rate 10 --data-length 100 --dest-ip 10.1.2.1 -S 10.1.1.15
		self.mode= 'udp'
		self.source_port = '5629'
		self.destination_port = '80'
		self.experiment_duration = 30
		self.destination_ip = '10.1.2.1'
		self.initial_address = subprocess.check_output("ifconfig | grep 10.1.1 | awk '{print $2}';", shell=True)
		self.initial_address.split(":")[1]
		self.num_flows = 10

		#in Kbits
		self.desired_load = 1000000

		self.source_ips = []
		ip_unit = self.initial_address.split('.')[3].split('\n')[0]

		for i in range(self.num_flows):
			self.source_ips.append('10.1.1.' + ip_unit + str(i))

		self.data_length = 1000
		self.rate = self.desired_load / self.data_length
		self.num_pkts = self.experiment_duration * self.rate

	@agentmethod()
	def startPing(self, msg):

		self.pids = []

		#nping --udp -p 80 -g 1010 -c 100 --rate 10 --data-length 100 --dest-ip 10.1.2.1 -S 10.1.1.15
		for i in range(self.num_flows):
			command = 'nping --' + str(self.mode) + ' -p ' + str(self.source_port) + ' -g ' + str(self.destination_port) \
			+ ' -c ' + str(self.num_pkts) + ' --rate ' + str(self.rate) +  ' --data-length ' + str(self.data_length) \
			+ ' --dest-ip ' + str(self.destination_ip) + ' -S ' + str(self.source_ips[i])
			print "Command: ", command
			self.pids.append(subprocess.Popen(command, shell=True))

		exit_codes = [p.wait() for p in self.pids]
		return True
