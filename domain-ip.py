import concurrent.futures
import requests
import threading
import sys
import time
from colorama import Fore, Style
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
output=open(outputfile, "a")
with open(inputfile, "r") as f:
	inputurl = [line.rstrip() for line in f]
threadLocal = threading.local()
count = len(inputurl)
print("number of subdomains = " + str(count))
def get_session():
    if not hasattr(threadLocal, "session"):
        threadLocal.session = requests.Session()
    return threadLocal.session
def check_sub(url):
	try :
		res=requests.get(url, stream=True)
		ip=res.raw._original_response.fp.raw._sock.getpeername()[0]
		res2=url + " : " + str(ip)
		print(Style.BRIGHT + Fore.WHITE + url[7:-1] + " : " + Fore.CYAN + str(ip))
		output.write(res2[7:-1]+"\n")
	except:
		pass
def itterate_url(inputurl):
	url="http://"+inputurl
	check_sub(url)
if __name__ == "__main__":
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
       		executor.map(itterate_url, inputurl)
	duration = time.time() - start_time
	print("finished in : " + str(duration) + "  sec")
