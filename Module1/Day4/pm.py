def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_multiplication_table_if_prime(number):
    if is_prime(number):
        print(f"{number} is a prime number.")
        print(f"Multiplication Table for {number}")
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")
    else:
        print(f"{number} is not a prime number.")
try:
    user_input = int(input("Enter a number to check if it's prime and print its multiplication table: "))
    print_multiplication_table_if_prime(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number")
