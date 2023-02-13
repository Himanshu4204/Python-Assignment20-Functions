#Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.?
def is_prime(n):
    if n < 2:
        return "Not Prime Number"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime Number"
    return "Prime Number"

print(is_prime(1))    
print(is_prime(12)) 
print(is_prime(31))   

