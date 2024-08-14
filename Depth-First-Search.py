def dfs(graph, start):
    visited = set()
    traversal_order = []
    def dfs_helper(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)

    return traversal_order

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E']),
}

print(dfs(graph, 'A'))