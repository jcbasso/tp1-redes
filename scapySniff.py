#! /usr/bin/env python
from scapy.all import *
import signal
import sys
import argparse
from collections import namedtuple

broadcast = 0
unicast = 0
macAddressDic = dict()

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
		print "S[broadcast]"
		broadcast = broadcast + 1
	else:
		print "S[unicast]"
		unicast = unicast + 1
	
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
	global macAddressDic
	for macAddress in macAddressDic:
	    print str(macAddress.value[Ether].dst) + " :"
	    print "   #Veces: " + macAddress.count
	    print "   Body: " + macAddress.body

def S1callback(pkt):
	global macAddressDic
	MAC = namedtuple('MAC', 'count body')
	macAddress = pkt[Ether].dst
	if macAddress in macAddressDic:
		macAddressDic[macAddress].count = macAddressDic[macAddress].count + 1
	else:
		macAddressDic[macAddress] = MAC(1,pkt)

def S(interfaz = "en1"):
	signal.signal(signal.SIGINT, Shandler)
	sniff(iface=interfaz, prn=Scallback)
	signal.pause()

def S1(interfaz = "en1"):
	signal.signal(signal.SIGINT, S1handler)
	sniff(iface=interfaz, prn=S1callback, filter="arp")
	signal.pause()

parser = argparse.ArgumentParser(description='Sniff packages')

parser.add_argument('interface', help='interface of your network')
parser.add_argument('--S1', dest='filter', const=S1, default=S, nargs='?', help='run S1 or S (default = S)')
args = parser.parse_args()

args.filter(args.interface)