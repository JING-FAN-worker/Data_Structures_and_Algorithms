def binpack(items, S):
    # Sort the items in decreasing order
    sorted_items = sorted(items, reverse=True)
    bins = []
    for item in sorted_items:
        # Try to fit the item in an existing bin
        placed = False
        for bin in bins:
            if sum(bin) + item <= S:
                bin.append(item)
                placed = True
                break
        # If the item does not fit in any existing bin, open a new bin
        if not placed:
            bins.append([item])
    return bins

# Example usage
if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10
    bins = binpack(items, B)
    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")


if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    print("One feasible solution:")
    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

    # A possible output:
    #   bin 1: [9]
    #   bin 2: [3, 3, 4]
    #   bin 3: [6, 3]
    #   bin 4: [10]
    #   bin 5: [6]
    #   bin 6: [8]
    #   bin 7: [6]
