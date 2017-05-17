import matplotlib.pyplot as plt
from networkx import *
import csv

reader = csv.reader(open("Datos Shopping/S1-shopping.csv"), delimiter=",")
ips = []
g = nx.Graph()

aPartirDeQueCantidadMostrarLabels = 35
timesAsking = {
  "172.17.0.1" : 1708,
  "172.17.90.43" : 7
}

labels = dict()
for key in timesAsking.keys():
	if(timesAsking[key] >= aPartirDeQueCantidadMostrarLabels):
		labels[key] = key

for ipFrom, ipSearchingFor in reader:
	g.add_edge(ipFrom,ipSearchingFor)

nodeSizesAsking = dict()
d = nx.degree(g)
for ip in d.keys():
	if not ip in nodeSizesAsking:
		try:
			nodeSizesAsking[ip] = timesAsking[ip]
		except:
			nodeSizesAsking[ip] = 0

edgeList = ips
# g.add_edges_from(edgeList)
oldMaxAsking = max(nodeSizesAsking.values())
newMax = 2000
for key in nodeSizesAsking.keys():
	nodeSizesAsking[key] = (nodeSizesAsking[key] * newMax) / oldMaxAsking

pos = nx.spring_layout(g,scale=1) #default to scale=1
nx.draw(g,pos, labels = labels,node_color = "#97edea",with_labels=True,edge_color="grey",width=0.5,node_size=[v for v in nodeSizesAsking.values()])
plt.show()
# nx.draw(g,pos, with_labels=True,node_size=[v for v in nodeSizesBeingSearch.values()])
# plt.show()

