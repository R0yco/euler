def smallest_divided_by(ceiling):
    num = ceiling
    inner_counter = 0
    division_results=[]
    while True:
        division_results=[]
        inner_counter = 1
        for i in range(1,ceiling):
            if num % i != 0:
                break
            division_results += [num / i]
            inner_counter += 1
        if inner_counter == ceiling :
            return num
        num += 10

print(smallest_divided_by(20))
