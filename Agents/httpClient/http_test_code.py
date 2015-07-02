import subprocess, os
import time

#server = '10.1.2.1' 
url = 'http://www.semana.com/deportes/articulo/wilmar-roldan-pitara-la-final-entre-chile-argentina/433316-3'
rate = 10.0
n_requests = 30
log_file_name = 'http_output_1.txt'
limit_rate = '1m'

test_start_time = time.time()

log_file = open(log_file_name, "w")
rate_ms = float(1/rate)

for i in range(n_requests):

	command = 'wget -q0 --no-cache --limit-rate=' + str(limit_rate) + ' ' + str(url)
	#print "Command: ", command
	initial_time = time.time()
	pid = subprocess.Popen(command, shell=True, stdout=log_file)
	pid.wait()
	time.sleep(rate_ms)
	finish_time = time.time() - initial_time
	#print "finish time ", finish_time

test_end_time = time.time() - test_start_time
print "Total test time", test_end_time