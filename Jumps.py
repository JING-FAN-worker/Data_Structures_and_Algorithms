def jumps(n, a, b):
    #I learnt it from internet
    ways = [0] * (n + 1)
    ways[0] = 1
    for current_level in range(1, n + 1):
        if current_level - a >= 0:
            ways[current_level] += ways[current_level - a]
        if current_level - b >= 0:
            ways[current_level] += ways[current_level - b]
    return ways[n]

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937