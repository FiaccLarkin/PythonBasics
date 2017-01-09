graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B']),
         'F': set(['C', 'E'])}


print "\n__________________ Depth First Search"

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
        	print vertex
        	visited.add(vertex)
        	stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A')


print "\n__________________ Breath First Search"
# uses a queue
# guarantees to return the shortest-path first

from collections import deque

def bfs(graph, start):
    visited, stack = set(), deque(start)
    while stack:
        vertex = stack.popleft()
        if vertex not in visited:
        	print vertex
        	visited.add(vertex)
        	stack.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A')