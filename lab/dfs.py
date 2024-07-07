def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))

    return dfs_order

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example usage
dfs_result = dfs(graph, 'A')
print("DFS order:", dfs_result)
