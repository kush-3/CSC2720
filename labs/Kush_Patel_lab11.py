def extract_cycle(adj_list, start):
    """
    This function extracts a cycle from the adjacency list starting from the given start node. 
    Uses Depth First search to find the cycle.

    Required parameters;
        adj_list: Adjacencu list representing the graph
        start: Starting node for the cycle
    Returns:
        List representing the cycle, or empty list if no cycle is found
    """
    if start < 0 or start >= len(adj_list):
        return []

    def dfs(node, path):
        for neighbor in adj_list[node]:
            if neighbor == start and len(path) >= 1:
                return path + [start]
            if neighbor not in path:
                found = dfs(neighbor, path + [neighbor])
                if found:
                    return found
        return None

    output = dfs(start, [start])
    return output if output else []



def main():
    # Adjacency list representing the graph
    adj = [
        [1, 3],
        [2],
        [4],
        [],
        [0, 3],
        [2],
    ]
    #  driver code.
    print("="*50)
    print("Test cases: \n")
    print(extract_cycle(adj, 0), "Expected: [0, 1, 2, 4, 0] \n")
    print(extract_cycle(adj, 1), "Expected: [1, 2, 4, 0, 1] \n")
    print(extract_cycle(adj, 3), "Expected: [] \n")
    print("="*50)

if __name__ == "__main__":
    main()