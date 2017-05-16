import matplotlib.pyplot as plt
from networkx import *
import csv

reader = csv.reader(open("S1.csv"), delimiter=",")
ips = []
g = nx.Graph()

aPartirDeQueCantidadMostrarLabels = 35
timesAsking = {"10.10.90.23" : 3,
"10.10.90.91" : 4,
"10.10.91.114" : 8,
"10.10.90.0": 38,
"10.10.12.84" : 2,
"10.10.90.55" : 17,
"10.10.90.40" : 8,
"0.0.0.0" : 36,
"10.10.91.75" : 9,
"10.10.91.183" : 44,
"10.10.90.19" : 40,
"10.10.91.132" : 2,
"10.10.90.15" : 33,
"10.10.91.56" : 26,
"10.10.90.80" : 1,
"10.10.88.1": 430,
"10.10.91.23" : 1,
"10.10.90.114" : 47}

labels = dict()
for key in timesAsking.keys():
	if(timesAsking[key] >= aPartirDeQueCantidadMostrarLabels):
		labels[key] = key

for ipFrom, ipSearchingFor in reader:
	g.add_edge(ipFrom,ipSearchingFor)

nodeSizesAsking = dict()
nodeSizesBeingSearch = dict()
d = nx.degree(g)
for ip in d.keys():
	if not ip in nodeSizesAsking:
		try:
			nodeSizesAsking[ip] = timesAsking[ip]
		except:
			nodeSizesAsking[ip] = 0
	if not ip in nodeSizesBeingSearch:
		try:
			nodeSizesBeingSearch[ip] = timesBeingSearch[ip]
		except:
			nodeSizesBeingSearch[ip] = 0


edgeList = ips
# g.add_edges_from(edgeList)
oldMaxAsking = max(nodeSizesAsking.values())
oldMaxBeingSearch = max(nodeSizesBeingSearch.values())
newMax = 2000
for key in nodeSizesAsking.keys():
	nodeSizesAsking[key] = (nodeSizesAsking[key] * newMax) / oldMaxAsking
	nodeSizesBeingSearch[key] = (nodeSizesBeingSearch[key] * newMax) / oldMaxBeingSearch

pos = nx.spring_layout(g,scale=1) #default to scale=1
nx.draw(g,pos, labels = labels,node_color = "#97edea",with_labels=True,edge_color="grey",width=0.5,node_size=[v for v in nodeSizesAsking.values()])
plt.show()
# nx.draw(g,pos, with_labels=True,node_size=[v for v in nodeSizesBeingSearch.values()])
# plt.show()
 
