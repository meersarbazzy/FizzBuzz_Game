for num in range(1, 101):  # Loop through numbers from 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # Check if divisible by both 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:  # Check if divisible by 3
        print("Fizz")
    elif num % 5 == 0:  # Check if divisible by 5
        print("Buzz")
    else:  # Print the number if none of the above conditions are met
        print(num)
