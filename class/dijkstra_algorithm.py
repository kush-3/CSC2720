"""
Dijkstra's Algorithm Implementation
CSC2720 - Data Structures and Algorithms
Author: Student

This module implements Dijkstra's shortest path algorithm for finding the shortest
path from a source vertex to all other vertices in a weighted directed graph.
"""

import heapq
from collections import defaultdict
import math


class Graph:
    """
    Graph class to represent a weighted directed graph using adjacency list representation.
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        self.vertices = set()
        self.edges = defaultdict(list)  # adjacency list: vertex -> [(neighbor, weight), ...]
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""    
        self.vertices.add(vertex)
    
    def add_edge(self, source, destination, weight):
        """
        Add a weighted edge from source to destination.
        
        Args:
            source: Source vertex
            destination: Destination vertex  
            weight: Weight of the edge (must be non-negative for Dijkstra's)
        """
        if weight < 0:
            raise ValueError("Dijkstra's algorithm doesn't work with negative weights")
        
        self.add_vertex(source)
        self.add_vertex(destination)
        self.edges[source].append((destination, weight))
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex with their edge weights."""
        return self.edges[vertex]
    
    def __str__(self):
        """String representation of the graph."""
        result = "Graph:\n"
        for vertex in sorted(self.vertices):
            neighbors = self.get_neighbors(vertex)
            if neighbors:
                neighbor_str = ", ".join([f"{dest}({weight})" for dest, weight in neighbors])
                result += f"  {vertex} -> {neighbor_str}\n"
            else:
                result += f"  {vertex} -> []\n"
        return result


def dijkstra(graph, source):
    """
    Implement Dijkstra's algorithm to find shortest paths from source to all vertices.
    
    Args:
        graph: Graph object
        source: Source vertex to start from
        
    Returns:
        tuple: (distances, previous) where:
            - distances: dict mapping vertex -> shortest distance from source
            - previous: dict mapping vertex -> previous vertex in shortest path
    """
    if source not in graph.vertices:
        raise ValueError(f"Source vertex {source} not in graph")
    
    # Initialize distances and previous vertices
    distances = {vertex: math.inf for vertex in graph.vertices}
    previous = {vertex: None for vertex in graph.vertices}
    distances[source] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, source)]
    visited = set()
    
    while pq:
        # Get vertex with minimum distance
        current_dist, current_vertex = heapq.heappop(pq)
        
        # Skip if already visited (handles duplicate entries in pq)
        if current_vertex in visited:
            continue
            
        visited.add(current_vertex)
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
                
            # Calculate new distance through current vertex
            new_distance = current_dist + weight
            
            # If we found a shorter path, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (new_distance, neighbor))
    
    return distances, previous


def get_shortest_path(previous, source, destination):
    """
    Reconstruct the shortest path from source to destination using previous vertices.
    
    Args:
        previous: Dictionary mapping vertex -> previous vertex in shortest path
        source: Source vertex
        destination: Destination vertex
        
    Returns:
        list: Shortest path from source to destination, or None if no path exists
    """
    if destination not in previous or previous[destination] is None and destination != source:
        return None  # No path exists
    
    path = []
    current = destination
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return path if path[0] == source else None


def print_results(graph, source, distances, previous):
    """Print the results of Dijkstra's algorithm in a formatted way."""
    print(f"\nDijkstra's Algorithm Results (Source: {source})")
    print("=" * 50)
    
    for vertex in sorted(graph.vertices):
        dist = distances[vertex]
        if dist == math.inf:
            print(f"Vertex {vertex}: No path from {source}")
        else:
            path = get_shortest_path(previous, source, vertex)
            path_str = " -> ".join(map(str, path))
            print(f"Vertex {vertex}: Distance = {dist}, Path = {path_str}")


def main():
    """
    Main function demonstrating Dijkstra's algorithm with example graphs.
    """
    print("Dijkstra's Shortest Path Algorithm")
    print("=" * 40)
    
    # Example 1: Simple graph
    print("\nExample 1: Simple weighted graph")
    g1 = Graph()
    
    # Add edges: (source, destination, weight)
    edges1 = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for source, dest, weight in edges1:
        g1.add_edge(source, dest, weight)
    
    print(g1)
    
    # Run Dijkstra's algorithm
    distances1, previous1 = dijkstra(g1, 'A')
    print_results(g1, 'A', distances1, previous1)
    
    # Example 2: Larger graph with numbers as vertices
    print("\n" + "=" * 60)
    print("Example 2: Larger graph with numeric vertices")
    
    g2 = Graph()
    edges2 = [
        (0, 1, 7),
        (0, 2, 9),
        (0, 5, 14),
        (1, 2, 10),
        (1, 3, 15),
        (2, 3, 11),
        (2, 5, 2),
        (3, 4, 6),
        (4, 5, 9)
    ]
    
    for source, dest, weight in edges2:
        g2.add_edge(source, dest, weight)
    
    print(g2)
    
    distances2, previous2 = dijkstra(g2, 0)
    print_results(g2, 0, distances2, previous2)
    
    # Example 3: Demonstrate specific path finding
    print("\n" + "=" * 60)
    print("Example 3: Finding specific shortest paths")
    
    source_vertex = 'A'
    target_vertices = ['D', 'E']
    
    for target in target_vertices:
        path = get_shortest_path(previous1, source_vertex, target)
        if path:
            distance = distances1[target]
            print(f"Shortest path from {source_vertex} to {target}: {' -> '.join(path)} (Distance: {distance})")
        else:
            print(f"No path found from {source_vertex} to {target}")


if __name__ == "__main__":
    main()