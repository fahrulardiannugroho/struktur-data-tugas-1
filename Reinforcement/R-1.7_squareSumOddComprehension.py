def squares_sum(n):
    return sum(number**2 for number in range(0,n) if number%2 != 0)

print(squares_sum(6)) 
