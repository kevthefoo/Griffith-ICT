def compute_cost(distance, toll, mode):
    if mode == "distance":
        return distance
    elif mode == "toll":
        return toll
    elif mode == "balanced":
        return distance + toll

def dijkstra(graph, start, end, mode):
    nodes = {}
    for v in graph:
        nodes[v] = {
            "dist": float("inf"),
            "toll": float("inf"),
            "cost": float("inf"),
            "prev": None
        }

    nodes[start]["dist"] = 0
    nodes[start]["toll"] = graph[start]["toll"]
    nodes[start]["cost"] = compute_cost(0, graph[start]["toll"], mode)

    queue = [start]
    visited = set()

    while queue:
        # Select node with lowest cost
        current = min(queue, key=lambda x: nodes[x]["cost"])
        queue.remove(current)

        if current == end:
            break

        visited.add(current)

        for neighbor in graph[current]["roads"]:
            if neighbor in visited:
                continue

            edge_dist = graph[current]["roads"][neighbor]
            new_dist = nodes[current]["dist"] + edge_dist
            new_toll = nodes[current]["toll"] + graph[neighbor]["toll"]
            new_cost = compute_cost(new_dist, new_toll, mode)

            if new_cost < nodes[neighbor]["cost"]:
                nodes[neighbor]["dist"] = new_dist
                nodes[neighbor]["toll"] = new_toll
                nodes[neighbor]["cost"] = new_cost
                nodes[neighbor]["prev"] = current
                if neighbor not in queue:
                    queue.append(neighbor)

    # Reconstruct path
    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = nodes[node]["prev"]

    return {
        "path": path,
        "distance": nodes[end]["dist"],
        "toll": nodes[end]["toll"],
        "cost": nodes[end]["cost"]
    }


Map = {
    "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
    "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
    "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
    "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
    "E": {"toll": 5, "roads": {"C": 6, "D": 2}},
}

result = dijkstra(Map, "A", "E", "toll")
print(f"Path: {result['path']}")

# Analysis and Explanation
# Time Complexity = O(V² + E)
# Space Complexity = O(V + E)