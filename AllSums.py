def sums(numbers):
    unique_sums = {0}
    #Such a magical algorithm was invented by predecessors
    for number in numbers:
        current_sums = set()
        for sum_ in unique_sums:
            current_sums.add(sum_ + number)
        unique_sums.update(current_sums)
    unique_sums.discard(0)
    return len(unique_sums)

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121