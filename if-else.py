n = int(input("Enter an integer between 1 and 100: "))

if n < 1 or n > 100:
    print("Invalid input. Please enter an integer between 1 and 100.")
else:
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
