from sympy import isprime

given_list = [3, 5, 2, 4, 9, 6]

sum_of_square = 0
product_of_non_primes = 1
for pos, number in enumerate(given_list):
    if number%2==0 and not isprime(pos+1):
        sum_of_square += number**2
    elif number%2!=0  and not isprime(number):
        product_of_non_primes *= number
        
print(f"Sum of squares of selected even numbers: {sum_of_square}\nProduct of non-prime odd numbers: {product_of_non_primes}")

