from Day5.m import is_prime
def calculate_result(number):
    if is_prime(number):
        print(f"{number} is prime. Multiplication table:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        result = number**2 + 5 * number + 2
        print(f"{number} is not prime. Result of x^2 + 5x + 2: {result}")

user_input = int(input("Enter a number: "))
calculate_result(user_input)
