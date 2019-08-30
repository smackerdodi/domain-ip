import socket
import sys 
import colorama
import time
from colorama import Fore, Style
from requests.exceptions import ConnectionError
print(Style.BRIGHT + Fore.CYAN + '''/

                          _                _           _ _ 
 ___ _ __ ___   __ _  ___| | _____ _ __ __| | ___   __| (_)
/ __| '_ ` _ \ / _` |/ __| |/ / _ \ '__/ _` |/ _ \ / _` | |
\__ \ | | | | | (_| | (__|   <  __/ | | (_| | (_) | (_| | |
|___/_| |_| |_|\__,_|\___|_|\_\___|_|  \__,_|\___/ \__,_|_|

''')
print(Fore.YELLOW + '''/              CODED BY : DAOUD YOUSSEF          


''')                                              
print (Style.BRIGHT + Fore.YELLOW + 'PREPARING FOR GETTING IPs')
for i in range(5,0,-1):
    time.sleep(1)
    print(str(i) + i * " . ") 
inputfile=sys.argv[1]
outputfile=sys.argv[2]
subfile=open(inputfile, "r")
output=open(outputfile, "a")
count = len(open(inputfile).readlines(  ))
print('''

''')
print(Style.BRIGHT + Fore.WHITE + " the number of subdomain in input file is : " + Fore.YELLOW + str(count))
print('''

''')
def getip(subd):
	try:
		req=socket.gethostbyname(subd)
		socket.setdefaulttimeout(1)
		res=subd + " : " + "(" + req + ")"
		output.write(res+"\n")
		print(Style.BRIGHT + Fore.WHITE + subd + Fore.RED + " : " + Fore.CYAN+ "(" + req + ")")
	except socket.gaierror as err:
		time.sleep(0.01)
		pass
for sub in subfile:
	if not sub.strip():
		pass
	else:
		subd=sub.strip()
		if subd[0] == "*" or subd[0] == ".":
			pass
		else:
			getip(subd)	
