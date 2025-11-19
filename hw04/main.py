from collections import deque

def bipartition(graph):
    color = {}  # node → 0 or 1 groups

    for start in graph:  # handle disconnected graph
        if start not in color:
            color[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    else:
                        # conflict means NOT bipartite
                        if color[v] == color[u]:
                            return None

    # Build left/right sets
    left = {node for node, c in color.items() if c == 0}
    right = set(color) - left
    return left, right
