def prime_factors(num,divisor=2):
    if num < 2:
        return []
    if num % divisor == 0:
        return [divisor]+prime_factors(num/divisor,divisor)
    return prime_factors(num, divisor +1)

print(prime_factors(60075143))


