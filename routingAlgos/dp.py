import numpy as np

def tsp_dynamic_programming(distances):
    n = len(distances)
    # Initialize memoization table
    memo = np.full((n, 2**n), np.inf)
    memo[0][1] = 0

    # Fill memoization table
    for mask in range(1, 2**n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            prev_mask = mask & ~(1 << i)
            for j in range(n):
                if i == j or not (prev_mask & (1 << j)):
                    continue
                memo[i][mask] = min(memo[i][mask], memo[j][prev_mask] + distances[j][i])

    # Find optimal tour
    tour = [0]
    mask = (1 << n) - 1
    while len(tour) < n:
        last = tour[-1]
        min_dist = np.inf
        next_city = None
        for i in range(n):
            if i == 0 or not (mask & (1 << i)):
                continue
            if distances[last][i] + memo[i][mask] < min_dist:
                min_dist = distances[last][i] + memo[i][mask]
                next_city = i
        tour.append(next_city)
        mask &= ~(1 << next_city)

    return tour, memo[0][(1<<n)-1]
