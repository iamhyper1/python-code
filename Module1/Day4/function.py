def check_prime(numner):
    counter=0
    prime=False
    for i in range(1, number+1):
      if number % i ==0:
            counter= counter+1
            if counter == 2:
                counter= counter+1

    if counter == 2:  
        prime=True 
        return prime
    
number=int(input("Enter a number to check prime"))
check_prime_bool=check_prime(number)
if check_prime_bool: 
     print("Prime Number")
else:
     print("Not Prime")
