def triangle(a, b, c):
    list = [a, b, c]
    for i in range(1, len(list)):
        d = i - 1
        while (d >= 0 and list[d]>list[d+1]):
            e = list[d]
            list[d] = list[i]
            list[i] = e
            d = d-1
    if list[2]-list[0] >= list[1] or list[0] + list[1] <= list[2] or a <= 0 or b<=0 or c<=0:
        return 'False'
    else:
        return 'True'

'''if __name__ == "__main__":
    print(triangle(3, 5, 4))'''