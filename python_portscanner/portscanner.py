import socket
import argparse
def scanner():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#addr_family: AF_INET and AF_INET6: IPv4 and IPv6
	#sock_type: SOCK_STREAM, SOCK_DGRAM: TCP and UDP
	arg_parser=argparse.ArgumentParser()
	arg_parser.add_argument("host",type=str,help="Target hostname")
	group=arg_parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--port",type=int,help="Target port number")
	group.add_argument("--all",help="Scan all ports",nargs='?', const=3)#can have 0 arguments, const 3 is for bookkeeping
	group.add_argument("--range",type=int,nargs=2,help="A range of ports")#nargs=number of args
	args=arg_parser.parse_args()
	if args.port:#scan a specific port
	    print("Scanning one specific port")
	    res=s.connect_ex((args.host,args.port))#-->s.connect(("python.org",80))
	    print("Trying to initiate a connection to port %d"%args.port)
	    if res==0:
	    	# info=s.recv(1024)#this line has been commented out because we don't know when the client will send the data
	    	# we are trying to grab the banner but don't know whether the service actually send the banner or not
	    	# print("[+] Port %d is open: %s"%(args.port,str(info)))
	    	print("[+] Port %d is open."%args.port)
	    else:
	    	print("[-] Port %d is closed or filtered."%args.port)
	    s.close()
	elif args.all:#scan all ports
		print("Scanning all ports")
		for i in range(0,65536):
			res=s.connect_ex((args.host,i))
			print("Trying to initiate a connection to port %d"%i)
			if res==0:
				print("[+] Port %d is open."%i)
			else:
				print("[-] Port %d is closed or filtered."%i)
		s.close()
	elif args.range:
		print("Scanning a range of ports")
		for i in range(args.range[0],args.range[1]):
			res=s.connect_ex((args.host,i))
			print("Trying to initiate a connection to port %d"%i)
			if res==0:
				print("[+] Port %d is open."%i)
			else:
				print("[-] Port %d is closed or filtered."%i)
		s.close()

def main():
	scanner()
if __name__=="__main__":
	main()