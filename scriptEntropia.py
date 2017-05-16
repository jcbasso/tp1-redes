#! /usr/bin/env python
from scapy.all import *
import signal
import sys
import argparse
import csv
import math

reader = csv.reader(open("S1.entropia"), delimiter=",")
totalQuantity = 0
simbolsQuantity = 0
for ip,quantity in reader:
	totalQuantity += int(quantity)
	simbolsQuantity += 1

reader = csv.reader(open("S1.entropia"), delimiter=",")

entropia = 0
for ip,quantity in reader:
	quantity = int(quantity)
	probability = (float(quantity)/totalQuantity)
	information = -math.log(probability,2)
	entropia += probability*information

entropiaMax = math.log(simbolsQuantity,2)
print "Entropia de la red: " + str(entropia)
print "Entropia max de la red: " + str(entropiaMax)