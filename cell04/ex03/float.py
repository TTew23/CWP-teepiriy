x = float((input("Give me a number: ")))
if x == int(x):
    print(f"{x} is an integer.")
elif x == float(x):
    print(f"{x} is a decimal.")