# only adding methods relevant to constructing the graph related structures and traversing

# lets say we have a Directed Edge List 
n = 8 

A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Convert Edge List into Adjacency Matrix 

# initialize matrix
M = []

# then for n vertices we want n rows and n columns 

for i in range(n): 
    M.append([0] * n)

for start, end in A: 
    M[start][end] = 1

    # Remember that this is directed (unidirectional)
    # if we want it to be undirected (bidirectional), just uncomment this line
    #M[start][end] = 1

# Now we have: 
"""
Directed: 
[[0, 1, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 1, 0, 1, 1, 0], 
 [0, 0, 1, 0, 0, 1, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

Undirected: 
[[0, 1, 0, 1, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 0, 1, 1, 0, 0, 0], 
 [1, 0, 0, 0, 1, 0, 1, 1, 0], 
 [0, 0, 1, 1, 0, 1, 0, 0, 0], 
 [0, 0, 1, 0, 1, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0, 0, 0]]

note that the undirected matrix is a symmetric matrix
-> symmetrical across the diagonal axis 

"""

# Convert Edge list into Adjacency List (maybe more useful)

from collections import defaultdict

# initializes default value for a key to be an empty list
D = defaultdict(list)

for start, end in A: 
    D[start].append(end)

    # If we want to use an undirected graph
    #D[end].append(start)

# Now we have: 
"""
 {0: [1, 3], 1: [2], 3: [4, 6, 7], 4: [2, 5], 5: [2]}

Quick and easy access to see what each node is connected to  
"""

# TRAVERSAL  

# DFS with Recursion O(V + E) where V is the number of nodes and E is the number of edges 

def dfs_recursive(node): 
    print(node)
    for neighbor in D[node]: 
        if neighbor not in seen: 
            seen.add(neighbor)
            dfs_recursive(neighbor)

source = 0 
seen = set() 
seen.add(source)
dfs_recursive(source)

"""
Output: 
0
1
2
3
4
5
6
7
"""

# DFS with iteration 

source = 0 
seen = set() 
seen.add(source)
stack = [source]

while stack: 
    node = stack.pop()
    print(node)
    for neighbor in D[node]: 
        if neighbor not in seen: 
            seen.add(neighbor)
            stack.append(neighbor)

"""
Output: 
0
3
7
6
4
5
2
1
"""

# BFS with Queue

source = 0 
from collections import deque 

source = 0 
seen = set() 
seen.add(source)
q = deque()
q.append(source)

while q: 
    node = q.popleft()
    print(node)
    for neighbor in D[node]: 
        if neighbor not in seen: 
            seen.add(neighbor)
            q.append(neighbor)

"""
Output: 
0
1
3
2
4
6
7
5
"""

# Class based storage in memory 
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.neighbors = []

    def __str__ (self): 
        return f'Node({self.value})'

    def display (self): 
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is connected to=: {connections}'


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)
C.neighbors.append(D)
D.neighbors.append(C)

B.display()
'''
Output: 
B is connected to=: ['A']
'''
