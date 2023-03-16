from itertools import combinations

def get_products(digit_num):
    numbers = [i for i in range(10**(digit_num-1),10**digit_num)]
    combs = combinations(numbers, 2)
    products = [i * j for i,j in combs]
    return products 

def is_palindromic(num):
    return str(num)[::-1] == str(num)

palindromes = filter(is_palindromic,get_products(3))
print(max(palindromes))
