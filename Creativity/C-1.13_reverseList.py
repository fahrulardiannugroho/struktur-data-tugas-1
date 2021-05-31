nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reverse(data):
    numRevers = []
    n = len(data) - 1
    for i in range(n, -1, -1):
        numRevers.append(data[i])
    return numRevers

print(nums)
print(reverse(nums))
