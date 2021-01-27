import re
import subprocess

#belove variable runs subprocess to get saved wifi devices!
sp = subprocess.run(['netsh','wlan','show','profile'], shell=True,capture_output=True, text=True ).stdout









#getting devices name and storing in list!
networks_name = re.findall('All User Profile     : (.*)',sp)






found_devs = list() 
for item in networks_name:
	profile = subprocess.run(['netsh','wlan','show','profile', item], shell=True,capture_output=True,text=True).stdout

	if re.findall('Security key           : Absent',profile):
		continue

	else:
		network = subprocess.run(['netsh','wlan','show','profile',item,'key=clear'],shell=True,capture_output=True,text=True).stdout
		pass_word = re.findall(' Key Content            :(.*)',network)
		wifi_dev = dict(ussid=item, passcode=pass_word[0].strip())
		found_devs.append(wifi_dev)

for i in found_devs:
	print(i)

