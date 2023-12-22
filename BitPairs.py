'''We are given a bit string which each character is either 0 or 1. Count the sum of each distance of bit pairs where both bits are 1.'''
def pairs(s):
    a = 0
    b = [i for i, char in enumerate(s) if char == "1"]
    for i in range(0,len(b)):
        a += b[i]*(2*i - len(b) + 1)
    return a

'''if __name__ == "__main__":
    print(pairs("100101"))'''