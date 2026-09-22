firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))

X = firstnumber * secondnumber
print(firstnumber, "x", secondnumber, "=", X)

if X > 0:
    print("The result is positive.")
elif X < 0:
    print("The result is negative.")
else:
    print("The result is zero.")
