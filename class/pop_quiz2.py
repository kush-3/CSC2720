# Question: What are the time complexities of the following operations for a graph: (adjaceny list representation)
# Briefly explain the reason. 
# 1: Add a node:
# 2: remove a node:
# 3: Check if two nodes are adjacent or not.
#  save a word doc on desktop, and submit it on iCollege. 



# answers:
# Adjacency List Representation — Time Complexities

# 1. Add a Node

# Time Complexity: O(1)
# Reason:
# Adding a node just means adding a new empty list to store its neighbors. No need to scan existing nodes or edges.

# ⸻

# 2. Remove a Node

# Time Complexity: O(V + E) (worst case)
# Reason:
# To remove a node:
# 	•	Remove its adjacency list → O(1)
# 	•	But you must also remove this node from all other nodes’ adjacency lists
# 	•	This requires scanning all vertices and edges → O(V + E)

# ⸻

# 3. Check if Two Nodes are Adjacent

# Time Complexity: O(deg(V)) (or O(V) worst case)
# Reason:
# To check if node A is adjacent to B, you must search B in A’s adjacency list
# 	•	This takes time proportional to the degree of node A
# 	•	Worst case (dense graph): O(V)