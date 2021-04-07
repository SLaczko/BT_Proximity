import nmap
import json

PHONE_IP = "192.168.1.12"

def runW():

	nm = nmap.PortScanner()

	output_json = nm.scan('192.168.1.12/24', arguments='-sn')
	if PHONE_IP in output_json['scan']:
		print("Found you!")
	else:
		print("You're gone...")
