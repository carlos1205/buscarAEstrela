# Using a Python dictionary to act as an adjacency list
graph = {'A': ['C'], 'B': ['C', 'D'], 'C': ['A', 'B', 'G'], 'D': ['B', 'E'], 'E': ['D', 'F'], 'F': ['E', 'J'], 'G': ['C', 'K', 'H'], 'H': ['G', 'I', 'K', 'L'], 'I': [
    'H', 'J'], 'J': ['I', 'M'], 'K': ['G', 'H', 'N'], 'L': ['H', 'M'], 'M': ['J', 'L', 'P'], 'N': ['K', 'O', 'Q'], 'O': ['N', 'P'], 'P': ['O', 'T'], 'Q': ['N', 'R'], 'R': [
    'Q', 'S'], 'S': ['R', 'T'], 'T': ['S', 'U'], 'U': ['T']
}


def dfs(adj_list, start, target, path, visited=set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            result = dfs(adj_list, neighbour, target, path, visited)
            if result is not None:
                return result
            path.pop()
    return None


def searchDFS(root, destiny):
    traversal_path = []
    traversal_path = dfs(graph, root, destiny, traversal_path)
    print(traversal_path)