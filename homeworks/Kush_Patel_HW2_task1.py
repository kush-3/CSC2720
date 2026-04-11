

import heapq


def _dijkstra(graph, start, nodes):
    """Return shortest distances from start to every node using Dijkstra's algorithm."""
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Skip outdated heap entries.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


def get_all_pairs_shortest_path(graph):
    """
    Takes an adjacency list of a weighted undirected graph and returns
    a 2D list representing the shortest-path distances between all pairs of nodes.
    """
    # Sort node labels so the matrix order matches 0, 1, 2, ... when labels are strings.
    nodes = sorted(graph.keys(), key=int)
    shortest_path_matrix = []

    # Run Dijkstra from each node and build one row of the matrix each time.
    for start in nodes:
        distances = _dijkstra(graph, start, nodes)
        row = [distances[node] for node in nodes]
        shortest_path_matrix.append(row)

    return shortest_path_matrix


if __name__ == "__main__":
    weightedGraph = {
        '0': [('1', 2), ('2', 8), ('3', 3)],
        '1': [('0', 2), ('5', 7)],
        '2': [('0', 8), ('3', 4), ('4', 2)],
        '3': [('0', 3), ('2', 4), ('4', 1)],
        '4': [('2', 2), ('3', 1), ('5', 12)],
        '5': [('4', 12), ('1', 7)]
    }

    result = get_all_pairs_shortest_path(weightedGraph)

    for row in result:
        print(row)