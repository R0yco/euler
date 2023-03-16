def sum_of_squares(ceil):
    return sum([i**2 for i in range(1,ceil+1)])

def square_of_sums(ceil):
    return sum(i for i in range(1,ceil+1)) ** 2


print(square_of_sums(100)-sum_of_squares(100))
