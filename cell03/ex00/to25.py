number = int(input("Enter a number: "))

if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, myvariable is " + str(number))
        number += 1
