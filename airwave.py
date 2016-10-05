import netmiko
import getpass

#testing git

usrname = raw_input("Username: ")
pswd = getpass.getpass('Password:')

FileIn = open('vc_ip.txt', 'r')
FileOut = open('results_ap.txt','w')
device = FileIn.readline().strip()

while (device != ""):
	
	aruba_ap = {
	'device_type': 'cisco_ios',
	'ip':   device,
	'username': usrname,          
	'password': pswd,
	'secret': pswd,
	}

	SSHClass = netmiko.ssh_dispatcher(aruba_ap['device_type'])
	try:
		net_connect = SSHClass(**aruba_ap)
		output = net_connect.send_command("commit apply")
		if 'denied' in output:
			net_connect.disconnect()
			device = FileIn.readline().strip()
			continue
			
		print "NotMgmt " + device
		results = device + ',NotInMgmt' + '\n'
		FileOut.write(results)
	except:
		print "Issues with " + device
		results = device + ',Issues' + '\n'
		FileOut.write(results)
	
	device = FileIn.readline().strip()

FileIn.close()
FileOut.close()