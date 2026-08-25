number = int(input("Enter a number:"))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if number <= 1:
    print("this is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime")
    else:
        print("This number is prime")
