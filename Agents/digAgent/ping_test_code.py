import subprocess, os

mode= 'udp'
source_port = '5629'
destination_port = '80'
experiment_duration = 30
destionation_ip = '8.8.8.8'
initial_address = subprocess.check_output("ifconfig | grep 192 | awk '{print $2}';", shell=True)
print "Aba: ", initial_address
initial_address.split(":")[1]
print "Initial address: " + str(initial_address)
num_flows = 10

#in Kbits
desired_load = 1000

source_ips = []
ip_unit = initial_address.split('.')[3].split('\n')[0]
print "IP unit: " + ip_unit


for i in range(num_flows):
	source_ips.append('192.168.0.' + ip_unit + str(i))
	print "ip unit: ", ip_unit
	print "i: ", i

print "Sources IPs to be used: ", source_ips

data_length = 1000
rate = desired_load / data_length
num_pkts = experiment_duration * rate

pids = []

#nping --udp -p 80 -g 1010 -c 100 --rate 10 --data-length 100 --dest-ip 10.1.2.1 -S 10.1.1.15
for i in range(num_flows):
	command = 'nping --' + str(mode) + ' -p ' + str(source_port) + ' -g ' + str(destination_port) \
	+ ' -c ' + str(num_pkts) + ' --rate ' + str(rate) +  ' --data-length ' + str(data_length) \
	+ ' --dest-ip ' + str(destionation_ip) + ' -S ' + str(source_ips[i])
	print "Comand: ", command
	pids.append(subprocess.Popen(command, shell=True))

exit_codes = [p.wait() for p in pids]
