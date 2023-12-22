from heapq import heappush, heappop

def salesman(city_map):
    n = len(city_map)
    best_cost = float('inf')
    best_path = []

    # Precompute the minimum outgoing edge cost for each city
    min_outgoing = [min(filter(lambda x: x > 0, row)) for row in city_map]

    def lower_bound(path, visited, current_cost):
        lb = current_cost
        for city in range(n):
            if city not in visited:
                lb += min_outgoing[city]
        return lb

    # Priority queue of nodes; each node is a tuple (lower_bound, current_cost, path, visited)
    queue = [(0, 0, [0], {0})]

    while queue:
        lb, current_cost, path, visited = heappop(queue)

        if lb >= best_cost:
            continue

        last_city = path[-1]
        if len(path) == n:
            total_cost = current_cost + city_map[last_city][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path
            continue

        for next_city in range(n):
            if next_city not in visited:
                new_path = path + [next_city]
                new_cost = current_cost + city_map[last_city][next_city]
                new_visited = visited | {next_city}
                new_lb = lower_bound(new_path, new_visited, new_cost)
                heappush(queue, (new_lb, new_cost, new_path, new_visited))

    return best_path + [0] if best_path else None



if __name__ == "__main__":
    
    cost = 0

    city_map = [
        [ 0, 12, 19, 16, 29],
        [12,  0, 27, 25,  5],
        [19, 27,  0,  8,  4],
        [16, 25,  8,  0, 14],
        [29,  5,  4, 14,  0]
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45

