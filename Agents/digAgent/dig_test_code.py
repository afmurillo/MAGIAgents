import subprocess, os
import time

server = '8.8.8.8' 
host = 'www.google.com'
rate = 20.0
n_requests = 50
rate_ms = float(1.0/rate)
log_file = 'dig_output_1.txt'
#log_file = '/home/andres/Dropbox/Doctorado/Git/MAGIAgents/Agents/digAgent/dig_output_1.txt'

print "Rate: ", rate_ms

test_start_time = time.time()

logfile = open(log_file, "w")

for i in range(n_requests):
	command = 'dig @' + str(server) + ' ' + str(host)
	#print "Command: ", command
	initial_time = time.time()
	pid = subprocess.Popen(command, shell=True, stdout=logfile)
	pid.wait()
	time.sleep(rate_ms)
	finish_time = time.time() - initial_time
	#print "finish time ", finish_time

test_end_time = time.time() - test_start_time
print "Total test time", test_end_time