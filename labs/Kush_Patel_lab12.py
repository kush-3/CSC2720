# Kush Patel
# Lab 12 - Topological Sort
# CSC 2720

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def topological_sort_stack(self):
        indegree = {vertex: 0 for vertex in self.vertices}

        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1

        stack = []
        for vertex in sorted(self.vertices, reverse=True):
            if indegree[vertex] == 0:
                stack.append(vertex)

        topo_order = []

        while stack:
            current = stack.pop()
            topo_order.append(current)

            for neighbor in sorted(self.graph[current], reverse=True):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        if len(topo_order) != len(self.vertices):
            raise ValueError("The graph contains a cycle, so no topological ordering exists.")

        return topo_order


def main():
    g = Graph()

    # Directed edges from prerequisite -> course
    edges = [
        ("MATH 1113", "MATH 2211"),
        ("MATH 1113", "CSC 2510"),
        ("CSC 1301", "CSC 1302"),
        ("MATH 2211", "MATH 2212"),
        ("CSC 2510", "CSC 2720"),
        ("CSC 2510", "CSC 3210"),
        ("CSC 1302", "CSC 2720"),
        ("CSC 1302", "CSC 3210"),
        ("CSC 1302", "CSC 3320"),
        ("MATH 2212", "MATH 2641"),
        ("MATH 2212", "MATH 3020"),
        ("MATH 3020", "CSC 4520"),
        ("CSC 2720", "CSC 4520"),
        ("CSC 2720", "CSC 3350"),
        ("CSC 3210", "CSC 3350"),
        ("CSC 3210", "CSC 4330"),
        ("CSC 3320", "CSC 4330"),
        ("CSC 3320", "CSC 4320"),
        ("CSC 3350", "CSC 4350"),
        ("CSC 3350", "CSC 4351"),
        ("CSC 4351", "CSC 4352"),
    ]

    for u, v in edges:
        g.add_edge(u, v)

    order = g.topological_sort_stack()

    print("Valid topological order for completing the courses:")
    for i, course in enumerate(order, start=1):
        print(f"{i}. {course}")


if __name__ == "__main__":
    main()