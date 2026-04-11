

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add a directed edge from u to v."""
        self.graph[u].append(v)

    def _topological_sort_util(self, vertex, visited, stack):
        """Depth-first search helper that pushes nodes onto a stack after exploring neighbors."""
        visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self._topological_sort_util(neighbor, visited, stack)

        # Push the current vertex after all of its neighbors are processed.
        stack.append(vertex)

    def topological_sort(self):
        """Return a topological ordering using the stack-based DFS approach."""
        visited = {i: False for i in range(self.vertices)}
        stack = []

        for vertex in range(self.vertices):
            if not visited[vertex]:
                self._topological_sort_util(vertex, visited, stack)

        # Reverse the stack to get the final topological order.
        return stack[::-1]


if __name__ == "__main__":
    # Example DAG for the video demonstration.
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    order = g.topological_sort()
    print("Topological Sort Order:", order)