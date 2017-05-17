import matplotlib.pyplot as plt
import matplotlib.colors as colors
from networkx import *
import csv

reader = csv.reader(open("S1-shopping.csv"), delimiter=",")
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
nodeSizesBeingSearch = dict()
d = nx.degree(g)
for ip in d.keys():
	if not ip in nodeSizesAsking:
		try:
			nodeSizesAsking[ip] = timesAsking[ip]
		except:
			nodeSizesAsking[ip] = 5


edgeList = ips
# g.add_edges_from(edgeList)
oldMaxAsking = max(nodeSizesAsking.values())
newMax = 2000
for key in nodeSizesAsking.keys():
	nodeSizesAsking[key] = (nodeSizesAsking[key] * newMax) / oldMaxAsking

colormap = plt.cm.Reds
pos = nx.spring_layout(g,scale=1) #default to scale=1
nx.draw(
	g,
	pos, 
	labels = labels,
	node_color = range(len(g.nodes())),
	with_labels=True,
	edge_color="grey",
	width=0.5,
	node_size=[v for v in nodeSizesAsking.values()],
	cmap=colormap,
	linewidths=0.5,
	linecolors="blue")

sm = plt.cm.ScalarMappable(cmap=colormap, norm=colors.Normalize(vmin=0, vmax=max(g.degree().values())))
sm._A = []
plt.colorbar(sm, shrink=0.8)
plt.show()
# nx.draw(g,pos, with_labels=True,node_size=[v for v in nodeSizesBeingSearch.values()])
# plt.show()
 
