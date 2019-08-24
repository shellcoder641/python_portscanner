#A simple port scanner that open a full 3 ways handshake TCP connection to check if the port is open or not.
#It then tries to grab the banner for running services. Currently it "suppose" to query all the ports but...
#ISSUE: when it queries port 22, 3 ways handshake established, then it makes another query on port 22?? and received a RST, 
#then stop all subsequence port scan??? 
#MISSING: doesn't know whether the port is closed or filtered by the firewall.
import socket
import argparse
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#addr_family: AF_INET and AF_INET6: IPv4 and IPv6
#sock_type: SOCK_STREAM, SOCK_DGRAM: TCP and UDP
arg_parser=argparse.ArgumentParser()
arg_parser.add_argument("host",type=str,help="Target hostname")
arg_parser.add_argument("--port",type=int,default=80,help="Target port number")
arg_parser.add_argument("--all,")
args=arg_parser.parse_args()
if args.port>0:
	try:
	    print("wth")
	    s.connect((args.host,args.port))#-->s.connect(("python.org",80))
	    info=s.recv(1024)
	    print("[+] Port %d is open: %s"%(args.port,str(info)))
	    s.close()
	except socket.error as e:
		print("[-] Port %d is closed or filtered."%args.port)
	socket.setdefaulttimeout(1)
else:
	for i in range(0,65536):
		try:
			s.connect((args.host,i))
			print("Trying to initiate a connection to port %d"%i)
			info=s.recv(100)
			s.close()
			print("[+] Port %d is open: %s"%(i,str(info)))
		except socket.error as e:
			print("[-] Port %d is closed or filtered."%args.port)
			continue
		socket.setdefaulttimeout(1)
