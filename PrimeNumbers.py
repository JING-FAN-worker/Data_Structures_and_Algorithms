def primes(N):
    b = 0
    for i in range(1,N+1):
        for a in range(1,i):
            if i%a == 0 and a != 1:
                break
            elif a == i-1:
                b = b+1     
    return b
        
'''if __name__ == "__main__":
    print(primes(7))'''