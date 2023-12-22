'''An array of n number of integers must be split in two sub arrays so that every integer of left sub array are smaller than every integer of right sub array. In how many points the array can be split in half?'''
def split(T):
    a = 0
    for i in range(1,len(T)):
        if max(T[0:i])<min(T[i:len(T)]):
            a = a + 1
    return a

'''if __name__ == "__main__":
    print(split([1,2,3,4,5]))'''