graph = {'A': ['C'], 'B': ['C', 'D'], 'C': ['A', 'B', 'G'], 'D': ['B', 'E'], 'E': ['D', 'F'], 'F': ['E', 'J'], 'G': ['C', 'K', 'H'], 'H': ['G', 'I', 'K', 'L'], 'I': [
    'H', 'J'], 'J': ['I', 'M'], 'K': ['G', 'H', 'N'], 'L': ['H', 'M'], 'M': ['J', 'L', 'P'], 'N': ['K', 'O', 'Q'], 'O': ['N', 'P'], 'P': ['O', 'T'], 'Q': ['N', 'R'], 'R': [
    'Q', 'S'], 'S': ['R', 'T'], 'T': ['S', 'U'], 'U': ['T']
}


def bfs(graph, start, end):
    # Fila com os caminhos
    queue = []
    # definimos uma lista para gravar os itens já visitados
    visited = set()
    # Coloca o inicio na fila
    queue.append([start])
    visited.add(start)
    while queue:
        # Pega o primeiro caminho da fila
        path = queue.pop(0)
        # Pega o último nó do caminho
        node = path[-1]
        # caminho encontrado, finaliza
        if node == end:
            return path
        # enumere todos os nós adjacentes, construa um novo caminho e coloque-o na fila
        for adjacent in graph.get(node, []):
            # se a aresta ainda não foi visitada
            if adjacent not in visited:
                new_path = list(path)
                new_path.append(adjacent)
                visited.add(adjacent)
                queue.append(new_path)


def searchBFS(root, destiny):
    print(bfs(graph, root, destiny))
