'''An array of n number of integers must be modified so that no two consecutive integers are equal.'''
def changes(A):
    num = 1
    for i in range(0,len(A)):
        if A[i] > num:
            num = A[i]

    a = num + 1
    c = 0
    for i in range(1,len(A)):
        b = A[i - 1]
        if A[i] == b:
            A[i] = a
            c = c + 1
    return c


'''if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))'''
