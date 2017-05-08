#! /usr/bin/env python
from scapy.all import *
import signal
import sys
import argparse

broadcast = 0
unicast = 0
macAddressDstDic = dict()

# Handler para cuando mandas sigint muestre #broadcast y #unicode
def Shandler(signal, frame):
	global broadcast,unicast
	print "\n\n\n\n--------------------------------- "    
	print "#S[broadcast] = " + str(broadcast)
	print "#S[unicast] = " + str(unicast)
	print 
	print "#S = " + str(broadcast+unicast)
	sys.exit(0)

def Scallback(pkt):
	# IMPRIME: si es un broadcast o unicast
	global broadcast,unicast
	if ( str(pkt[Ether].dst) == "ff:ff:ff:ff:ff:ff"):
		broadcast = broadcast + 1
		print "S[broadcast] : " + str(broadcast) 
	else:
		unicast = unicast + 1
		print "S[unicast] : " + str(unicast)

	# IMPRIME: ip.src,ip.dst,ethernet.src,ethernet.dst
	# try:
	# 	print "IP: " + str(pkt[IP].src) + " -> " + str(pkt[IP].dst)
	# except:
	# 	print "IP: No ip found"
	#
	# try:
	# 	print "Ethernet: " + str(pkt[Ether].src) + " -> " + str(pkt[Ether].dst)
	# except:
	# 	print "Ethernet: No ethernet found"
	# print
	
	# IMPRIME: Todo
	#print pkt.show()

def S1handler(signal, frame):
	global macAddressDstDic
	print "\n\n\n\n--------------------------------- "    
	for macAddressDst in macAddressDstDic:
		print str(macAddressDst) + " :"
		print "   #Veces: " + str(macAddressDstDic[macAddressDst])
		print 
	sys.exit(0)

def S1callback(pkt):
	global macAddressDstDic
	macAddressDst = pkt[Ether].dst
	if macAddressDst in macAddressDstDic:
		macAddressDstDic[macAddressDst] += 1
	else:
		macAddressDstDic[macAddressDst] = 1
	print str(macAddressDst) + " : " + str(macAddressDstDic[macAddressDst])

def S(interfaz = "en1"):
	signal.signal(signal.SIGINT, Shandler)
	print "S[type] : #Veces"
	sniff(iface=interfaz, prn=Scallback)
	signal.pause()

def S1(interfaz = "en1"):
	signal.signal(signal.SIGINT, S1handler)
	print "MacAdress destino : #Veces"
	sniff(iface=interfaz, prn=S1callback, filter="arp")
	signal.pause()

parser = argparse.ArgumentParser(description='Sniff packages')

parser.add_argument('interface', default='en1', nargs='?', help='interface of your network')
parser.add_argument('--S1', dest='sniffAlgorithm', const=S1, default=S, nargs='?', help='run S1 or S (default = S)')

args = parser.parse_args()

args.sniffAlgorithm(args.interface)