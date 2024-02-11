def check_and_multiply_or_print_table(number):
    if number < 0:
        result = number * 5
        print(f"The number is negative, Multiplication Table of the number: {result}")
    elif number > 0:
        print(f"The number is positive. Multiplication table:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        print("The number is zero.")

user_input = float(input("Enter a number: "))
check_and_multiply_or_print_table(user_input)
