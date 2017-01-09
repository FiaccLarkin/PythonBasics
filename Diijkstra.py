import heapq
from pprint import pprint

"""
	Crux: - Shortest path algo with everything relative to the starting node.
			Get shortest path from starting node to every other node 
			(unless you decide to stop when you have 'seen' your destination)

		  - Use 4 independant data structures: 
		  		- dist dict
		  		- prev dict
		  		- seen set
		  		- hq priority queue (heapq) which holds the next step choices as a tuple pair; dist (priority metric), and, next node name 
		  		(plus the graph datastructure of course which is adjacency disctionary of distances)

		  - priority queue dijkstra is O(ElogV)

		  - Use a priority queue (heapq) to decide what node to move to next 
			and does any backtracking for you

		  - It traverses the graph using the priority queue to keep picking the shortest next step
		    to an adjacent node and updates the datastructures as it goes

"""


AdjGraph = {'s':{'u':10, 'x':5}, 
			'u':{'v':4, 'x':2}, 
			'v':{'y':4}, 
			'x':{'u':3, 'v':9, 'y':2},
			'y':{'s':7, 'v':6}
			}


def getMinSpanningTree(G, source):
	dist = {source: 0}
	prev = {}
	seen = set([source])
	for k in G.keys():
		dist[k] = 99999
		prev[k] = None

	hq = [(0, source)]
	while hq:
		c_tuple = heapq.heappop(hq)

		c_dist, c = c_tuple

		seen.add(c)

		for adj, adj_dist in G[c].items():

			alt = c_dist + adj_dist
			if alt < dist[adj]:
				dist[adj] = alt
				prev[adj] = c

			if adj not in seen:
				heapq.heappush(hq, (dist[adj], adj)) 
		
	return dist, prev


def printPath(G, dist, prev, source):

	destinations = set(G.keys())
	destinations.remove(source)

	for k in list(destinations):
		path = []
		c = k

		while c != source:
			c = prev[c]
			path.append( c )

		print "%s to %s takes: %s - %s \n" \
				% (source, k, dist[k], list(reversed(path))+[k])

	print "\nloopback case"
	c = prev[source]
	path = [c]
	while c != source:
			c = prev[c]
			path.append( c )

	print "%s to %s takes: %s - %s \n" \
				% (source, source, dist[k], list(reversed(path))+[source])




source = 's'
dist, prev = getMinSpanningTree(AdjGraph, source)

printPath(AdjGraph, dist, prev, source)














