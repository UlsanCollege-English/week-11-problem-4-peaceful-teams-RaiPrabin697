# HW04 — Peaceful Teams (Bipartite Check by BFS Coloring)

**Story intro.**  
You must split people into **two teams** so that no pair of enemies ends up on the same team. The enemy relations form an undirected graph. Can we color nodes with two colors so that every edge connects different colors?

**Technical description.**  
- **Input:** `graph` as adjacency list `dict` for an undirected graph.  
- **Output:** `bipartition(graph)` → `(left_set, right_set)` as two Python `set`s if the graph is bipartite; otherwise `None`.  
- **Constraints:**  
  - Graph may be disconnected; color each unvisited part.  
  - If a component is a single node, it can go in either set.  
- **Expected complexity:** **O(V+E)** time, **O(V)** space.

## Prompts (minimal — you drive the Steps)
- Decide the data structures (Step 4). Hint: queue for BFS; dict node→color (`0/1`).  
- Choose the traversal order across components.  
- Detect a conflict when you see an edge whose endpoints share the same color.  
- Build the two sets from the color map.

## Hints
- Start BFS from every uncolored node.  
- Color the start `0`; neighbors get `1 - color[u]`.  
- On conflict, return `None` early.

## Run tests locally
```bash
python -m pytest -q
```

## FAQ
Q: Directed edges? A: No. Undirected only.

Q: Multiple valid splits? A: Any valid pair of sets is OK.

Q: Singleton nodes? A: Place them arbitrarily; tests accept either side.

Q: Big-O? A: O(V+E) time, O(V) space.

Q: Read stdin? A: No. Implement the function.

Q: Why do my sets fail equality? A: We check validity, not exact membership of a specific side.