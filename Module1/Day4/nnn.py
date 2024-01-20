def print_multiplication_table():
    try:
        max_number = int(input("Enter the maximum number for the multiplication table: "))
        for number in range(1, max_number + 1):
            print(f"\nMultiplication Table for {number}:")
            for i in range(1, 11):
                result = number * i
                print(f"{number} x {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print_multiplication_table()
