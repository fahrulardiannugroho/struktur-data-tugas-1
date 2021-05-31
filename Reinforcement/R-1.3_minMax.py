def minmax(data):
    small = data[0]
    large = data[0]
    for i in data:
        if small>i:
            small = i

        if large<i:
            large = i
    return (small, large)
        


print(minmax([2,4,3,5,1]))
